import subprocess, sys, shutil

path = sys.argv[1]

# path = /groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/test_runscripts/runScript_mouse.sh
# which is the variable 

src = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/test_runscripts/"
dst = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/"

shutil.copy(src, dst) #

subprocess.call([path])
