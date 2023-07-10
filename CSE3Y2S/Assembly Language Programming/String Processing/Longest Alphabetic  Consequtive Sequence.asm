.MODEL SMALL

.STACK 100H

.DATA   
    
    MSG DB 'ENTER A STRING :$' 
    NEW_LINE DB 10,13,'$'
    
    MAX   DW 0
    INDEX DW 0   
    
    ARR DB 100 DUP('$')
    
.CODE  


MAIN PROC

    MOV AX, @DATA
    MOV DS, AX  
    
    
    MOV AH,9
    INT 21H
    
         
    MOV SI,-1          
    MOV AH,1   
    INPUT: 
        INC SI
        INT 21H
        CMP AL, 13
        JE END_INPUT
        
        MOV ARR[SI],AL
        JMP INPUT
    
    END_INPUT:   
    
    ;CHECK   
    MOV CX,1
    MOV SI,-1 
    
    CHECK: 
      INC SI 
      CMP ARR[SI],'$'
      JE END_CHECK
      
      MOV BL,ARR[SI]  
      MOV BH,ARR[SI+1]
      
      INC BL 
      CMP BL,BH   
      JNE CHECK_MAX 
      
      ;BL==BH
      INC CX 
      
      JMP CHECK
      
      
    CHECK_MAX:
        CMP CX,MAX
        JG UPDATE_MAX ; IF MAX IS  GREATER
        
        MOV CX,1
        JMP CHECK; 
        
        
    UPDATE_MAX:
        MOV MAX,CX 
        MOV BX,SI;BX FOR TMP INDEX
        SUB BX,CX
        MOV INDEX ,BX
        MOV CX,1
        JMP CHECK
      
      
    END_CHECK:
    
    LAST_CHECK:
        CMP CX,MAX
        JLE PRINT 
        
        ;UPDATE
        MOV MAX,CX
        MOV BX,SI
        SUB BX,CX
        MOV INDEX,BX 
        
        
    PRINT:
            
        ;NEWLINE
        LEA DX, NEW_LINE
        MOV AH,9
        INT 21H
        ;
        ;NUMBER OF CHAR
        ADD MAX,48
        MOV AH,2
        MOV DX,MAX
        INT 21H  
        
        ;NEWLINE
        LEA DX,NEW_LINE
        MOV AH,9
        INT 21H
    ;PRINT SEQUENCE
        SUB MAX,48
        MOV CX,MAX
        MOV SI,INDEX
        
        SEQUENCE: 
            INC SI
            MOV AH,2
            MOV DL,ARR[SI]
            INT 21H
        LOOP SEQUENCE
    
   
MAIN ENDP   
END MAIN
        