import machine
import time 
import esp32 
import network
import urequests
import ujson 
import sys 




#print(u"呃".encode("utf8"))
t = u"\u%s" % "5A00"

print([t])
print(t.encode("utf8"))

sys.exit(0)

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
wiflist=  sta_if.scan()                             # Scan for available access points 

home = 0 
office = 0 
for w in wiflist:
    if b"ssmax" in w :
        office  = 1 
        break 
    if b"zzwxiaomi" in w :
        home = 1 
        break 
if office :
    ssid = "ssmax"
    passwd= "NTES4ever#23"
elif home:
    ssid= "zzwxiaomi"
    passwd= "163163!!"
else:
    ssid= ""
    passwd= ""
if ssid :
    sta_if.connect(ssid, passwd) # Connect to an AP


while 1 :
    if sta_if.isconnected():
        break 
    time.sleep_ms(2000)
    print("%s connected to AP .. %s  status:%s" % (time.time(),ssid,sta_if.status()))


print("connected ok")

#pin12 = machine.Pin(18, machine.Pin.OUT,machine.Pin.PULL_DOWN)


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

print(myphone.AT("AT+CSCS=PCCP936"))
print(myphone.AT("AT+CMGF=1"))
print(myphone.AT("AT&W"))


while 1:
    res = myphone.ATLoop()
    #print(res)
    if res and b"MESSAGE" in res:
        data = {}
        data["msg"] = res 
        print(ujson.dumps(data))
    
#  
#myphone.AT("AT+RESET")




#import time 
#while 1 :
#    time.sleep_ms(300)
#    print(pin12.value())


#pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
#print(pin13.value())