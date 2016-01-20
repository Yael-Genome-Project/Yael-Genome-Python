import subprocess, sys, shutil

x = sys.argv[1]
y = "./" + x

src = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/test_runscripts/" + x
dst = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/"

shutil.copy(src, dst)

subprocess.call([y])


# subprocess.call(["sh","/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10", y])
# /groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10: is a directory

#subprocess.call(['./runScript_mouse.sh']) worked!

# print ("works!")