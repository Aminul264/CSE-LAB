.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB       'INPUT NUMBER   : $'
MSG2 DB 10,13,'FACTORIAL      : $'

FACT DB 1

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
    
    
    XOR CX,CX
    MOV CL,AL  
    MOV AL,1
    
    JCXZ PRINT;  
    
    FACT_:
        CMP CL,1
        JE PRINT
        
        MUL CL ;AL=AL*CL
        LOOP FACT_
     
           

    
    PRINT: 
    MOV FACT ,AL
    MOV AH,9 
    LEA DX,MSG2
    INT 21H  
    
    ;DIGIT TO ASCCI
    ADD FACT,48 
    MOV AH,2
    MOV DL,FACT
    INT 21H
      
                     

    
   
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN