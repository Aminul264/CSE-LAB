.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB       'INPUT NUMBER   : $'
MSG2 DB 10,13,'SUM(1-N)       : $'

SUM DB 0

.CODE
MAIN PROC 
    
    MOV AX,@DATA
    MOV DS,AX 
    
    ;PRINT MSG1
    MOV AH,9
    LEA DX,MSG1 
    INT 21H   
    
    MOV AH,1
    INT 21H  
    
    ;ASCCI TO DIGIT
    SUB AL,48
    
    ;FOR CLEAR CX
    XOR CX,CX
    MOV CL,AL
    JCXZ PRINT
    
    ADD_:
     ADD SUM,CL
     LOOP ADD_
              
           
       
    PRINT:
    MOV AH,9 
    LEA DX,MSG2
    INT 21H
    ;DIGIT TO ASCCI
    ADD SUM,48 
    MOV AH,2
    MOV DL,SUM
    INT 21H
      
                     

    
   
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN