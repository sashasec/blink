import time
from blink1.blink1 import Blink1
    
blink1 = Blink1()
print("Testing TLP concept with Blink1")

print("Logging in to system xyx. \n\nReturning tickets . . .\n") 

tickets = ['red', 'red', 'red', 'amber', 'white', 'white']
print(tickets)

for ticket in tickets: 
    if ticket == 'red': 
        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
        time.sleep(0.2)
        blink1.fade_to_rgb(1000, 255, 0, 0, 0) #red
        time.sleep(1)
    elif ticket == 'amber': 
        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
        time.sleep(0.2)
        blink1.fade_to_rgb(1000, 255, 192, 0, 0) #amber
        time.sleep(1)
    elif ticket == 'white': 
        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
        time.sleep(0.2)
        blink1.fade_to_rgb(1000, 255, 255, 255, 0) #white
        time.sleep(1)
    else: 
        blink1.fade_to_rgb(10, 0, 0, 0, 0) #black
        time.sleep(0.2)
        blink1.fade_to_rgb(1000, 51, 255, 0, 0) #green
        time.sleep(1)
        
print("\nNow all issues are resolved. On the next check, the Blink1 will be changed to green.")
blink1.fade_to_rgb(1000, 51, 255, 0, 0) #green
time.sleep(1)
