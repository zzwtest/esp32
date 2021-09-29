from machine import UART
import time   
uart = UART(2, baudrate=115200, rx=16,tx=17,timeout=10)  

def _AT(uart,cmd,timeout_ms=3000):
    cmd = cmd.encode() if isinstance(cmd,str) else cmd 
    cmd = cmd+b"\r"
    uart.write(cmd)
    res = ATLoop(timeout_ms)
    res = res.replace(cmd,b"")
    return res.strip(b"\r\n")




def AT(cmd,timeout_ms=3000):
    return _AT(uart,cmd,timeout_ms)


def ATLoop(timeout_ms=1000):
    ts = 0 
    sleepms=50
    res = b""
    while 1:
        time.sleep_ms(sleepms)
        ts+=sleepms
        if ts>=timeout_ms:
            break 
        s = uart.read()
        if s:
            res += s 
        if res.count(b"\r\n") >= 2 and not s and  res[-2:] == b"\r\n" :
            break 
    return res 
    




# #选择短消息服务:AT+CSMS 
# uart.write('AT+CSMS=1\r\n')
# print(uart.read())


# uart.write('AT+CSCS="PCCP936"\r\n')
# time.sleep_ms(1000)
# print(uart.read())


# uart.write('AT+CMGF=1\r\n')
# time.sleep_ms(1000)
# print(uart.read())

 

# import time 
# while 1:
#     s = uart.readline();time.sleep_ms(30)
# if s :print(s)

