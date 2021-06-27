# Blink - a visual indicator connected to ticketing or other systems. 
# Each ticketing system will likely behave differently - but each will have the capability of performing a query by hitting their API/Site.
# Works best with: https://www.amazon.com/ThingM-Blink-USB-RGB-BLINK1MK3/dp/B07Q8944QK/ref=sr_1_1?crid=2E6PMKXCOAL10&dchild=1&keywords=thingm+blink&qid=1624758572&sprefix=thingm%2Caps%2C293&sr=8-1
# Find you preferred colors RGB values here: https://www.w3schools.com/colors/colors_picker.asp 

# requirements: 
# pip install Blink1
# pip install requests

from __future__ import print_function                                         
from datetime import datetime                                                  
from pprint import pprint    
from blink1.blink1 import Blink1
import requests, re, json, base64, time, code            
requests.packages.urllib3.disable_warnings()                                   
                                                                               
def login():
    url = "https://your_ticketing_system.com:443/api/v1/login/"
    headers = {"Content-Type":"application/json", 'User-Agent':'blink1'}
    body = """{"user_name":"service-account", "password":"secret-password"}""" 
    response = requests.post(url, headers=headers, data=body)
    if 'json' in dir(response): 
        json_response = response.json()
        if 'set-cookie' in response.headers.keys():
            cookie = response.headers['set-cookie'][11:]
        else: 
            cookie = "failed"
    else: 
        cookie = "failed"
    # User account data here
    #print(json_response['user'])
    return cookie 

def get_ticket_list(cookies):
    global user, pwd
    try:
        url = 'https://your_ticketing_system.com/api/v1/sr?query=%5BSECURITY%20TICKET%5D&status=1,2,4,5,6,40,41,46'
        headers = {"Content-Type":"application/json", "User-Agent":"blink1"}
        response = requests.get(url, headers=headers, cookies=cookies)
        json_response = response.json()
    except: 
        print(str(datetime.now()) + "Ticketing query failed")
        json_response =  "failed"
        pass
    
    return json_response 

def clean_json(response):
    ticket_list = []
    for j in response:
        my_dict = {}
        for i in j['info']:
            # key, value, keyCaption, valueCaption
            if i['key'] == 'alertID':
                my_dict.update({i['key']:i['value']})
            else:
                my_dict.update({i['key']:i['valueCaption']})
        ticket_list.append(my_dict)
    return ticket_list



def main():
    print("                        ")
    print("  _     _ _       _     ")
    print(" | |   | (_)     | |    ")
    print(" | |__ | |_ _ __ | | __ ")
    print(" | '_ \| | | '_ \| |/ / ")
    print(" | |_) | | | | | |   <  ")
    print(" |_.__/|_|_|_| |_|_|\_\ ")
    print("                        ")
                                      
    try:
        blink1 = Blink1()
        blink1.fade_to_rgb(10, 128, 128, 128, 0) #gray
        time.sleep(2)
    except:
        print(str(datetime.now()) + " no blink1 found")
        sys.exit()

    try:
		cookie = login()
        while True:
			ticket = get_ticket_list({"JSESSIONID":cookie})

            if ticket == "failed":
                blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                time.sleep(1)
                blink1.fade_to_rgb(10, 128, 128, 128, 0) #gray
                time.sleep(1)
            else: 
                ticket_list = clean_json(ticket) 

                if not len(ticket_list):
                    print(str(datetime.now()) + " No active tickets")
                    countdown = 0
                    blink1.fade_to_rgb(1000, 0, 128, 0, 0) #green 
                    
                else:
                    for ticket in ticket_list:
                        if len(ticket['responsibility']) == 0:
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            blink1.fade_to_rgb(10, 255, 0, 0, 0) #red
                            time.sleep(0.6)
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            unseen_exists = True
                        elif ticket['responsibility'] == "Team Member1": 
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            blink1.fade_to_rgb(1000, 255, 0, 0, 1) #red
                            blink1.fade_to_rgb(1000, 0, 0, 255, 2) #blue
                            time.sleep(0.6)
                        elif ticket['responsibility'] == "Team Member2":
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            blink1.fade_to_rgb(1000, 255, 204, 229, 1) #dark purple
                            blink1.fade_to_rgb(1000, 255, 128, 0, 2) #dark orange
                            time.sleep(0.6)
                        elif ticket['responsibility'] == "Team Member3": 
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            blink1.fade_to_rgb(1000, 179, 179, 77, 1) #gray yellow
                            blink1.fade_to_rgb(1000, 235, 153, 71, 2) #orange
                            time.sleep(0.6)
                        elif ticket['responsibility'] == "Team Member4":
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            blink1.fade_to_rgb(1000, 153, 51, 0, 1) #ice blue
                            blink1.fade_to_rgb(1000, 51, 153, 0, 2) #light purple 
                            time.sleep(0.6)
                        else: 
                            blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                            time.sleep(0.2)
                            blink1.fade_to_rgb(1000, 255, 255, 255, 1) #white
                            blink1.fade_to_rgb(1000, 0, 0, 255, 2) #blue
                            time.sleep(0.6)
							
                    if countdown < (notices_per_hour/4):
                        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                        time.sleep(1) 
                        blink1.fade_to_rgb(1000, 255, 255, 0, 0) #amber
                    elif countdown <= (notices_per_hour/2):
                        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                        time.sleep(1) 
                        blink1.fade_to_rgb(1000, 255, 255, 0, 1) #amber 
                        blink1.fade_to_rgb(1000, 255, 0, 0, 2) # red
                    elif countdown <= ((notices_per_hour/4)*3):
                        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                        time.sleep(1) 
                        blink1.fade_to_rgb(1000, 255, 153, 0, 1) # orange
                        blink1.fade_to_rgb(1000, 255, 0, 0, 2) # red
                    elif countdown <= notices_per_hour:
                        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                        time.sleep(1) 
                        blink1.fade_to_rgb(1000, 255, 0, 0, 1) #red
                        blink1.fade_to_rgb(1000, 0, 0, 0, 2) # black
                    elif countdown > notices_per_hour:
                        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
                        time.sleep(1) 
                        blink1.fade_to_rgb(1000, 255, 0, 0, 0) #red

                    print(str(datetime.now()) + " " + str(len(ticket_list)) + " open tickets found. Notice number: " + str(countdown))

                time.sleep(interval)
                    
    except KeyboardInterrupt:
        print()
        print(str(datetime.now()) + " Goodbye")
        blink1.fade_to_rgb(1000, 128, 128, 128, 0) #gray 
        time.sleep(2)
        blink1.close()

if __name__ == "__main__":
    main()
