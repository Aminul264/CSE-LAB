;even odd check (1-9)
;given a digit (1-9)  then check is it even or odd


.MODEL SMALL
.STACK 100H
.DATA

    input db 10,13,'Enter a number (1-9) : $'
    odd_msg db 10,13,'Odd number$'
    even_msg db 10,13,'Even number$' 
    
    
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
     
     test al,1; last bit of al*1
     jz even   
     ;else odd
     lea dx,odd_msg
     mov ah ,9
     int 21h  
     jmp exit
     
     
 even:
     lea dx,even_msg
     mov ah ,9
     int 21h
     
     
  
    exit:
    mov ah,4ch
    int 21h 
    
    MAIN ENDP
END MAIN


