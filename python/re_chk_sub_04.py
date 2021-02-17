import re

a="""
//STEP530 EXEC XXXXMIT,COND=(0,NE),                                    
//STEP530 EXEC CPPERMIT,COND=(0,NE),                                    
//             MODE=PROD,          * RUN ENVIRONMENT                    
//             LIB=,               * GROUP LIBRARY                      
//             CPTAPE=CPTAPEVM     * GROUP ID ACCESS                    
//*                                                                     
//STEP540 EXEC CPPERMIT,COND=(0,NE),                                    
//             MODE=PROD,          * RUN ENVIRONMENT                    
//             LIB=,               * GROUP LIBRARY                      
//             CPTAPE=CPTAPECV     * GROUP ID ACCESS                    
//*                                                                     
//STEP541 EXEC CPPERMIT,COND=(0,NE),                                    
//             MODE=PROD,          * RUN ENVIRONMENT                    
//             LIB=,               * GROUP LIBRARY                      
//             CPTAPE=CPTAPEVM     * GROUP ID ACCESS                    
//*                                                                     
//STEP550 EXEC TAPERMIT,COND=(0,NE)                                     
//SYSIN DD *                                                            
 PERMIT CPPRODT.UNLD1.DCPCAP1.SAHTSP(0)        ID(CD0PPROD) ACCESS(READ)
 PERMIT CPPRODT.UNLD1.DCPCAP3.SCFTSP(0)        ID(ZF3T)     ACCESS(READ)
//**                                                                    
//STEP555 EXEC TAPERMIT,COND=(0,NE)                                     
//SYSIN DD *                                                            
 PERMIT CPPRODT.UNLD1.DCPCAP3.SCOTSP(0)        ID(DM0PMAIL) ACCESS(READ)
 PERMIT CPPRODT.UNLD1.DCPCAP3.SCOTSP(0)        ID(DM0PPROD) ACCESS(READ)
//CPWP9000 EXEC CPWP9000,                                           
//         DUMPOUT='*',                 * OUTPUT REPORT CLASS       
//         SOUT='*',                    * OUTPUT REPORT CLASS       
//**********************************                                """




rgx_cppermit_steps=re.compile(r"^(\/\/\w+\s+EXEC\s+CPPERMIT.*?)(^\/\/\w+\s+EXEC\s+)",flags=(re.DOTALL|re.MULTILINE))
match_cppermit=rgx_cppermit_steps.search(a)
b=a

while(match_cppermit):
    print("Match Found")
    b=rgx_cppermit_steps.sub(r"\2",b)
    match_cppermit=rgx_cppermit_steps.search(b)
    print(b)



