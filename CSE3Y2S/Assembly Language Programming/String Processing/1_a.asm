;Case conversion

.MODEL SMALL 
.STACK 100H
.DATA

 MSG1 DB '      INPUT STRING : $'
 MSG2 DB 10,13,'AFTER CASE CONVERTION: $'
 
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
    MOV SI,-1  
    
    CASE_CONVERSION:
       
       INC SI
       CMP ARR[SI],'$'
       JE DISPLAY
       
       CMP ARR[SI],'A'
       JL NO_CHANGE
       CMP ARR[SI],'z'
       JG NO_CHANGE
       CMP ARR[SI],'Z'
       JLE TO_LOWER
       CMP ARR[SI],'a'
       JGE TO_UPPER
       
    NO_CHANGE:
      JMP CASE_CONVERSION
       
    TO_LOWER:
       ADD ARR[SI],32
       JMP CASE_CONVERSION 
       
    TO_UPPER: 
       SUB ARR[SI],32 
       JMP CASE_CONVERSION
    
       
       
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
