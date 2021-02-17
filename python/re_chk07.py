import re
a="""
//SYSUT4   DD DISP=SHR,DSN=OR&USER..HISEXT.B&BRCH..RPTFILE.F000000010   
//SYSUT5   DD DISP=(NEW,CATLG),DSN=OR&USER..HISEXT.B&BRCH..RPTF.F0000001 
//SYSUT6   DD DSN=OR&USER..HISEXT.B&BRCH..RPTFILE,DISP=SHR               
//SYSIN    DD DUMMY                                                      
//SYSUT7   DD DSN=OR&USER..HISEXT.B&BRCH..RPTFIL,DISP=(,CATLG,DELETE),   
//            UNIT=DISK,SPACE=(CYL,(50,50))                              
//*                                                                      
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
        #                 72                             -       \
        #                 match_dsn_line.start(2)      -       \
        #                 len(match_dsn_line.group(2).rstrip())
        white_space_buffer= 72 - \
                            (match_dsn_line.start(2)-match_dsn_line.start(0)) - \
                            len(match_dsn_line.group(2).rstrip())
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
    return b


b=split_long_lines_with_dsn_for_reg_parm_insertion(a)
print(b)



    # print("WhiteSpaceBuffer:{}".format(white_space_buffer))
    #print("\n")
