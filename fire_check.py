import machine
import time 
import esp32 
#pin12 = machine.Pin(34, machine.Pin.IN)#,machine.Pin.PULL_DOWN)
import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("zzwxiaomi", "163163!!") # Connect to an AP
LED_GPIO = 18 
LED_FIRE_CHECK=34
#常亮
LED_TYPE_OPEN = 1 

#常灭
LED_TYPE_CLOSE = 0 

#慢速闪烁 
LED_TYPE_SLOW = 2 

LED_TYPE_SLOW_SLOW = 3

#快速闪烁
LED_TYPE_FAST = 4



LAST_LED_TICK = time.ticks_ms() 
LAST_LED = 0 



machine.freq(80000000)
led_pin  = machine.Pin(LED_GPIO, machine.Pin.OUT,machine.Pin.PULL_DOWN)
fire_pin = machine.Pin(LED_FIRE_CHECK, machine.Pin.IN,machine.Pin.PULL_DOWN)

def flush_led(pin,ledtype):
    global LAST_LED
    global LAST_LED_TICK
    if ledtype == LED_TYPE_OPEN:
        LAST_LED = 1 
        LAST_LED_TICK = time.ticks_ms() 
    elif ledtype == LED_TYPE_CLOSE:
        LAST_LED = 0 
        LAST_LED_TICK = time.ticks_ms() 
    elif ledtype == LED_TYPE_SLOW:
        if time.ticks_ms() - LAST_LED_TICK > 300:
            LAST_LED = int(not LAST_LED)
            LAST_LED_TICK = time.ticks_ms()
    elif ledtype == LED_TYPE_SLOW_SLOW:
        if time.ticks_ms() - LAST_LED_TICK > 1000:
            LAST_LED = int(not LAST_LED)
            LAST_LED_TICK = time.ticks_ms()
    elif ledtype == LED_TYPE_FAST:
        if time.ticks_ms() - LAST_LED_TICK > 50:
            LAST_LED = int(not LAST_LED)
            LAST_LED_TICK = time.ticks_ms()
    
    pin.value(LAST_LED) 


num = 1 
while 1:
    time.sleep_ms(30)
    num += 1
    fire = fire_pin.value()
    if fire == 1 :
        flush_led(led_pin,LED_TYPE_FAST) 
        continue

    if sta_if.isconnected():
        flush_led(led_pin,LED_TYPE_SLOW_SLOW)
    else:
        flush_led(led_pin,LED_TYPE_FAST)
    

    #flush_led(led_pin,LED_TYPE_SLOW_SLOW)



#def flush_led():
#    global led_pin
#    led_pin.value(1)


#flush_led() 