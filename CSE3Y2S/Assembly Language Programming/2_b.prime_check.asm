;even odd check (1-9)
;given a digit (1-9)  prime check


.MODEL SMALL
.STACK 100H
.DATA

    input db 10,13,'Enter a number (1-9) : $'
    prime_msg db 10,13,'prime number$'
    not_prime_msg db 10,13,'not a prime number$' 
    
   prime_arr db  2,3,5,7,'$' 
    
    
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
     sub al,48
     
     mov cx,4 
     lea si, prime_arr   
     
loop_:     
     
     cmp al,[si]
     jz prime  
     inc si
     loop loop_ 
     
     
     lea dx,not_prime_msg
     mov ah,9
     int 21h
     jmp exit
      
     
     


prime:
     lea dx,prime_msg
     mov ah,9
     int 21h
  
    exit:
    mov ah,4ch
    int 21h 
    
    MAIN ENDP
END MAIN
