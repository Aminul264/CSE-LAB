
;Sorting a string ascending and descending order





.model small
.stack 100h
.data  
 msg1 db 'Enter string :$'
 msg2 db 10,13,'Ascending order:$'
 msg3 db 10,13,'Descending order:$'
 
 str db 100 dup ('$')
 
 
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
    mov si,0 
    
    
    ;sorting ascending order

      mov si,-1
outer_loop:
      inc si 
      cmp str[si],'$'
      je end_loop
      mov di,si
      mov bl,str[si]
      inner_loop:
        cmp str[di],'$'
        je outer_loop
        
        cmp bl,str[di]
        jl next_elem
        
        xchg bl,str[di]
        mov str[si],bl   
        
        
      next_elem:
        inc di
        jmp inner_loop
         
end_loop: 



;print ascending order
lea dx,msg2
mov ah,9
int 21h

lea dx,str
mov ah,9
int 21h   


;print descending order

lea dx,msg3
mov ah,9
int 21h

dec si
loop_:
     mov ah,2
     mov dl,str[si] 
     int 21h 
     dec si 
     cmp si,0
     jl exit
     loop loop_
     
        
    
    
    exit:
    mov ah,4ch
    int 21h
    
    main endp
end main

