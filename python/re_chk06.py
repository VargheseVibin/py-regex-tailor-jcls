import re
a="""
 //ORAHCP32 EXEC PGM=IEBGENER,                                           
 //            COND=(0,NE)                                               
 //SYSPRINT DD SYSOUT=*                                                  
 //SYSUT1   DD DSN=NULLFILE,DCB=(RECFM=FB,LRECL=200,BLKSIZE=23400)       
 //SYSUT1   DD DSN=NULLFILE,DCB=(RECFM=FB,LRECL=200,BLKSIZE=23400),      
 //            DISP=(,CATLG,DELETE),                                     
 //            UNIT=DISK,SPACE=(CYL,(50,50))                             
 //SYSUT2   DD DSN=OR&USER..HISEXT.B&BRCH..RPTFILE,                      
 //            DISP=(,CATLG,DELETE),                                     
 //            UNIT=DISK,SPACE=(CYL,(50,50))                             
 //SYSUT3   DD DISP=SHR,DSN=OR&USER..HISEXT.B&BRCH..RPTFILE.F00001       
//SYSUT4   DD DISP=(NEW,CATLG),DSN=OR&USER..HISEXT.B&BRCH..RPTF.F0000100
//SYSUT3   DD DSN=OR&USER..HISEXT.B&BRCH..RPTFILE,DISP=SHR              
//SYSIN    DD DUMMY                                                     
//*                                                                     
"""

pattern_dsn_line_in_jcl=r"(^\/\/.*?)(,?)(DSN=(.*?))(\s|,|\n|(\r\n))(.*?)$"
regx_dsn_line=re.compile(pattern_dsn_line_in_jcl,flags=re.MULTILINE)

matches_dsn_line=regx_dsn_line.finditer(a)
#https://regex101.com/r/Sz4V0C/1

for match in matches_dsn_line:
    white_space_buffer=     match.start(0)      +       \
                            72                  -       \
                            match.start(7)      -       \
                            len(match.group(7).rstrip())
    print("WhiteSpaceBuffer:{}".format(white_space_buffer))
    dsn_name=match.group(4)
    if (white_space_buffer>=5)      or  \
        (dsn_name=="NULLFILE"):
        continue

    print("G0:"+match.group(0))
    print("G1:"+match.group(1))
    print("G2:"+match.group(2))
    print("G3:"+match.group(3))
    print("G4:"+match.group(4))
    print("G5:"+match.group(5))
    print("G6:"+match.group(6))
    #print("G6:"+match.group(7))


    # print("WhiteSpaceBuffer:{}".format(white_space_buffer))
    #print("\n")
