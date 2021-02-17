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

def replaceVbFb(matchObj):
    if(matchObj.group(0)=="Vibin"):
        return "Febin"

b=re.sub(r"Vibin",replaceVbFb,a)
print(b)
