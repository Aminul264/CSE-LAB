.MODEL SMALL
.STACK 100H
.DATA  
    TEXT     DB 'AMAR SONAR BANGLADESH$'
    PATTERN  DB 'DE$' 
    MSG1     DB 10,13,'FOUND$' 
    MSG2     DB 10,13,'NOT FOUND$'
    

.CODE
MAIN PROC 
    
    MOV AX,@DATA
    MOV DS,AX
    
    MOV SI,-1
    MOV DI,0 
    SEARCH:
        INC SI 
        CMP TEXT[SI],'$'
        JE NOT_FOUND  
        
        MOV BL,TEXT[SI]
        CMP BL,PATTERN[DI]
        JE UPDATE_INDEX  
         ;AGAIN SEARCH PATTERN FROM ZERO INDEX
        MOV DI,0
        JMP SEARCH
        
          
        
        
    UPDATE_INDEX: 
        INC DI
        CMP PATTERN[DI],'$'
        JE FOUND
        JMP SEARCH
    
        
        
        
    
    END_CHECK:
    NOT_FOUND:
        MOV AH,9
        LEA DX,MSG2
        INT 21H 
        JMP EXIT
    FOUND:
        MOV AH,9
        LEA DX,MSG1
        INT 21H
          
    
    EXIT:
    MOV AH,4CH
    INT 21H
    MAIN ENDP
END MAIN
