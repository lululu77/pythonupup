#!/bin/bash
cat filelist.txt |while read file
do
matlab -nodesktop -nosplash -r "wordname='$file';main_speech;quit"
done
