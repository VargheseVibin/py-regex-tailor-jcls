import re
step_to_delete_part1=r"(^\/\/\w+\s+EXEC\s+"
step_to_delete_part2=r".*?)(^\/\/\w+\s+EXEC\s+)"


lines_in_jcl="""
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
//**********************************                                
"""
lines_in_jcl="//STEP530 EXEC CPPERMIT,COND=(0,NE),                                    "
lines_in_jcl=" CPPERMIT"
pgm_name="CPPERMIT"
# pgm_pattern_in_jcl=step_to_delete_part1     +               \
#                     pgm_name                 +               \
#                     step_to_delete_part2
# pgm_pattern_in_jcl=repr(pgm_name)
# print("Looking for RegEx pattern:"+pgm_pattern_in_jcl) 
# rgx_jcl_pgm_step=re.compile(pgm_pattern_in_jcl,flags=(re.DOTALL|re.MULTILINE))
# rgx_jcl_pgm_step=re.compile(pgm_pattern_in_jcl)
match_rgx_jcl_pgm_step=re.match(pgm_name,lines_in_jcl)
# match_rgx_jcl_pgm_step=rgx_jcl_pgm_step.match(lines_in_jcl)

if (match_rgx_jcl_pgm_step):
    print("Match Found")
else:
    print("No Match found")