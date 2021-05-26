import requests
import json
import numpy as np
import time
from datetime import date,datetime,timedelta
ct=0
Mem_Sessions0=0
Mem_Sessions1=0
Mem_Sessions2=0
Mem_Sessions3=0
Mem_Sessions4=0
Mem_Sessions5=0
Mem_Sessions6=0
Mem_Sessions7=0
Mem_Sessions8=0
Mem_Sessions9=0
Mem_Sessions10=0
Mem_Sessions11=0
Mem_Sessions12=0
Mem_Sessions13=0

DB0=np.array([])
DB1=np.array([])
DB2=np.array([])
DB3=np.array([])
DB4=np.array([])
DB5=np.array([])
DB6=np.array([])
data1=0

dataB1=np.array([])
data1 = 0
abstr=''
abstr0=''
abstr1=''
abstr2=''
abstr3=''
abstr4=''
abstr5=''
abstr6=''

def sendTGMessage(message:str, chat_ID:str)->None:
    url = f'https://api.telegram.org/bot<bot_ID>/sendMessage'
    msg_data = {'chat_id':chat_ID,'text':message,"parse_mode":"Markdown"}
    resp = requests.post(url, msg_data).json()
    print("Message Not Send" if resp['ok'] is False else "👉    Message  Sent")
def GetData(district_ID,District_Name,chat_ID1):
	global dataB1
	global data1
	global DB0
	global DB1
	global DB2
	global DB3
	global DB4
	global DB5
	global DB6
	global Mem_Sessions0
	global Mem_Sessions1
	global Mem_Sessions2
	global Mem_Sessions3
	global Mem_Sessions4
	global Mem_Sessions5
	global Mem_Sessions6
	global Mem_Sessions7
	global Mem_Sessions8
	global Mem_Sessions9
	global Mem_Sessions10
	global Mem_Sessions11
	global Mem_Sessions12
	global Mem_Sessions13
	global abstr
	global abstr0
	global abstr1
	global abstr2
	global abstr3
	global abstr4
	global abstr5
	global abstr6
	day0=datetime.now()
	day1=day0+timedelta(1)
	day2=day0+timedelta(2)
	day3=day0+timedelta(3)
	day4=day0+timedelta(4)
	day5=day0+timedelta(5)
	day6=day0+timedelta(6)
	Week=np.array([day0,day1,day2,day3,day4,day5,day6])


	for x in range(7):
		time.sleep(4)
		Date=Week[x].strftime('%d-%m-%Y')
		url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_ID}&date={Date}'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
		result = requests.get(url, headers=headers)
		new_result=result.json()
		num=len(new_result['sessions'])
		num1=num
		modifiedlist = []
		for i in range(num):
			modifiedlist.append(i+1)
			modifiedlist.append(".")
			modifiedlist.append(" ")
			modifiedlist.append(new_result['sessions'][i]['name'])
			modifiedlist.append(" - Doses = ")

			modifiedlist.append(new_result['sessions'][i]['available_capacity'])
			modifiedlist.append("\n")
