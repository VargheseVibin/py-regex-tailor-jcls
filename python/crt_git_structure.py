import re
import csv
import os

dsMappingFile="D:\\OneDrive - Infosys Limited\\6_ResLife\\Sydney\\Git Structure\\sydney_mainframe_dataset_mapping.csv"
rootDir=r"D:\\OneDrive - Infosys Limited\\6_ResLife\\Sydney\\Git Structure\reslife-sydney-app"

print("Hello There!")

cblTypeToDirNameMapping = {
    "AMP-BATCH-DB2" : "cob-batch-db2" ,
    "AMP-BATCH-IMSDB" : "cob-batch-imsdb" ,
    "AMP-ONLINE-IMS-DB2" : "cob-imsdc-db2" ,
    "AMP-ONLINE-CICS-DB2" : "cob-cics-db2" ,
    "AMP-ONLINE-IMS-IMSDB" : "cob-imsdc-imsdb" 
}

elTypeToDirNameMpping = {
    "SRCLIB" : "src" ,
    "COPYLIB" : "cobcopy" ,
    "PARMLIB" : "parm" ,
    "PROCLIB" : "proc" ,
    "JCLLIB" : "jcl" ,
    "DBDLIB" : "dbd" ,
    "PSBLIB" : "psb" ,

}

def crt_src_dir(cbl_type,el_type,app_name):
    if (el_type=="SRCLIB"):
        sub_dir=cblTypeToDirNameMapping[cbl_type]
    else:
        sub_dir=elTypeToDirNameMpping[el_type]
    src_dir=os.path.join(rootDir,app_name,sub_dir)
    if not os.path.exists(src_dir):
        print("Creating Directory {}".format(src_dir))
        os.makedirs(src_dir)
    
#https://stackoverflow.com/questions/49543139/csv-reader-picks-up-garbage-in-the-first-few-characters 
#encoding set as utf-8-sig to skip byte order mark at the start of the file.
with open(dsMappingFile,"r", encoding="utf-8-sig") as iFile:
    lines=csv.reader(iFile,delimiter=',')
    for line in lines:
        cblType=line[0]
        elType=line[1]
        endevorDS=line[2]
        pattern=r"EVPROD\.PRODP\.(.*?)\..*"
        appName=re.match(pattern,endevorDS).group(1)
        print("Element Type:{}; SubDir:{}; EndevorDS: {}".format(cblType,elType,appName))
        crt_src_dir(cblType,elType,appName)

