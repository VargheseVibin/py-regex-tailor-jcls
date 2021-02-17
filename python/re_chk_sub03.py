import re

a="""
LISTDSD 'IBMUSER.*'                                                     00160000
//*********************************************************************
//*
//GOOD   EXEC PGM=IEFBR14,COND=(2,LT)
//*
//*********************************************************************
//*                                                                   *
//*   BAD:  SEND ERROR CONDITION MESSAGES TO OPERATOR                 *
//*                                                                   *
//*********************************************************************
//*
//BAD    EXEC HKWTO,COND=(0,EQ,GOOD)
//IEFRDER DD *
*********************************************
*                                           *
*   CONDITION CODE ERROR IN JOB CP#AI010.   *
*                                           * """

rgx_hkwto_steps=re.compile(r"\/\/\w+\s+EXEC\s+HKWTO.*",re.DOTALL)
b=rgx_hkwto_steps.finditer(a)
for match in b:
    print("Match FOund")
    print(match.group(0))
print(rgx_hkwto_steps.sub(r"",a))

