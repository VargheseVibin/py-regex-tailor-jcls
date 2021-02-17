import os
import re

inpJclDir="D:/OneDrive - Infosys Limited/6_ResLife/ComponentTailoring/ProdJCL"
outJclDir="D:/OneDrive - Infosys Limited/6_ResLife/ComponentTailoring/OutJCL"

os.chdir(inpJclDir)

pattern_for_step_delete_part1=r"^(\/\/\w+\s+EXEC\s+"
pattern_for_step_delete_part2=r".*?)(^\/\/\w+\s+EXEC\s+)"


"""
    Replace all & with ~ temporarily to avoid any unintended substitutions
    /*--------------------------------------------------------------------*/
    /* TURN SCAN OFF TO AVOID SUBSTITUTION PROBLEMS WITH &                */
    /*--------------------------------------------------------------------*/
"""
def replace_amp_with_tilda(lines_in_jcl):
    return re.sub(r"&",r"~",jclLines)

"""

    This deletes the whole block in JCL seen below. 
    These are WTO steps only meant to be executed for PROD jobs
    /*--------------------------------------------------------------------*/
    /* REMOVE WRITE TO OPERATOR                                           */
    /*--------------------------------------------------------------------*/

    //BAD    EXEC HKWTO,COND=(0,EQ,GOOD)                                       
    //IEFRDER DD *                                                             
    *********************************************                              
    *                                           *                              
    *   CONDITION CODE ERROR IN JOB CP#AI010.   *                              
    *                                           *                              
    *********************************************                              
    /*                                                                         
    //*                                                                        
    //*********************************************************************    
    //*                                                                   *    
    //*   ABEND: CONTROL JOB ABEND CONDITION                              *    
    //*                                                                   *    
    //*********************************************************************    
    //*                                                                        
    //ABEND  EXEC JOBFAIL,COND=ONLY  
"""
def delete_hkwto_steps(lines_in_jcl):
    rgx_hkwto_steps=re.compile(r"^\/\/\w+\s+EXEC\s+HKWTO.*",
                            flags=re.DOTALL|re.MULTILINE)
    return rgx_hkwto_steps.sub(r"",lines_in_jcl)

"""
    This function accepts the name of a program as input and removes the whole
    step in the JCL EXEC'ing it, if it is not commented out
"""
def delete_pgm_in_jcl(pgm_name,lines_in_jcl):
    edited_lines=lines_in_jcl
    pattern_pgm_in_jcl=pattern_for_step_delete_part1     +               \
                       pgm_name                          +               \
                       pattern_for_step_delete_part2
    rgx_jcl_pgm_step=re.compile(pattern_pgm_in_jcl,
                                flags=(re.DOTALL|re.MULTILINE))
    match_rgx_jcl_pgm_step=rgx_jcl_pgm_step.search(lines_in_jcl)
    while(match_rgx_jcl_pgm_step):
        edited_lines=rgx_jcl_pgm_step.sub(r"\2",edited_lines)
        match_rgx_jcl_pgm_step=rgx_jcl_pgm_step.search(edited_lines)
    return edited_lines

"""
    This function accepts a string.
    Removes all lines in JCL staring with the sting together with any subsequent 
    line that that starts with a whitespace.

    Example:
    From ====
    //****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
    %INCLUDE IF (TODAY('LAST FRIDAY OF MONTH LESS 0 WORKDAYS')  +           
            OR TODAY('LAST WORKDAY OF YEAR'))                 +           
            OR TODAY('LAST WORKDAY OF YEAR'))                             
    //****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
    To =====
    //****  RUN LAST FRIDAY LESS 0 WORKDAY                                  
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

"""
    Remove all occurence of the passed string from everywhere in the jcl body
"""
def remove_str_in_jcl_body(str_to_remove,lines_in_jcl):
    edited_lines=re.sub(str_to_remove,"",lines_in_jcl)
    return edited_lines

"""
    This fucntion removes all extra whitespaces between in "DD   DSN="
"""
def remove_extra_spaces_dd_dsn(lines_in_jcl):
    pattern_dd_dsn_in_jcl=r"(\/\/\S+\s+DD)\s+(DSN=)"
    rgx_dd_dsn_in_jcl=re.compile(pattern_dd_dsn_in_jcl)
    edited_lines=rgx_dd_dsn_in_jcl.sub(r"\1 \2",lines_in_jcl)
    return edited_lines

"""
    This function splits jcl lines with "DSN=", when it cannot "house" &REG. into the 
    DS name
"""
def split_long_lines_with_dsn_for_reg_parm_insertion(a):
    pattern_dsn_line_in_jcl=r"(^\/\/.*)(?=DSN=)(DSN=(.*))$"
    regx_dsn_line=re.compile(pattern_dsn_line_in_jcl,flags=re.MULTILINE)
    curr_pos=1
    b=a
    match_dsn_line=regx_dsn_line.search(b,curr_pos)
    #https://regex101.com/r/Sz4V0C/1

    while(match_dsn_line):
        print("Match start from  {} - {}".format(match_dsn_line.start(0),  \
                                                match_dsn_line.end(0)))
        print("DSN Match start from  {} - {}".format(match_dsn_line.start(2),  \
                                                match_dsn_line.end(2)))
        print("Whole Match is :"+match_dsn_line.group(0))
        # white_space_buffer=match_dsn_line.start(0)      +       \
                        # 72                             -       \
                        # match_dsn_line.start(2)      -       \
                        # len(match_dsn_line.group(2).rstrip())
        white_space_buffer= 72 - \
                    (match_dsn_line.start(2)-match_dsn_line.start(0)) - \
                    len(match_dsn_line.group(2).rstrip())
        print("Width:{}".format(len(match_dsn_line.group(2).rstrip())))
        print("WhiteSpaceBuffer:{}".format(white_space_buffer))

        curr_pos=match_dsn_line.end(0)+1
        print("Now searching at"+str(curr_pos))

        if (white_space_buffer>=5)      or  \
            (match_dsn_line.group(3).startswith("NULLFILE")):
            pass
        else:
            dd_half_str     =match_dsn_line.group(1)
            dsn_half_str    =match_dsn_line.group(2)

            match_dsn_half_str_for_coma=re.match(r"(DSN=.*?),(.*)$",dsn_half_str)
            print("Now Matching "+match_dsn_line.group(0))
            leading_coma=","
            trailing_coma=""
            if match_dsn_half_str_for_coma:
                if(dsn_half_str.rstrip().endswith(",")):
                    leading_coma=""
                    trailing_coma=","
                dsn_line_1  =   "\n"            +   \
                                dd_half_str     +   \
                                match_dsn_half_str_for_coma.group(2)
                dsn_line_1=dsn_line_1+(" "*(72-len(dsn_line_1)))
                dsn_line_2  =   "//            "     +  \
                                leading_coma         +  \
                                match_dsn_half_str_for_coma.group(1)    +   \
                                trailing_coma
                dsn_line_2=dsn_line_2+(" "*(72-len(dsn_line_2)))
                b=  b[:match_dsn_line.start(0)-1]     +   \
                    dsn_line_1                          +   \
                    "\n"                                +   \
                    dsn_line_2                          +   \
                    b[match_dsn_line.end(0):]
            else:
                dsn_line_1  =   "\n"            +   \
                                dd_half_str
                dsn_line_1=dsn_line_1+(" "*(72-len(dsn_line_1)))
                dsn_line_2  =   "//            "     +  \
                                dsn_half_str         
                dsn_line_2=dsn_line_2+(" "*(72-len(dsn_line_2)))
                b=  b[:match_dsn_line.start(0)-1]     +   \
                    dsn_line_1                          +   \
                    "\n"                                +   \
                    dsn_line_2                          +   \
                    b[match_dsn_line.end(0):]
        match_dsn_line=regx_dsn_line.search(b,curr_pos)
    #print(b)
    return b


for root, dirs, jcls in os.walk(inpJclDir):
    for jcl in jcls:
        jclLines=open(os.path.join(inpJclDir,jcl),'r').read()
        #print ("JCL {} Lines are :\n{}".format(jcl,jclLines))
        newJclLines=replace_amp_with_tilda(jclLines)
        newJclLines=delete_hkwto_steps(newJclLines)
        newJclLines=delete_pgm_in_jcl(r"CPPERMIT",newJclLines)
        newJclLines=delete_pgm_in_jcl(r"TAPERMIT",newJclLines)
        newJclLines=delete_jcl_sysin_and_following_lines_starting_with_whitespaces("%INCLUDE",newJclLines)
        newJclLines=remove_str_in_jcl_body("~LIB.",newJclLines)
        newJclLines=remove_str_in_jcl_body("~USER.",newJclLines)
        newJclLines=remove_str_in_jcl_body("~ACCPT.",newJclLines)
        newJclLines=remove_str_in_jcl_body("~UACCR.",newJclLines)
        newJclLines=remove_extra_spaces_dd_dsn(newJclLines)
        newJclLines=split_long_lines_with_dsn_for_reg_parm_insertion(newJclLines)

        # print("Modified Lines of JCL are below\n{}".format(newJclLines))

