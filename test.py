import time
from blink1.blink1 import Blink1
    
blink1 = Blink1()
blink1.fade_to_rgb(1000, 0, 128, 0, 0) #green
time.sleep(3)
blink1.fade_to_rgb(1000, 255, 255, 102, 0) #yellow
time.sleep(3)
blink1.fade_to_rgb(1000, 255, 0, 0, 0) #red
