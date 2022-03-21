from selenium import webdriver
from datetime import datetime, date, time
import time as tm
import pytz
import uuid
import constant.db as db
import constant.constants as const
import re

import boto3


#os.environ['TZ'] = 'Asia/Ulaanbaatar'
#time.tzset()
options = webdriver.ChromeOptions()
#options.binary_location = '/opt/headless-chromium'
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('driver/chromedriver', chrome_options=options)

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.replace("&nbsp;", "").replace("·", "")
    return cleantext

def check_published_date(found_date):
    try:
        time_terms = const.gogo_date_terms.terms
        cleared_time = found_date
        c = cleanhtml(cleared_time)
        b = c.strip()
        for key, value in time_terms.items():
                if key == str(b):
                    b = value
                    return b
    except:
        return b


tz = pytz.timezone("Asia/Ulaanbaatar")
def is_today(p_date):
    the_date = date.today()
    day_today = datetime.combine(the_date, time())
    p_date = datetime.strptime(p_date, '%Y-%m-%d %H:%M')
    #print(p_date)
    print("TODAY: ", day_today)
    print("P_DATE: ", p_date)
    if p_date > day_today:
        return True
    else:
        return False

def isXpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def lambda_handler(event, context):

    target_url = "https://ikon.mn/"
    driver.get(target_url)
    driver.implicitly_wait(30)
    xpath_element = "//*[@id='wrapper']/div[1]/div[3]/div[2]/div[2]/div[2]"
    fBody = driver.find_element_by_xpath(xpath_element)
    scroll = 0
    # little scroll down the page
    while scroll < 3:  # this will scroll 3 times
        driver.execute_script("window.scrollTo(0, 700);")
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        scroll += 1
        driver.implicitly_wait(6)
    tm.sleep(3)
    if isXpath("//*[@class='newsitem']"):
        xpath_news_list = driver.find_elements_by_xpath("//*[@class='newsitem']")
        print(len(xpath_news_list))
        lm = len(xpath_news_list)
        links =[]
        for i in range(0,lm):
            links.append(xpath_news_list[i].get_attribute("id"))
        lmm = len(links)
        for j in range(0,lmm):
            news_link = driver.find_element_by_xpath('//*[@id="'+links[j]+'"]/div/a')
            #print(news_link.get_attribute("href"))
            x_path_date =  driver.find_element_by_xpath('//*[@id="'+links[j]+'"]/div[2]/div[@class="dtime"]/span[2]')
            p_date = x_path_date.get_attribute("innerHTML")
            p_date = cleanhtml(p_date)
            job_id = uuid.uuid4()
            p_date = check_published_date(p_date)
            if is_today(p_date) == True:
                status = "ikon's_new"
                link = news_link.get_attribute("href")
                print(p_date, link, j, "today-news")
                #db.update_crawling_results(str(job_id), status, link, p_date)
            else:
                print(news_link.get_attribute("href"), j, "old news")
                #print("old news")

        return "sucess"


print(lambda_handler(event="test1", context="test_context"))


