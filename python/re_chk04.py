import re

a="""
//**********************************************************************
//***  STEP281:  UNLOAD - IH TABLE                                   ***
//**********************************************************************
//STEP281 EXEC CPWUNLDB,COND=(0,NE),                                    
//            MODE=PROD,          * RUN ENVIRONMENT                     
//            LIB=,               * GROUP LIBRARY                       
//            GDGC='(0)',         * CURRENT GDG                         
//            GDGN='(+1)',        * NEXT GDG                            
//            LABEL=34,           * CART LABEL NUMBER                   
//*                               * IF RESTARTED CHANGE THIS LABEL TO 1 
//            DBASE=2,            * DB2 DATABASE NAME                   
//            TABLE=IH,           * CAPS-I-L TABLE NAME                 
//            STEPNUM=STEP280     * THIS REFERS BACK TO THE PREV STEP   
//*=== UNCOMMENT THE NEXT LINE IF RESTARTED FROM THIS STEP ==*          
//STEPLIB   DD DSN=~USER.TEST.STEPLIB
//          DD DSN=~LIB.TEST.STEPLIB
//          DD DSN=~USER.TEST.STEPLIB
//          DD DSN=~ACCPT.TEST.STEPLIB
//          DD DSN=~UACCR.TEST.STEPLIB
//*CPUNLD10.SYSREC   DD VOL=(PRIVATE,RETAIN,,40)                        
//*                                                                     
//****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
%INCLUDE IF (TODAY('LAST FRIDAY OF MONTH LESS 0 WORKDAYS')  +           
          OR TODAY('LAST WORKDAY OF YEAR'))                 +           
          OR TODAY('LAST WORKDAY OF YEAR'))                             
%INCLUDE IF (TODAY('LAST FRIDAY OF MONTH LESS 0 WORKDAYS')  +           
          OR TODAY('LAST WORKDAY OF YEAR'))                 +           
          OR TODAY('LAST WORKDAY OF YEAR'))                             
//****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
//**********************************************************************
//***  STEP284:  UNLOAD - UHCO TABLE                                 ***
//**********************************************************************
//STEP284 EXEC CPWUNLDB,COND=(0,NE),                                    
//            MODE=PROD,          * RUN ENVIRONMENT                     
//            LIB=,               * GROUP LIBRARY                       
//            GDGC='(0)',         * CURRENT GDG                         
//            GDGN='(+1)',        * NEXT GDG                            
//            LABEL=35,           * CART LABEL NUMBER                   
//*                               * IF RESTARTED CHANGE THIS LABEL TO 1 
//            DBASE=3,            * DB2 DATABASE NAME                   
//            TABLE=UHCO,         * CAPS-I-L TABLE NAME                 
//            STEPNUM=STEP281     * THIS REFERS BACK TO THE PREV STEP   
//*=== UNCOMMENT THE NEXT LINE IF RESTARTED FROM THIS STEP ==*          
//*CPUNLD10.SYSREC   DD VOL=(PRIVATE,RETAIN,,40)                        
//*                                                                     
//****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
%INCLUDE IF (TODAY('LAST FRIDAY OF MONTH LESS 0 WORKDAYS')              
//****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
"""


def remove_str_in_jcl_body(str_to_remove,lines_in_jcl):
    edited_lines=re.sub(str_to_remove,"",lines_in_jcl)
    return edited_lines


b=a
b=remove_str_in_jcl_body("~LIB",b)
b=remove_str_in_jcl_body("~USER",b)
b=remove_str_in_jcl_body("~ACCPT",b)
b=remove_str_in_jcl_body("~UACCR",b)

print(b)

