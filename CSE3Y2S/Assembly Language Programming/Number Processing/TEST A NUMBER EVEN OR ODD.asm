.MODEL SMALL 
.STACK 100H
.DATA

 MSG1 DB '      INPUT STRING  : $'
 MSG2 DB 10,13,'       EVEN$' 
 MSG3 DB 10,13,'       ODD$'
 

.CODE
          
               
          
MAIN PROC  
    
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    LEA DX,MSG1
    MOV AH,9
    INT 21H
    
    ;INPUT
    MOV AH,1
    INT 21H  
    
    ;CHECK
    
    TEST AL,1     ;AL&0001  ;JE==JZ
    JZ EVEN
    JMP ODD
    

       
    EVEN: 
        LEA DX,MSG2
        MOV AH,9
        INT 21H
        JMP EXIT
    
    ODD:
        LEA DX,MSG3
        MOV AH,9
        INT 21H

    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN