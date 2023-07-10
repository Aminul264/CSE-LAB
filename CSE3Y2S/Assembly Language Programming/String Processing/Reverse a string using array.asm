.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB 'INPUT STRING : $'
MSG2 DB 10,13,'REVERSE STRING : $'

ARR DB 100 DUP('$')

.CODE
MAIN PROC 
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    MOV AH,9
    LEA DX,MSG1 
    INT 21H   
    
    MOV SI,-1 
    MOV AH,1
    INPUT: 
        
        INT 21H 
        INC SI
        CMP AL,13
        JE END_INPUT
        
        MOV ARR[SI],AL 
        JMP INPUT  
        
    END_INPUT: 
             
    MOV DI,SI
    MOV SI,-1
    REVERSE:
        INC SI
        DEC DI
        
        CMP SI,DI
        JG PRINT
        
        MOV BL,ARR[DI]
        XCHG BL,ARR[SI]
        MOV ARR[DI],BL
        
        JMP REVERSE

    
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