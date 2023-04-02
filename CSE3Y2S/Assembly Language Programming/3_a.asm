.MODEL SMALL
.STACK 100H
.DATA

    out_msg db 10,13,'largest number : $' 
    arr db 100 dup('$')
    
.CODE

MAIN PROC
     
     mov ax,@data
     mov ds,ax    
     
     ;taking input array 
     mov si,0
input:
     mov ah,1 
     int 21h 
     
     cmp al,13 ; check if Enter key is pressed
     je end_input
     
     sub al,48  
     mov arr[si],al 
     inc si
     jmp input
     
end_input: 
     mov arr[si],'$' 
     
     ;let bl=0
     mov bl,0 
     mov si,0  
     
find_largest: 
     cmp arr[si],'$'
     je display   
     
     cmp bl,arr[si]
     jge next_elem
     mov bl,arr[si]

next_elem: 
     inc si
     jmp find_largest
     
display:
     lea dx,out_msg
     mov ah,9
     int 21h 
     

     add bl,48 
     
     mov dl,bl 
     mov ah,2
     int 21h
  
    exit:
    mov ah,4ch
    int 21h 
    
MAIN ENDP
END MAIN
