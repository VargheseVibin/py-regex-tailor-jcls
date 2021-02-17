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



def delete_jcl_sysin_and_following_lines_starting_with_whitespaces(sysin_val,lines_in_jcl):
    edited_lines                =lines_in_jcl
    pattern_sysin_and_next_line=r"(^"+sysin_val+r"\s+.*?$)(?:\r?)\n(\s+.*?$)"
    rgx_sysin_next_line         =re.compile(pattern_sysin_and_next_line,
                                    flags=(re.DOTALL|re.MULTILINE))
    print("Attempting match for regex:"+pattern_sysin_and_next_line)
    match_sysin_next_line       =rgx_sysin_next_line.search(edited_lines)
    while(match_sysin_next_line):
        print("Match for sysin with next line found")
        edited_lines                =rgx_sysin_next_line.sub(r"\1",edited_lines)
        match_sysin_next_line       =rgx_sysin_next_line.search(edited_lines)
    pattern_sysin_single_line   =r"^"+sysin_val+r"\s+.*?(?:\r?)\n"
    rgx_sysin_single_line       =re.compile(pattern_sysin_single_line,
                                    flags=(re.DOTALL|re.MULTILINE))
    match_sysin_single_line     =rgx_sysin_single_line.search(edited_lines)
    while(match_sysin_single_line):
        edited_lines            =rgx_sysin_single_line.sub(r"",edited_lines)
        match_sysin_single_line =rgx_sysin_single_line.search(edited_lines)
    return edited_lines


b=delete_jcl_sysin_and_following_lines_starting_with_whitespaces("%INCLUDE",a)
print(b)

