.MODEL SMALL
.STACK 100H
.DATA

    input db 10,13,'Enter a number (1-3) : $' 
    result_msg db 10,13,'Factorial : $' 
    
  n db 48
    
    
.CODE


MAIN PROC
     
     mov ax,@data
     mov ds,ax 
     
     lea dx,input
     mov ah,9
     int 21h  
     
     
     ;take input
     mov ah,1
     int 21h 
     
     
     ;sub al,48
     mov bl,al  
     mov al,1 
     
     loop_: 
     mul bl  ;al=al*bl
     div n 
     sub bl,1 ;
     cmp bl,48
     jnz loop_
     
     
     ;print rsult
     
     lea dx,result_msg 
     mov ah,9
     int 21h
    
     ;
     mov ah,2
     mov dl,al
     int 21h
     
     
     

    
    exit:
    mov ah,4ch
    int 21h 
    
    MAIN ENDP
END MAIN