;REVERSE USING STACK


 ;STRING REVERSE USING STACK
.MODEL SMALL 
.STACK 100H
.DATA

 MSG1 DB '      INPUT STRING  : $'
 MSG2 DB 10,13,'AFTER REVERSAL: $'
 
 ARR DB 100 DUP('$')
 
.CODE
          
               
          
MAIN PROC  
    
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    LEA DX,MSG1
    MOV AH,9
    INT 21H
       
    MOV AH,1 
    MOV CX,0
    
    INPUT:
      
      INT 21H
      CMP AL,13;IF ENTER KEY IN PRESSED
      JE END_INPUT
      
      PUSH AX
      INC CX
      JMP INPUT 
      
    END_INPUT:
    ;NEWLINE
    MOV AH,9
    LEA DX,MSG2
    INT 21H
    
    MOV AH,2
    REVERSE:
      POP DX 
      INT 21H
      LOOP REVERSE
       

    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN
