
buffer = "" 
recvdata = {} 

function uart_on(data)
    print("receive from uart:" ,string.byte(data),data)
    buffer = buffer .. data 
    if  string.find( buffer , "zzwquit")   then
      uart.on("data") -- unregister callback function
    end

    s,e = string.find(buffer , "\r\n")
    if s  then
        local  str = string.sub(buffer,0,s) 
        if string.find(str,"zzw:") then
            at = string.sub(str,5) 
            uart.write(1,at.."\r\n")
            --uart.write(1,"AT+CSCS=PCCP936\r\n") 
        else 
            print("recv:" , s,e,string.len(str),str ) 
        end 
        
        
            
        buffer = string.sub(buffer,e+1)
        --print("last:" , buffer)
    end 
end

--uart_on("abc")

uart.on("data","\n",uart_on, 0)
 