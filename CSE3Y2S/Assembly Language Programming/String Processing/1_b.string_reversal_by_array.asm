;string reversal : using array


.model small
.stack 100h
.data  

 msg1 db 'Enter a string  : $'
 msg2 db 10,13,'After reversal : $'
 
 str db 10,13,100 dup ('$')
.code

main proc   
    
    mov ax,@data
    mov ds,ax   
    
    ;print msg1
    lea dx,msg1
    mov ah,9
    int 21h
    
    ;take input
    mov si,0
input:  

      mov ah,1
      int 21h
      cmp al,13
      je end_input  
      mov str[si],al
      inc si 
      jmp input 
      
end_input:
    dec si 
    
    
;print msg2
   lea dx,msg2
   mov ah,9
   int 21h

   
;after reverse
print:
   cmp si,-1
   je exit
   
   mov dl,str[si]
   mov ah,2
   int 21h 
   
   dec si
   jmp print
   

    
    exit:
    mov ah,4ch
    int 21h
    
    main endp
end main