#			#modifiedlist.append(new_result['sessions'][i]['fee_type'])
#			#modifiedlist.append("Vaccine: ")
#			#modifiedlist.append(new_result['sessions'][i]['vaccine'])
#			#modifiedlist.append(",")
		for y in modifiedlist:
			abstr+= str(y)
		#print(abstr)
		marray =np. array(modifiedlist)
		marray =marray.reshape(num,7)
		if x==0:
			DB0=marray
			abstr0=abstr
		if x==1:
			DB1=marray
			abstr1=abstr
		if x==2:
			DB2=marray
			abstr2=abstr
		if x==3:
			DB3=marray
			abstr3=abstr
		if x==4:
			DB4=marray
			abstr4=abstr
		if x==5:
			DB5=marray
			abstr5=abstr
		if x==6:
			DB6=marray
			abstr6=abstr
		abstr=''
	if len(DB0)!=0:
		message0=f"\n\n{Week[0].strftime('%d-%m-%Y')}\n\n{abstr0}Number of centers available is {len(DB0)}"
	else:
		message0=f"\n\n{Week[0].strftime('%d-%m-%Y')}\nNo centers available"
	if len(DB1)!=0:
		message1=f"\n\n{Week[1].strftime('%d-%m-%Y')}\n\n{abstr1}Number of centers available is {len(DB1)}"
	else:
		message1=f"\n\n{Week[1].strftime('%d-%m-%Y')}\nNo centers available"
	if len(DB2)!=0:
		message2=f"\n\n{Week[2].strftime('%d-%m-%Y')}\n\n{abstr2}Number of centers available is {len(DB2)}"
	else:
		message2=f"\n\n{Week[2].strftime('%d-%m-%Y')}\nNo centers available"
	if len(DB3)!=0:
		message3=f"\n\n{Week[3].strftime('%d-%m-%Y')}\n\n{abstr3}Number of centers available is {len(DB3)}"
	else:
		message3=f"\n\n{Week[3].strftime('%d-%m-%Y')}\nNo centers available"
	if len(DB4)!=0:
		message4=f"\n\n{Week[4].strftime('%d-%m-%Y')}\n\n{abstr4}Number of centers available is {len(DB4)}"
	else:
		message4=f"\n\n{Week[4].strftime('%d-%m-%Y')}\nNo centers available"
	if len(DB5)!=0:
		message5=f"\n\n{Week[5].strftime('%d-%m-%Y')}\n\n{abstr5}Number of centers available is {len(DB5)}"
	else:
		message5=f"\n\n{Week[5].strftime('%d-%m-%Y')}\nNo centers available"
	if len(DB6)!=0:
		message6=f"\n\n{Week[6].strftime('%d-%m-%Y')}\n\n{abstr6}Number of centers available is {len(DB6)}"
	else:
		message6=f"\n\n{Week[6].strftime('%d-%m-%Y')}\nNo centers available"
	WholeSessions=len(DB0)+len(DB1)+len(DB2)+len(DB3)+len(DB4)+len(DB5)+len(DB6)

	message =f"\nUpdate on {District_Name} district {message0}{message1}{message2}{message3}{message4}{message5}{message6} \n\nTotal centers from {Week[0].strftime('%d-%m-%Y')} to {Week[6].strftime('%d-%m-%Y')} is {WholeSessions} \n\n\nIt'll take some time to reflect the changes in Cowin portal. If the doses is a number it is availabe right now, doses is 0 refresh the page and try again it'll take upto 30 minutes.\nAleart from Server 3. Please verify the details with https://cowin.gov.in and book Cowid-19 vaccine from there. For more info visit https://vaccine-alert.github.io \nGreetings from Electro Kerala, The hardware community"
	#print(message)


	if district_ID==301:
		Temp_Sessions0=WholeSessions
		if Mem_Sessions0!=Temp_Sessions0:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions0=Temp_Sessions0
			print(message)

	if district_ID==307:
		Temp_Sessions1=WholeSessions
		if Mem_Sessions1!=Temp_Sessions1:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions1=Temp_Sessions1
	if district_ID==306:
		Temp_Sessions2=WholeSessions
		if Mem_Sessions2!=Temp_Sessions2:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions2=Temp_Sessions2
	if district_ID==297:
		Temp_Sessions3=WholeSessions
		if Mem_Sessions3!=Temp_Sessions3:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions3=Temp_Sessions3

	if district_ID==295:
		Temp_Sessions4=WholeSessions
		if Mem_Sessions4!=Temp_Sessions4:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions4=Temp_Sessions4

	if district_ID==298:
		Temp_Sessions5=WholeSessions
		if Mem_Sessions5!=Temp_Sessions5:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions5=Temp_Sessions5

	if district_ID==304:
		Temp_Sessions6=WholeSessions
		if Mem_Sessions6!=Temp_Sessions6:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions6=Temp_Sessions6

	if district_ID==305:
		Temp_Sessions7=WholeSessions
		if Mem_Sessions7!=Temp_Sessions7:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions7=Temp_Sessions7

	if district_ID==302:
		Temp_Sessions8=WholeSessions
		if Mem_Sessions8!=Temp_Sessions8:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions8=Temp_Sessions8

	if district_ID==308:
		Temp_Sessions9=WholeSessions
		if Mem_Sessions9!=Temp_Sessions9:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions9=Temp_Sessions9

	if district_ID==300:
		Temp_Sessions10=WholeSessions
		if Mem_Sessions10!=Temp_Sessions10:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions10=Temp_Sessions10


	if district_ID==296:
		Temp_Sessions11=WholeSessions
		if Mem_Sessions11!=Temp_Sessions11:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions11=Temp_Sessions11

	if district_ID==303:
		Temp_Sessions12=WholeSessions
		if Mem_Sessions12!=Temp_Sessions12:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions12=Temp_Sessions12

	if district_ID==299:
		Temp_Sessions13=WholeSessions
		if Mem_Sessions13!=Temp_Sessions13:
			print("Update Available")
			sendTGMessage(message,chat_ID1)
			Mem_Sessions13=Temp_Sessions13

	

#GetData(<district code>,"district name","chat_id")-1001339973178

		
def loop():
	try:
	 
		GetData(301,"Alappuzha","@alappuzha_vaccine_alert")
		time.sleep(16)
		GetData(307,"Ernakulam","@ernakulam_vaccine_alert")
		time.sleep(16)
		GetData(306,"Idukki","@idukki_vaccine_alert")
		time.sleep(16)
		GetData(297,"Kannur","@kannur_vaccine_alert")
		time.sleep(16)
		GetData(295,"Kasaragod","@kasaragod_vaccine_alert")
		time.sleep(16)
		GetData(298,"Kollam","@kollam_vaccine_alert")
		time.sleep(16)
		GetData(304,"Kottayam","@kottayam_vaccine_alert")
		time.sleep(16)
		GetData(305,"Kozhikode","@kozhikode_vaccine_alert")
		time.sleep(16)
		GetData(302,"Malappuram","@malappuram_vaccine_alert")
		time.sleep(16)
		GetData(308,"Palakkad","@palakkad_vaccine_alert")
		time.sleep(16)
		GetData(300,"Pathanamthitta","@pathanamthitta_vaccine_alert")
		time.sleep(16)
		GetData(296,"Thiruvananthapuram","@thiruvananthapuram_vaccine_alert")
		time.sleep(16)
		GetData(303,"Thrissur","@thrissur_vaccine_alert")
		time.sleep(16)
		GetData(299,"Wayanad","@wayanad_vaccine_alert")
		sendTGMessage("Function is running","-1001339973178")
		loop()
	
	
	except:
		time.sleep(32)
		sendTGMessage("Something went wrong","-1001339973178")
		loop()

		

loop()
