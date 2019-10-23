#!/bin/bash
path=ywzn_en_out_dBC
newpath=test_dBC 
cat filelist.txt |while read file
do
cd /Users/liulu/Desktop/tool/$path/$file/
ls > ../$file'list.txt'
cd /Users/liulu/Desktop/tool/$path/
    count=0
    cat $file'list.txt' |while read line
    do
    
    mv /Users/liulu/Desktop/tool/$path/$file/$line /Users/liulu/Desktop/tool/$newpath/$file
    
    if [ $count -eq 300 ]
    then
       break
    fi
    count=`expr $count + 1`
    done

done
