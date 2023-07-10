.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB 'INPUT STRING : $'
MSG2 DB 10,13,'REVERSE STRING : $'

.CODE
MAIN PROC 
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    MOV AH,9
    LEA DX,MSG1 
    INT 21H   
    
    MOV CX,0
    MOV AH,1
    INPUT: 
        INT 21H
        CMP AL,13
        JE END_INPUT
        
        PUSH AX 
        INC CX
        JMP INPUT
        
    END_INPUT: 
    
 
    PRINT:
            
    MOV AH,9
    LEA DX,MSG2
    INT 21H 
    
    MOV AH,2 
    JCXZ EXIT:
    REVERSE:
        POP DX
        INT 21H
        LOOP REVERSE
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN