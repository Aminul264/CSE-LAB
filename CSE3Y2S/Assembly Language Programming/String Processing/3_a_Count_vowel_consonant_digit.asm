
;find vowel, consonant,space and digit of a string


.model small
.stack 100h
.data  

 msg1 db      'Enter a string      : $' 
 msg2 db 10,13,'Vowel              : $'
 msg3 db 10,13,'Consonat           : $' 
 msg4 db 10,13,'digit              : $'    
 msg5 db 10,13,'Space              : $' 
 msg6 db 10,13,'special              : $'  
 
 
 str  db 100 dup('$')  
 
 vowels db 'AEIOUaeiou$'
 digits db '0123456789$'
 
 vc    db 0
 cc    db 0
 sc    db 0
 dc    db 0  
 spcl  db 0
 
  
  
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
      
count:
      cmp str[si],'$'
      je end_count 
      
      ;space check
      cmp str[si],32 
      je space_count 
      
      
      ;vowel check  
      mov di,0
      mov cx,10
      mov bl,str[si]
      check_vowel:
            cmp bl,vowels[di] 
            je vowel_count
            inc di
            loop check_vowel 
      
      
      ;digit check
      mov di,0
      mov cx,10
      check_digit:
            cmp bl,digits[di]
            je digit_count  
            inc di
            loop check_digit 
            
      
      
      ;consonant check
      cmp bl,'A'
      jl special_count
      cmp bl,'z'
      jg  special_count
      
      
      jmp consonant_count
      
       
      inc si
      jmp count
         
      
end_count: 
jmp print

vowel_count:
      add vc,1
      inc si  
      jmp count  
      
digit_count:
      add dc,1
      inc si
      jmp count
          
space_count: 
      inc sc   
      inc si
      jmp count  
      
consonant_count:
     inc cc;
     inc si
     jmp count
special_count:
     inc spcl
     inc si
     jmp count
      
      
          

;print vowel  
print:
 lea dx,msg2
 mov ah,9
 int 21h
 
 add vc,48
 mov dl,vc
 mov ah,2
 int 21h  
 
 ;print consonat
 lea dx,msg3
 mov ah,9
 int 21h
 
 add cc,48
 mov dl,cc
 mov ah,2
 int 21h
    
;print digit
 lea dx,msg4
 mov ah,9
 int 21h
 
 add dc,48
 mov dl,dc
 mov ah,2
 int 21h
        
        
;print space
 lea dx,msg5
 mov ah,9
 int 21h
 
 add sc,48
 mov dl,sc
 mov ah,2
 int 21h  
 

 
    
    exit:
    mov ah,4ch
    int 21h
    
    main endp
end main
