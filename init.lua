
buffer = "" 
recvdata = {} 

function uart_on(data)
    --print("receive from uart:" ,string.byte(data),buffer)
    buffer = buffer .. data 
    if  string.find( buffer , "zzwquit")   then
      uart.on("data") -- unregister callback function
    end

    s,e = string.find(buffer , "\r\n")
    if s  then
        local  str = string.sub(buffer,0,s) 
        print("recv:" , s,e,string.len(str),str )
            
        buffer = string.sub(buffer,e+1)
        print("last:" , buffer)
    end 
end

--uart_on("abc")

uart.on("data",0,uart_on, 0)
 