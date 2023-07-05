
;find first capital and last capital of a string

 
 ;FIND OUT FIRST CAPITAL AND LAST CAPITAL 
.MODEL SMALL 
.STACK 100H
.DATA
 
 MSG0 DB 10,13,'ENTER ACSTRING : $'
 MSG1 DB 10,13,'FIRST CAPITAL : $' 
 MSG2 DB 10,13,'LAST CAPITAL  : $'
 MSG3 DB 10,13,'NO CAPITAL  : $'
 
 ARR DB 100 DUP('$') 
 FC  DB 91   ;FC=FIRST CAPITAL
 LC  DB 64  ;LC=LAST CAPITAL
 
 
.CODE
          
               
          
MAIN PROC  
    
    
    MOV AX,@DATA
    MOV DS,AX 
    
    
    LEA DX,MSG0
    MOV AH,9
    INT 21H
       
    MOV AH,1 
    MOV SI,-1
    
    INPUT:
      INT 21H
      CMP AL,13;IF ENTER KEY IN PRESSED
      JE END_INPUT 
      
      CMP AL,'Z'
      JG INPUT 
      CMP AL,FC
      JL UPDATE_FC 
      CMP AL,LC
      JG UPDATE_LC
      
      JMP INPUT 
    
    UPDATE_FC: 
       MOV FC,AL
       JMP INPUT
       
    UPDATE_LC:
       MOV LC,AL
       JMP INPUT
      
    END_INPUT:
    
    
    CMP LC,64
    JNE PRINT
    
    MOV AH,9
    LEA DX,MSG3
    INT 21H 
    JMP EXIT
    
    
    PRINT:
    LEA DX,MSG1
    MOV AH,9
    INT 21H
    MOV AH,2
    MOV DL,FC
    INT 21H 
    
    MOV AH,9
    LEA DX,MSG2
    INT 21H
    MOV AH,2
    MOV DL,LC
    INT 21H

       

    
    EXIT:
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
END MAIN
