# blink
A visual flashing indicator connected to ticketing or other systems. 

Inspiration for this project came from noticing the difficulty in effectively utilizing TVs in SOCs. 
More on that [here](https://sashasec.medium.com/soc-dashboard-destroyer-a-29-99-flash-drive-using-tlp-3f05041e8211). TLDR: use a Blink1 instead. 

For only $29.99 you can buy a ThingM Blink(1) LED USB -> [here](https://www.amazon.com/ThingM-Blink-USB-RGB-BLINK1MK3/dp/B07Q8944QK/ref=sr_1_1?crid=2E6PMKXCOAL10&dchild=1&keywords=thingm+blink&qid=1624758572&sprefix=thingm%2Caps%2C293&sr=8-1)

This was written with the Traffic Light Protocol in mind ([TLP](https://www.cisa.gov/tlp)) but you can use colors that work for you by looking up their [RBG](https://www.w3schools.com/colors/colors_picker.asp) values.

requirements: 
`sudo apt install -y python3 python3-pip`
`pip install Blink1`
`pip install requests`

Usage: 

    python test.py
    
    # Once connected with your given ticketing system, run: 
    python3 blink.py 


Testing colors manually in python interactive shell: 

    import time
    from blink1.blink1 import Blink1
        
    blink1 = Blink1()
        
    blink1.fade_to_rgb(1000, 51, 255, 0, 0) #green

    blink1.fade_to_rgb(1000, 255, 255, 255, 0) #white 

    blink1.fade_to_rgb(1000, 255, 192, 0, 0) #amber

    blink1.fade_to_rgb(1000, 255, 0, 0, 0) #red
        
