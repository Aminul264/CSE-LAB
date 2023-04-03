
;find first capital and last capital of a string



.model small
.stack 100h
.data  

 msg1 db       'Enter a string  : $'
 msg2 db 10,13,'First capital   : $'
 msg3 db 10,13,'Last capital    : $' 
 msg4 db 10,13,'No capitals     :  $'
 
 first1 db 91;say first capital=91
 last1  db 64;say last capital =64
 
 str db 100 dup ('$')   
     
     
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
      mov si,0
      mov bl,first1
      mov cl,last1
      
      
process:    
      cmp str[si],'$'
      je end_process 
      
      cmp str[si],'A'
      jl next_elem
      
      cmp str[si],'Z'
      jg next_elem
       
      
      ;check first capital
      cmp str[si],bl
      jl first
   
      ;check last capital
      cmp str[si],cl
      jg last  
      
      
      inc si
      jmp process


first: 
     mov bl,str[si]
     inc si
     jmp process  
     
last:
    mov cl,str[si]
    inc si
    jmp process
          
next_elem:
      inc si
      jmp process
      


end_process: 

;check is no capital exist?
cmp bl,91;64means same as before (defined)
jnz print_capitals

lea dx,msg4
mov ah,9
int 21h
jmp exit
 
 
print_capitals:
;print first capital  

  lea dx,msg2
  mov ah,9
  int 21h

  mov dl,bl
  mov ah,2
  int 21h 
  
  
;print last capital  

  lea dx,msg3
  mov ah,9
  int 21h 
  mov dl,cl
  mov ah,2
  int 21h


    
    exit:
    mov ah,4ch
    int 21h
    
    main endp
end main