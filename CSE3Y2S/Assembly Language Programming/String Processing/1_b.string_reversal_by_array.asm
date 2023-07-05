;string reversal : using array

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
         
    MOV SI,0
    MOV DI,0
       
    MOV AH,1 
    
    INPUT:
      
      INT 21H
      CMP AL,13;IF ENTER KEY IN PRESSED
      JE END_INPUT
      
      MOV ARR[SI],AL
      INC SI
      JMP INPUT 
      
    END_INPUT:
    MOV DI,SI
    MOV SI,-1
    
    REVERSE:
      INC SI
      DEC DI 
      CMP SI,DI 
      JG DISPLAY
      MOV BL,ARR[SI]
      XCHG BL,ARR[DI] 
      MOV ARR[SI],BL
      JMP REVERSE
       
    DISPLAY: 
    LEA DX,MSG2
    MOV AH,9
    INT 21H
    
    LEA DX,ARR
    MOV AH,9
    INT 21H

    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN
