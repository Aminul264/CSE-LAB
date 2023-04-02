.MODEL SMALL
.STACK 100H
.DATA

    msg1 db 10,13,'Input array element : $'
    msg2 db 10,13,'Ascending order : $'
    msg3 db 10,13,'Descending order : $'
     
    arr db 100 dup('$') 
    n dw ?
    
.CODE

MAIN PROC
     
     mov ax,@data
     mov ds,ax    
     
     ;taking input array 
     mov si,0 
     
     
     ;print msg1
      lea dx,msg1
      mov ah,9
      int 21h
        

input:
     mov ah,1 
     int 21h 
     
     cmp al,13 ; check if Enter key is pressed
     je end_input
     mov arr[si],al 
     inc si
     jmp input
     
end_input: 
     mov arr[si],'$'

   mov si,-1 
outer_loop:
    inc si
    mov di,si
    cmp arr[si],'$'
    je print 
   
                 
  inner_loop:
  
    inc di 
    cmp arr[di],'$'
    je outer_loop
    ;memory to memory not possible so,need extra register
    mov bl,arr[di]
    cmp arr[si],bl
    jl inner_loop
    
    XCHG arr[si],bl
    mov arr[di],bl 
    
    jmp inner_loop
  
   

print:
    mov si,0 
    ;print msg2
    lea dx,msg2
    mov ah,9
    int 21h      
                 
ascending:

       mov dl,arr[si]
       mov ah,2
       int 21h 
       
       inc si 
  
       cmp arr[si],'$'
       jz msg_desc
       jmp ascending


msg_desc:
    dec si
    lea dx,msg3
    mov ah,9
    int 21h
 
descendig: 
       mov dl,arr[si]
       mov ah,2
       int 21h
       
       dec si
       
       cmp si,-1
       jne descendig
       

  
    exit:
    mov ah,4ch
    int 21h 
    
MAIN ENDP
END MAIN
