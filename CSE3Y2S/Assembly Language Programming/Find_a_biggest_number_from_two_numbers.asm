.model small
.stack 100h
.data  
msg1 db 'Input two numbers : $'
msg2 db 10,13,'Biggest Number : $'
big db ?

.code 

main proc

  mov ax,@data
  mov ds,ax  
  
             
  mov ah,9 
  lea dx,msg1
  int 21h 
   
   
   mov ah,1
   int 21h
   mov bl,al
   int 21h
   mov bh,al 
   
   ;check and jump
   cmp bl,bh ; bl-bh
   jg l1
   jmp l2
   
   
   
   l1:
   mov big,bl
   jmp biggest
   
   
   l2:       
   mov big,bh
   jmp biggest
    
   biggest:
   mov ah,9
   lea dx,msg2
   int 21h
   
   mov ah,2
   mov dl,big
   int 21h 
   jmp exit
   


  exit:
  mov ah,4ch
  int 21h
            
  main endp
end main
  
  
  
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
       
