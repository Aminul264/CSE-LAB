.MODEL SMALL 
.STACK 100H
.DATA

 MSG1 DB '      INPUT NUMBER   :$'
 MSG2 DB 10,13,'LARGEST NUMBER :$'  
 
 
 MAX DB 0 
           
.CODE
          
               
          
MAIN PROC  
    
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    LEA DX,MSG1
    MOV AH,9
    INT 21H  
    
    MOV AH,1
    INPUT: 
        INT 21H
        CMP AL,13
        JE END_INPUT  
        
        CMP AL,MAX
        JL INPUT
        
        MOV MAX,AL
        
        JMP INPUT
        
    
    END_INPUT:
    
    ;PRINT OUPUT
        LEA DX,MSG2
        MOV AH,9
        INT 21H
        
    
        MOV AH,2
        MOV DL,MAX
        INT 21H

    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN