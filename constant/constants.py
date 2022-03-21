import datetime
from datetime import date, timedelta
class gogo_date_terms:
    terms={
        "Дөнгөж сая": datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        "Өнөөдөр": datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        # "Өчигдөр":(datetime.datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M'),
        "1 өдөр": (datetime.datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M'),
        "2 өдөр": (datetime.datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M'),
        "3 өдөр": (datetime.datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d %H:%M'),
        "1 цаг":(datetime.datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M'),
        "2 цаг":(datetime.datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M'),
        "3 цаг":(datetime.datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M'),
        "4 цаг":(datetime.datetime.now() - timedelta(hours=4)).strftime('%Y-%m-%d %H:%M'),
        "5 цаг":(datetime.datetime.now() - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M'),
        "6 цаг":(datetime.datetime.now() - timedelta(hours=6)).strftime('%Y-%m-%d %H:%M'),
        "7 цаг":(datetime.datetime.now() - timedelta(hours=7)).strftime('%Y-%m-%d %H:%M'),
        "8 цаг":(datetime.datetime.now() - timedelta(hours=8)).strftime('%Y-%m-%d %H:%M'),
        "9 цаг":(datetime.datetime.now() - timedelta(hours=9)).strftime('%Y-%m-%d %H:%M'),
        "10 цаг":(datetime.datetime.now() - timedelta(hours=10)).strftime('%Y-%m-%d %H:%M'),
        "11 цаг":(datetime.datetime.now() - timedelta(hours=11)).strftime('%Y-%m-%d %H:%M'),
        "12 цаг":(datetime.datetime.now() - timedelta(hours=12)).strftime('%Y-%m-%d %H:%M'),
        "13 цаг":(datetime.datetime.now() - timedelta(hours=13)).strftime('%Y-%m-%d %H:%M'),
        "14 цаг":(datetime.datetime.now() - timedelta(hours=14)).strftime('%Y-%m-%d %H:%M'),
        "15 цаг":(datetime.datetime.now() - timedelta(hours=15)).strftime('%Y-%m-%d %H:%M'),
        "16 цаг":(datetime.datetime.now() - timedelta(hours=16)).strftime('%Y-%m-%d %H:%M'),
        "17 цаг":(datetime.datetime.now() - timedelta(hours=17)).strftime('%Y-%m-%d %H:%M'),
        "18 цаг":(datetime.datetime.now() - timedelta(hours=18)).strftime('%Y-%m-%d %H:%M'),
        "19 цаг":(datetime.datetime.now() - timedelta(hours=19)).strftime('%Y-%m-%d %H:%M'),
        "20 цаг":(datetime.datetime.now() - timedelta(hours=20)).strftime('%Y-%m-%d %H:%M'),
        "21 цаг":(datetime.datetime.now() - timedelta(hours=21)).strftime('%Y-%m-%d %H:%M'),
        "22 цаг":(datetime.datetime.now() - timedelta(hours=22)).strftime('%Y-%m-%d %H:%M'),
        "23 цаг":(datetime.datetime.now() - timedelta(hours=23)).strftime('%Y-%m-%d %H:%M'),
        "1 минут":(datetime.datetime.now() - timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M'),
        "2 минут":(datetime.datetime.now() - timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M'),
        "3 минут":(datetime.datetime.now() - timedelta(minutes=3)).strftime('%Y-%m-%d %H:%M'),
        "4 минут":(datetime.datetime.now() - timedelta(minutes=4)).strftime('%Y-%m-%d %H:%M'),
        "5 минут":(datetime.datetime.now() - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M'),
        "6 минут":(datetime.datetime.now() - timedelta(minutes=6)).strftime('%Y-%m-%d %H:%M'),
        "7 минут":(datetime.datetime.now() - timedelta(minutes=7)).strftime('%Y-%m-%d %H:%M'),
        "8 минут":(datetime.datetime.now() - timedelta(minutes=8)).strftime('%Y-%m-%d %H:%M'),
        "9 минут":(datetime.datetime.now() - timedelta(minutes=9)).strftime('%Y-%m-%d %H:%M'),
        "10 минут":(datetime.datetime.now() - timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M'),
        "11 минут":(datetime.datetime.now() - timedelta(minutes=11)).strftime('%Y-%m-%d %H:%M'),
        "12 минут":(datetime.datetime.now() - timedelta(minutes=12)).strftime('%Y-%m-%d %H:%M'),
        "13 минут":(datetime.datetime.now() - timedelta(minutes=13)).strftime('%Y-%m-%d %H:%M'),
        "14 минут":(datetime.datetime.now() - timedelta(minutes=14)).strftime('%Y-%m-%d %H:%M'),
        "15 минут":(datetime.datetime.now() - timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M'),
        "16 минут":(datetime.datetime.now() - timedelta(minutes=16)).strftime('%Y-%m-%d %H:%M'),
        "17 минут":(datetime.datetime.now() - timedelta(minutes=17)).strftime('%Y-%m-%d %H:%M'),
        "18 минут":(datetime.datetime.now() - timedelta(minutes=18)).strftime('%Y-%m-%d %H:%M'),
        "19 минут":(datetime.datetime.now() - timedelta(minutes=19)).strftime('%Y-%m-%d %H:%M'),
        "20 минут":(datetime.datetime.now() - timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M'),
        "21 минут":(datetime.datetime.now() - timedelta(minutes=21)).strftime('%Y-%m-%d %H:%M'),
        "22 минут":(datetime.datetime.now() - timedelta(minutes=22)).strftime('%Y-%m-%d %H:%M'),
        "23 минут":(datetime.datetime.now() - timedelta(minutes=23)).strftime('%Y-%m-%d %H:%M'),
        "24 минут":(datetime.datetime.now() - timedelta(minutes=24)).strftime('%Y-%m-%d %H:%M'),
        "25 минут":(datetime.datetime.now() - timedelta(minutes=25)).strftime('%Y-%m-%d %H:%M'),
        "26 минут":(datetime.datetime.now() - timedelta(minutes=26)).strftime('%Y-%m-%d %H:%M'),
        "27 минут":(datetime.datetime.now() - timedelta(minutes=27)).strftime('%Y-%m-%d %H:%M'),
        "28 минут":(datetime.datetime.now() - timedelta(minutes=28)).strftime('%Y-%m-%d %H:%M'),
        "29 минут":(datetime.datetime.now() - timedelta(minutes=29)).strftime('%Y-%m-%d %H:%M'),
        "30 минут":(datetime.datetime.now() - timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M'),
        "31 минут":(datetime.datetime.now() - timedelta(minutes=31)).strftime('%Y-%m-%d %H:%M'),
        "32 минут":(datetime.datetime.now() - timedelta(minutes=32)).strftime('%Y-%m-%d %H:%M'),
        "33 минут":(datetime.datetime.now() - timedelta(minutes=33)).strftime('%Y-%m-%d %H:%M'),
        "34 минут":(datetime.datetime.now() - timedelta(minutes=34)).strftime('%Y-%m-%d %H:%M'),
        "35 минут":(datetime.datetime.now() - timedelta(minutes=35)).strftime('%Y-%m-%d %H:%M'),
        "36 минут":(datetime.datetime.now() - timedelta(minutes=36)).strftime('%Y-%m-%d %H:%M'),
        "37 минут":(datetime.datetime.now() - timedelta(minutes=37)).strftime('%Y-%m-%d %H:%M'),
        "38 минут":(datetime.datetime.now() - timedelta(minutes=38)).strftime('%Y-%m-%d %H:%M'),
        "39 минут":(datetime.datetime.now() - timedelta(minutes=39)).strftime('%Y-%m-%d %H:%M'),
        "40 минут":(datetime.datetime.now() - timedelta(minutes=40)).strftime('%Y-%m-%d %H:%M'),
        "41 минут":(datetime.datetime.now() - timedelta(minutes=41)).strftime('%Y-%m-%d %H:%M'),
        "42 минут":(datetime.datetime.now() - timedelta(minutes=42)).strftime('%Y-%m-%d %H:%M'),
        "43 минут":(datetime.datetime.now() - timedelta(minutes=43)).strftime('%Y-%m-%d %H:%M'),
        "44 минут":(datetime.datetime.now() - timedelta(minutes=44)).strftime('%Y-%m-%d %H:%M'),
        "45 минут":(datetime.datetime.now() - timedelta(minutes=45)).strftime('%Y-%m-%d %H:%M'),
        "46 минут":(datetime.datetime.now() - timedelta(minutes=46)).strftime('%Y-%m-%d %H:%M'),
        "47 минут":(datetime.datetime.now() - timedelta(minutes=47)).strftime('%Y-%m-%d %H:%M'),
        "48 минут":(datetime.datetime.now() - timedelta(minutes=48)).strftime('%Y-%m-%d %H:%M'),
        "49 минут":(datetime.datetime.now() - timedelta(minutes=49)).strftime('%Y-%m-%d %H:%M'),
        "50 минут":(datetime.datetime.now() - timedelta(minutes=50)).strftime('%Y-%m-%d %H:%M'),
        "51 минут":(datetime.datetime.now() - timedelta(minutes=51)).strftime('%Y-%m-%d %H:%M'),
        "52 минут":(datetime.datetime.now() - timedelta(minutes=52)).strftime('%Y-%m-%d %H:%M'),
        "53 минут":(datetime.datetime.now() - timedelta(minutes=53)).strftime('%Y-%m-%d %H:%M'),
        "54 минут":(datetime.datetime.now() - timedelta(minutes=54)).strftime('%Y-%m-%d %H:%M'),
        "55 минут":(datetime.datetime.now() - timedelta(minutes=55)).strftime('%Y-%m-%d %H:%M'),
        "56 минут":(datetime.datetime.now() - timedelta(minutes=56)).strftime('%Y-%m-%d %H:%M'),
        "57 минут":(datetime.datetime.now() - timedelta(minutes=57)).strftime('%Y-%m-%d %H:%M'),
        "58 минут":(datetime.datetime.now() - timedelta(minutes=58)).strftime('%Y-%m-%d %H:%M'),
        "59 минут":(datetime.datetime.now() - timedelta(minutes=59)).strftime('%Y-%m-%d %H:%M'),
    }