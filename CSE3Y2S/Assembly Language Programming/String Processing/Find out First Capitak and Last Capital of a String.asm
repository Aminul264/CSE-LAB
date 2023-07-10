.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB 'INPUT STRING : $'
MSG2 DB 10,13,'FIRST CAPITAL : $'
MSG3 DB 10,13,'LAST CAPITAL  : $'
MSG4 DB 10,13,'NO CAPITAL $'

FC DB 91
LC DB 64


.CODE
MAIN PROC 
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    MOV AH,9
    LEA DX,MSG1 
    INT 21H   
    
    MOV AH,1
    INPUT:   
    
        INT 21H
        CMP AL,13
        JE END_INPUT
        
        CMP AL,'Z'
        JG INPUT
        CMP AL,'A'
        JL INPUT
        
        CMP AL,FC
        JL UPDATE_FC
        
        CMP AL,LC
        JG UPDATE_LC  
        
        
        
        JMP INPUT
        
    UPDATE_FC:
    
        MOV FC,AL
 
       ;SAY ONLY ONE INPUT
       CMP LC,AL
       JL UPDATE_LC
         
       JMP INPUT
        
    UPDATE_LC: 
    
        MOV LC,AL
        JMP INPUT
    
        
    END_INPUT: 
    
    CMP LC,64
    JE NO_CAPITAL
    
 
    PRINT:
            
    MOV AH,9
    LEA DX,MSG2
    INT 21H   
    ;PRINT FC
    MOV AH,2
    MOV DL,FC
    INT 21H 
    ;PRINT LC
    MOV AH,9
    LEA DX,MSG3
    INT 21H  
    MOV AH,2
    MOV DL,LC
    INT 21H
    JMP EXIT
    
    
        
    NO_CAPITAL:
        MOV AH,9       
        LEA DX,MSG4
        INT 21H
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN