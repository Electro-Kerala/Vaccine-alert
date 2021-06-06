import requests
import numpy as np
import time 
from datetime import datetime,timedelta

index= 0
DB = np.array([])
DB = np.zeros((7,), dtype = np.ndarray)
abstrList = np.array([])
abstrList = np.zeros((7,), dtype = np.object_)
Mem_Sessions = np.array([])
Mem_Sessions = np.zeros((14,), dtype = np.int_) 
total_dos_aval = np.array([])
total_dos_aval = np.zeros((14,), dtype = np.int_) 
Message = f""


def sendTGMessage(message:str, chat_ID:str)->None:
    url = f'https://api.telegram.org/bot<Bot-ID>/sendMessage'
    msg_data = {'chat_id':chat_ID,'text':message,"parse_mode":"Markdown"}
    resp = requests.post(url, msg_data).json()
    print("Message Not Send" if resp['ok'] is False else "👉    Message  Sent")

'''
	This function sends the message to each district platforms, according to the total No. of centers or dose availability
'''
def setData(district_ID:int, WholeSessions:int, index:int, message:str, temp_dos_avl:int, chat_ID1:str)->None:
	global Mem_Sessions
	global total_dos_aval
	Dis_ID = [ 301, 307, 306, 297, 295, 298, 304, 305, 302, 308, 300, 296, 303, 299]
	if district_ID==Dis_ID[index]:
		if Mem_Sessions[index]!=WholeSessions or (total_dos_aval[index]!= temp_dos_avl):
			print("Updates Available") 
			sendTGMessage(message,chat_ID1)
			Mem_Sessions[index]=WholeSessions
			total_dos_aval[index] = temp_dos_avl
			print(message)

'''
	This function gives the updated message according to the No. of centers 
	Returns the total No. of centers
'''
def buildMessage(Week)->int:
	global DB # veriable from the function dataBase (list of m arrays )
	global abstrList
	global Message
	length=0
	for j in range(7):
		length=length+DB[j]
		if DB[j]!=0:
			message0=f"\n\n{Week[j].strftime('%d-%m-%Y')}\n\n{abstrList[j]}Number of centers available is {DB[j]}"
		else:
			message0=f"\n\n{Week[j].strftime('%d-%m-%Y')}\nNo updates available"
		Message = Message+ message0
	return length


def dataBase(x:int, abstr:str, num_of_centers:int)->None:
	'''
	This function records the number of centers with dose grater than 10 and abstr string per day
	'''
	
	global DB
	global abstrList
	if x<7:
		DB[x]=num_of_centers
		abstrList[x]=abstr


def getData(district_ID:int, District_Name:str, chat_ID1:str)->None:
	global index
	global Message
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
		print("day",x)
		time.sleep(4)
		Date=Week[x].strftime('%d-%m-%Y')
		url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_ID}&date={Date}'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
		result = requests.get(url, headers=headers)
		new_result=result.json()
		num=len(new_result['sessions'])
		modifiedlist = []
		abstr =''
		aval_dose_num = 0 # Is use to save number of slotes with availabe doses
		for i in range(num):
			temp_dos_avl+=new_result['sessions'][i]['available_capacity']
			# print(new_result['sessions'][i]['available_capacity'])
			if new_result['sessions'][i]['available_capacity'] > 10:
				aval_dose_num += 1
				modifiedlist.append(aval_dose_num)
				modifiedlist.append(".")
				modifiedlist.append(" ")
				modifiedlist.append(new_result['sessions'][i]['name'])
				modifiedlist.append(" - Doses = ")
				modifiedlist.append(new_result['sessions'][i]['available_capacity'])
				modifiedlist.append("\n")
				print(modifiedlist)
				
		for y in modifiedlist:
			abstr+= str(y)
		print(aval_dose_num)
		marray =np.array(modifiedlist)
		marray =marray.reshape(aval_dose_num,7)
		dataBase(x, abstr, aval_dose_num)
		total+=temp_dos_avl

	WholeSessions=buildMessage(Week)
	message =f"\nUpdate on  {District_Name} district {Message} \n\nTotal centers from {Week[0].strftime('%d-%m-%Y')} to {Week[6].strftime('%d-%m-%Y')} is {WholeSessions} \n\n\nIt'll take some time to reflect the changes in Cowin portal. If the doses is a number it is availabe right now, doses is 0 refresh the page and try again it'll take upto 30 minutes.\nAlert from Server 3: Please verify the details with https://cowin.gov.in and book Covid-19 vaccine from there. For more info visit https://vaccine-alert.github.io \nGreetings from Electro Kerala, The hardware community"
	print(message)
	setData(district_ID, WholeSessions, index, message, total, chat_ID1)
	Message = f""
	index+=1

#getData(<district code>,"district name","chat_id")-1001339973178
		
def loop():
	global index
	index=0
	try:
		'''
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
		'''
		getData(301,"Alappuzha","-1001339973178")
		time.sleep(16)
		getData(307,"Ernakulam","-1001339973178")
		time.sleep(16)
		getData(306,"Idukki","-1001339973178")
		time.sleep(16)
		getData(297,"Kannur","-1001339973178")
		time.sleep(16)
		getData(295,"Kasaragod","-1001339973178")
		time.sleep(16)
		getData(298,"Kollam","-1001339973178")
		time.sleep(16)
		getData(304,"Kottayam","-1001339973178")
		time.sleep(16)
		getData(305,"Kozhikode","-1001339973178")
		time.sleep(16)
		getData(302,"Malappuram","-1001339973178")
		time.sleep(16)
		getData(308,"Palakkad","-1001339973178")
		time.sleep(16)
		getData(300,"Pathanamthitta","-1001339973178")
		time.sleep(16)
		getData(296,"Thiruvananthapuram","-1001339973178")
		time.sleep(16)
		getData(303,"Thrissur","-1001339973178")
		time.sleep(16)
		getData(299,"Wayanad","-1001339973178")
		#sendTGMessage("Function is running","-1001339973178")
		loop()

	except:
		time.sleep(32)
		print("some thing went wrong")
		#sendTGMessage("Something went wrong","-1001339973178")
		loop()


loop()
