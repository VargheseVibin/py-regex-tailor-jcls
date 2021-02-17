import re

a="""
//ORAHCP32 EXEC PGM=IEBGENER,                                         
//            COND=(0,NE)                                             
//SYSPRINT DD SYSOUT=*                                                
//SYSUT1   DD DSN=NULLFILE,DCB=(RECFM=FB,LRECL=200,BLKSIZE=23400)     
//SYSU@T2  DD      DSN=OR&USER..HISEXT.B&BRCH..RPTFILE,                    
//            DISP=(,CATLG,DELETE),                                   
//            UNIT=DISK,SPACE=(CYL,(50,50))                           
//SYSIN    DD DUMMY                                                   
//*                                                                   
"""


def remove_extra_spaces_dd_dsn(lines_in_jcl):
    pattern_dd_dsn_in_jcl=r"(\/\/\S+\s+DD)\s+(DSN=)"
    rgx_dd_dsn_in_jcl=re.compile(pattern_dd_dsn_in_jcl)
    edited_lines=rgx_dd_dsn_in_jcl.sub(r"\1 \2",lines_in_jcl)
    return edited_lines


b=a
b=remove_extra_spaces_dd_dsn(a)

print(b)

