# blink
A visual flashing indicator connected to ticketing or other systems. 

For only $29.99 you can buy a ThingM Blink(1) LED USB -> [here](https://www.amazon.com/ThingM-Blink-USB-RGB-BLINK1MK3/dp/B07Q8944QK/ref=sr_1_1?crid=2E6PMKXCOAL10&dchild=1&keywords=thingm+blink&qid=1624758572&sprefix=thingm%2Caps%2C293&sr=8-1)

This was written with the Traffic Light Protocol in mind ([TLP](https://www.cisa.gov/tlp)) but you can find colors that work for you by looking up their [RBG](https://www.w3schools.com/colors/colors_picker.asp) values.

requirements: 
`sudo apt install -y python3 python3-pip`
`pip install Blink1`
`pip install requests`

Usage: 

    python3 blink.py 

