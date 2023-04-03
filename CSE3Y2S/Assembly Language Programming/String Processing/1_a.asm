;Case conversion

.model small
.stack 100h
.data  
    msg1 db 'Enter a string : $'
    msg2 db 10,13,'After case conversion : $' 
    str  db 10,13,100 dup ('$');
.code

main proc 
    mov ax,@data
    mov ds,ax
    
    lea dx,msg1
    mov ah,9
    int 21h   
    
    ;input
    mov  si,0
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

      
case_conversion:
      
     
     cmp str[si],'$'
     je end_conversion
     
     cmp str[si],'A'
     jl no_change 
     cmp str[si],'Z'
     jle to_lower
     
     
     cmp str[si],'z' 
     jg no_change  
     cmp str[si],'a'
     jge to_upper
     
     
          
     
no_change:
     inc si
     jmp case_conversion  
     
     
to_lower:
        add str[si],32
        inc si
        jmp case_conversion 
to_upper:
        sub str[si],32
        inc si
        jmp case_conversion
        
        
 
 
end_conversion:
     
     lea dx,msg2
     mov ah,9
     int 21h
             
             
     ;after conversion
     
     lea dx,str
      mov ah,9
      int 21h 
     
    
      
    exit:
    mov ah,4ch
    int 21h
    
    main endp
end main
