import requests
import json
import numpy as np
import time 
from datetime import date,datetime,timedelta

index= 0
DB=np.array([])
dataB1=np.array([])
abstrList=np.array([])
Mem_Sessions=np.array([])
total_dos_aval =np.array([])
Message = f""


def sendTGMessage(message:str, chat_ID:str)->None:
    url = f'https://api.telegram.org/bot<bot_ID>/sendMessage'
    msg_data = {'chat_id':chat_ID,'text':message,"parse_mode":"Markdown"}
    resp = requests.post(url, msg_data).json()
    print("Message Not Send" if resp['ok'] is False else "👉    Message  Sent")

'''
	This function sends the message to each district platforms, according to the total No. of centers or dose availability
	array=np.insert(where,index,value)
'''
def setData(district_ID:int, WholeSessions:int, index:int, message:str, temp_dos_avl:int, chat_ID1:str)->None:
	global Mem_Sessions
	global total_dos_aval
	Dis_ID = [ 301, 307, 306, 297, 295, 298, 304, 305, 302, 308, 300, 296, 303, 299]
	if district_ID==Dis_ID[index]:
		if Mem_Sessions!=WholeSessions or (total_dos_aval[index]!= temp_dos_avl):
			print("Updates Available") 
			#sendTGMessage(message,chat_ID1)
			Mem_Sessions=np.insert(Mem_Sessions,index,WholeSessions)
			total_dos_aval = np.insert(total_dos_aval,index,temp_dos_avl)
			print(message)

'''
	This function gives the updated message according to the No. of centers 
	Returns the total No. of centers
'''
def buildMessage(Week)->int:
	global DB
	global abstrList
	global Message
	length=0
	for j in range(7):
		length=length+len(DB[j])
		if len(DB)!=0:
			message0=f"\n\n{Week[j].strftime('%d-%m-%Y')}\n\n{abstrList[j]}Number of centers available is {len(DB[j])}"
		else:
			message0=f"\n\n{Week[j].strftime('%d-%m-%Y')}\nNo updates available"
		Message = Message+ message0
	return length

<<<<<<< HEAD

=======
'''
	This function records the marray and abstr string per day
	array=np.insert(where,index,value)
'''
>>>>>>> 479c9231c0e3549e37fe19cf3bc4b534ee2a123e
def dataBase(x:int, abstr:str, marray)->None:
	global DB
	global abstrList
	if x<7:
		DB=np.insert(DB,x,marray)
		abstrList=np.insert(abstrList,x,abstr)

def getData(district_ID:int, District_Name:str, chat_ID1:str)->None:
	global dataB1
	global index
	global Message
	abstr =''
	temp_dos_avl = total = 0
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
		modifiedlist = []
		for i in range(num):
			temp_dos_avl+=new_result['sessions'][i]['available_capacity']
			#print(new_result['sessions'][i]['available_capacity'])
			if new_result['sessions'][i]['available_capacity'] >= 10:
				modifiedlist.append(i+1)
				modifiedlist.append(".")
				modifiedlist.append(" ")
				modifiedlist.append(new_result['sessions'][i]['name'])
				modifiedlist.append(" - Doses = ")
				modifiedlist.append(new_result['sessions'][i]['available_capacity'])
				modifiedlist.append("\n")
		for y in modifiedlist:
			abstr+= str(y)
			# print(abstr)
		marray =np.array(modifiedlist)
		marray =marray.reshape(num,7)
		dataBase(x, abstr, marray)
		total+=temp_dos_avl

	WholeSessions=buildMessage(Week)
	message =f"\nUpdate on {District_Name} district {Message} \n\nTotal centers from {Week[0].strftime('%d-%m-%Y')} to {Week[6].strftime('%d-%m-%Y')} is {WholeSessions} \n\n\nIt'll take some time to reflect the changes in Cowin portal. If the doses is a number it is availabe right now, doses is 0 refresh the page and try again it'll take upto 30 minutes.\nAleart from Server 3. Please verify the details with https://cowin.gov.in and book Cowid-19 vaccine from there. For more info visit https://vaccine-alert.github.io \nGreetings from Electro Kerala, The hardware community"
	#print(message)
	setData(district_ID, WholeSessions, index, message, total, chat_ID1)
	index+=1

#getData(<district code>,"district name","chat_id")-1001339973178
		
def loop():
	global index
	index=0
	try:
		getData(301,"Alappuzha","@alappuzha_vaccine_alert")
		time.sleep(16)
		getData(307,"Ernakulam","@ernakulam_vaccine_alert")
		time.sleep(16)
		getData(306,"Idukki","@idukki_vaccine_alert")
		time.sleep(16)
		getData(297,"Kannur","@kannur_vaccine_alert")
		time.sleep(16)
		getData(295,"Kasaragod","@kasaragod_vaccine_alert")
		time.sleep(16)
		getData(298,"Kollam","@kollam_vaccine_alert")
		time.sleep(16)
		getData(304,"Kottayam","@kottayam_vaccine_alert")
		time.sleep(16)
		getData(305,"Kozhikode","@kozhikode_vaccine_alert")
		time.sleep(16)
		getData(302,"Malappuram","@malappuram_vaccine_alert")
		time.sleep(16)
		getData(308,"Palakkad","@palakkad_vaccine_alert")
		time.sleep(16)
		getData(300,"Pathanamthitta","@pathanamthitta_vaccine_alert")
		time.sleep(16)
		getData(296,"Thiruvananthapuram","@thiruvananthapuram_vaccine_alert")
		time.sleep(16)
		getData(303,"Thrissur","@thrissur_vaccine_alert")
		time.sleep(16)
		getData(299,"Wayanad","@wayanad_vaccine_alert")
		#sendTGMessage("Function is running","-1001339973178")
		loop()
		
	except:
		time.sleep(32)
		#sendTGMessage("Something went wrong","-1001339973178")
		loop()

loop()
