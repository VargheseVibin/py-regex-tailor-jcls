import re

jcl="""
//CRTRACFU JOB ACCT#,'IBMUSER',CLASS=A,MSGCLASS=H,MSGLEVEL=(1,1),       00020000
// NOTIFY=IBMUSER,REGION=0M                                             00060000
//*                                                                     00080000
//STEP01  EXEC PGM=IKJEFT01                                             00100000
//SYSTSPRT DD  SYSOUT=*                                                 00110000
//SYSOUT   DD  SYSOUT=*                                                 00120000
//SYSTSIN  DD  *                                                        00130000
LU IBMUSER                                                              00140000
LG SYS1                                                                 00150000
LISTDSD 'IBMUSER.*'                                                     00160000
//STEP02  EXEC PGM=IKJEFT02                                             00100000
//SYSTSPRT DD  SYSOUT=*                                                 00110000
//SYSOUT   DD  SYSOUT=*                                                 00120000
//SYSTSIN  DD  *                                                        00130000
LU IBMUSER                                                              00140000
LG SYS1                                                                 00150000
LISTDSD 'IBMUSER.*'                                                     00160000
"""

patternExec=re.compile(r"^\/\/\w+\s+EXEC\s+(?:=|PGM=)(\w+)",re.MULTILINE)

matchesExec=patternExec.finditer(jcl)
for match in matchesExec:
    print("Match for {} at {} spanning {}".format(match.group(1),match.start(),match.end()))