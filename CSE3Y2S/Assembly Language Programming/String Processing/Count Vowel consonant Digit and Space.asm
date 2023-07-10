.MODEL SMALL
.STACK 100H
.DATA 
MSG1 DB             'INPUT STRING   :$'
MSG2 DB 10,13,'NUMBER OF VOWELS     : $'
MSG3 DB 10,13,'NUMBER OF CONSONANT  : $'
MSG4 DB 10,13,'NUMBER OF DIGIT      : $'
MSG5 DB 10,13,'NUMBER OF SPACE      : $' 
MSG6 DB 10,13,'NUMBER OF SPECIAL    : $'

VOWEL      DB '0'
CONSONANT  DB '0'
DIGIT      DB '0'
SPACE      DB '0' 
SPECIAL    DB '0'  

VW DB 'AEIOUaeiou$'
DG DB '0123456789$'


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
                  
                  
        ;CHECK SPACE
        CMP AL,' '  
        JE UPDATE_SPACE 
        
        ;CHECK VOWEL
        MOV SI,-1
        MOV CX,10
        CHECK_V:
            INC SI
            CMP AL,VW[SI]
            JE UPDATE_VOWEL
            LOOP CHECK_V
             
        ;CHECK DIGIT
        MOV CX,10
        MOV SI,-1
        CHECK_D: 
            INC SI
            CMP AL,DG[SI]
            JE UPDATE_DIGIT
            LOOP CHECK_D
        
        ;CONSONAT CHECK
        CMP AL,'A'
        JL UPDATE_SPECIAL
        CMP AL,'z'
        JG UPDATE_SPECIAL
        CMP AL,'Z'
        JLE UPDATE_CONSONANT
        CMP AL,'a'
        JGE UPDATE_CONSONANT
        
        
        ;
        JMP UPDATE_SPECIAL 
       
            
   
         
    UPDATE_SPACE:
        INC SPACE
        JMP INPUT
           
    UPDATE_VOWEL:
        INC VOWEL
        JMP INPUT
        
    UPDATE_CONSONANT:
        INC CONSONANT
        JMP INPUT
        
    UPDATE_DIGIT:
        INC DIGIT
        JMP INPUT  
        
    UPDATE_SPECIAL: 
        INC SPECIAL
        JMP INPUT
    
        
    END_INPUT: 
    
    ;PRINT
    PRINT:
        ;VOWEL 
        MOV AH,9
        LEA DX,MSG2 
        INT 21H
        ;
        MOV AH,2
        MOV DL,VOWEL
        INT 21H
        
        ;CONSONANT
        MOV AH,9
        LEA DX,MSG3 
        INT 21H
        ;
        MOV AH,2
        MOV DL,CONSONANT
        INT 21H
        
        ;DIGIT
        MOV AH,9
        LEA DX,MSG4 
        INT 21H
        ;
        MOV AH,2
        MOV DL,DIGIT
        INT 21H
        
        ;SPACE
        MOV AH,9
        LEA DX,MSG5 
        INT 21H
        ;
        MOV AH,2
        MOV DL,SPACE
        INT 21H
        
        ;SPECIAL
        MOV AH,9
        LEA DX,MSG6 
        INT 21H
        ;
        MOV AH,2
        MOV DL,SPECIAL
        INT 21H
        

    
   
    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN