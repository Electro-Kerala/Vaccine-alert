import requests
import json
from datetime import date,datetime,timedelta

todays_date=datetime.now()
Date=todays_date.strftime('%d-%m-%Y')

# district id 
#  301 for Alappuzha
#  304 for Kottayam
def printjson(district_ID,Date):

    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_ID}&date={Date}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    result = requests.get(url, headers=headers)
    new_result=result.json()
    print(new_result)

printjson(304,Date)