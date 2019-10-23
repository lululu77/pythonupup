#!/bin/bash
cat filelist.txt |while read file
do
mkdir ./tiaocan_dBC/$file
done
