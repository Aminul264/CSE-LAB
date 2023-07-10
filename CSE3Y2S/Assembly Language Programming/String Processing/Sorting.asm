.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB             'INPUT STRING   : $'
MSG2 DB 10,13,'AFTER SORTING    : $'

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
        
        INC SI
        INT 21H
        CMP AL,13
        JE END_INPUT
        
        MOV ARR[SI],AL
        JMP INPUT    
    
        
    END_INPUT:
    
    MOV SI,-1
    OUTER:
      INC SI
      MOV DI,SI  
      CMP ARR[SI],'$'
      JE PRINT
         
         INNER:
            INC DI
            CMP ARR[DI],'$'
            JE OUTER
            
            MOV BL,ARR[SI]
            CMP BL,ARR[DI]
            JL INNER
            XCHG BL,ARR[DI]
            MOV ARR[SI],BL 
            
            JMP INNER
              
           
           
    PRINT:
    MOV AH,9 
    LEA DX,MSG2
    INT 21H
    
    MOV AH,9
    LEA DX,ARR
    INT 21H
      
                     

    
   
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN