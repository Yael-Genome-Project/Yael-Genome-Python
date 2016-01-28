# -*- coding: utf-8 -*-
import os, shutil

file_path = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/S10/"  # Input where is the location of dir
result = "Result"
myfolders = []  #list of files in folder
        
for root, dirs, files in os.walk(file_path):
    myfolders.extend(files) #add files name into list
    for d in myfolders:
        folder_name = d.rsplit('.',1)[0]    #If file calls abc.txt , so takes abc
        newpath = os.path.join(file_path,folder_name)   
        if not os.path.exists(newpath): #check if folder exists
            os.makedirs(newpath)    #create folder based on the filenames
        file_original_path = os.path.join(file_path,d)
        shutil.copy(file_original_path,newpath) #copy the corresponding files to the folder
        
        
        result_path = os.path.join(file_path,result)   #set result's folder path
        if not os.path.exists(result_path): #check if folder exists
            os.makedirs(result_path)    #create a folder called Result

print ("Part I ok!")

x = sys.argv[1]  # the location of runScript_human.sh or  runScript_mouse.sh, this one really depends on the user
# ex. /groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/test_scripts/runScript_mouse.sh
y = sys.argv[2]  # the destination of .b2z folder that they want to run the mouse script  or human script
# ex./groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/S10/+myfolder[0] +"/"q

src = "x"
dst = "y"

shutil.copy(src, dst)   # ccopy runScript_mouse.sh/runScript_human.sh from src to dst location

run_script = x[-18 : ]

y=dst+run_script #set shell command

subprocess.call([y])    #run runScript_mouse.sh

run_result_path = dst +result   #the dir of result folder
src_files = os.listdir(dst) #list of files in src folder
for file_name in src_files:
    full_file_name = os.path.join(dst, file_name)
    if (os.path.isfile(full_file_name) and file_name.find("S")==0): #check if file_name's first word is "S" and file_name type is file
        shutil.copy(full_file_name, run_result_path)    #copy file_name to result folder
    if (os.path.isfile(full_file_name) and file_name.find("R")==0): #check if file_name's first word is "R" and file_name type is file
        shutil.rmtree(full_file_name)   #delete file_name

lecseq_path = dst+"/lecseq"  #the dir of lecseq folder
lecseq_new_path = run_result_path + "/lecseq"   #the dir of lecseq folder in result folder
if os.path.exists(lecseq_path): #check if lecseq folder exist
    if not os.path.exists(lecseq_new_path): #check if lecseq folder in result folder exist or not
        os.makedirs(lecseq_new_path)    # if not, create it in result folder
    lecseq_files = os.listdir(lecseq_path)  #list all files in lecseq folder
    for file_name in lecseq_files:  
        full_file_name = os.path.join(lecseq_path, file_name)
        shutil.copy(full_file_name, lecseq_new_path)    #copy files in lecseq folder into /Result/lecseq/ folder
