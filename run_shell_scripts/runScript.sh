#!/bin/bash
#This is just the /groups/bpf-evergrande/liRNAseq_scripts/lirRNAseq_pipeline.sh  script with the directory change commented out
#cd /groups/bpf-evergrande/data/FC_01648/Unaligned_1_PF_mm1/Data/Project_yael

#R libraries taken from /groups/cbdm_lab/dp133/R_libraries
#export R_LIBS="/groups/bpf-evergrande/tools/cbdm_R_libraries/R_libraries"
# Comments: liRNAseq_pipeline_2_human.sh (human) and liRNAseq_pipeline_2_mouse.sh (mouse) - *****Variable
for dir in S* ; do echo $dir ; bsub -q mcore -n 2 -W 480:00 -R "rusage[mem=36000]" -o $dir.liRNAseq.log /groups/immdiv-bioinfo/evergrande/copy_work/yael/liRNAseq_newdpzpipeline/*****Variable $dir $dir; done
