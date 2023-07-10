.MODEL SMALL 
.STACK 100H
.DATA

 MSG1 DB '      INPUT NUMBER :$'
 MSG2 DB 10,13,'       PRIME  $' 
 MSG3 DB 10,13,'     NOT PRIME$' 
 
 
 N DB ?   
           
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
    ;ASCCI TO DIGIT
    SUB AL,48 
    
    ;DIVIDE N BY (1 TO N-1 ) 
    XOR CX,CX
    MOV N,AL  
    MOV CL,AL
    SUB CL,1 
    
    
    CMP N,0 
    JE NOT_PRIME
    CMP N,1
    JE PRIME
    
    
    CHECK:
        CMP CL,1
        JE PRIME 
        
        DIV CL  ;  QUOTIENT AL=AX/CL   REMAINDER AH=AX%CL 
        CMP AH,0
        JE NOT_PRIME 
        
        XOR AX,AX
        MOV AL,N
        LOOP CHECK
        
    PRIME:
        LEA DX,MSG2
        MOV AH,9
        INT 21H
        JMP EXIT
        
    NOT_PRIME: 
        LEA DX,MSG3
        MOV AH,9
        INT 21H

    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN