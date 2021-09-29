import machine
import time 
import esp32 
#pin12 = machine.Pin(34, machine.Pin.IN)#,machine.Pin.PULL_DOWN)
import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)

sta_if.connect("zzwxiaomi", "163163!!") # Connect to an AP



pin12 = machine.Pin(18, machine.Pin.OUT,machine.Pin.PULL_DOWN)


#esp32.wake_on_ext0(pin = pin12, level = esp32.WAKEUP_ANY_HIGH)
#machine.lightsleep()

#machine.deepsleep()

# n = 0 
# while 1:
#     if sta_if.isconnected() :
#         pin12.value(1)
#     else:
#         #pin12.value(0)
#         pin12.value(n);n = abs(n-1) ;time.sleep_ms(100)

import myphone 

myphone.AT("AT+CSCS=PCCP936")
myphone.AT("AT+CMGF=1")
myphone.AT("AT&W")

while 1:
    print(myphone.ATLoop())
#  
#myphone.AT("AT+RESET")




#import time 
#while 1 :
#    time.sleep_ms(300)
#    print(pin12.value())


#pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
#print(pin13.value())