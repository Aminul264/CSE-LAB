            .MODEL SMALL
.STACK 100H
.DATA 

MSG1 DB 'BEFORE CONVERSION : $'
MSG2 DB  10,13,'AFTER CONVERSION : $'

ARR DB 100 DUP('$')


.CODE
MAIN PROC 
     
     
    MOV AX,@DATA
    MOV DS,AX 
    
    
    MOV AH,9
    LEA DX,MSG1
    INT 21H
    
    ;INPUT 
    MOV SI,-1 
    MOV AH,1
           
    INPUT:
    
        INC SI
        INT 21H
        CMP AL,13
        JE END_INPUT
        
        MOV ARR[SI],AL
        JMP INPUT
        
        
    END_INPUT:
    
    
    MOV SI,-1
    CASE_CONVERSE:
        
        INC SI 
    
        CMP ARR[SI],'$'
        JE PRINT
        
        CMP ARR[SI],'A'
        JL CASE_CONVERSE
        
        CMP ARR[SI],'z'
        JG CASE_CONVERSE
        
        CMP ARR[SI],'Z' 
        JLE TO_LOWER
        
        CMP ARR[SI],'a'
        JGE TO_UPPER    
        
    TO_UPPER: 
    
        SUB ARR[SI],32
        JMP CASE_CONVERSE
        
    TO_LOWER:
         ADD ARR[SI],32
         JMP CASE_CONVERSE 
    
        
    PRINT:
    
    MOV AH,9  
    LEA DX,MSG2
    INT 21H
    LEA DX,ARR
    INT 21H
   
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN