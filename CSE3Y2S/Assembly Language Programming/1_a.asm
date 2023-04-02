.MODEL SMALL
.STACK 100H
.DATA

    input db 10,13,'Enter a number (1-3) : $' 
    result_msg db 10,13,'Summation : $' 
    
    sum db 48
    ;sum db '0'
    
    
.CODE


MAIN PROC
     
     mov ax,@data
     mov ds,ax
     
     
    
     mov ah,9 
     lea dx,input
     int 21h 
     
     
     ;take input
     mov ah,1
     int 21h
     
     ;if at first enter 0 then
     cmp al,'0';'0'==48
     je result 
     
     ;summation n+(n-1)+...1  
     loop_:
     add sum,al
     sub sum,48
     sub al,1  
     cmp al,48
     jnz loop_  
                 
                 
     ;print result
      
     result:
     lea dx,result_msg
     mov ah,9
     int 21h
     
     
     mov ah,2 
     mov dl,sum
     int 21h 
     
    
    
    exit:
    mov ah,4ch
    int 21h 
    
    MAIN ENDP
END MAIN