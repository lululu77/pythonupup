#!/bin/bash
cd leftwakeup
ls | grep -v txt > ../file.txt
cd ../
cat file.txt |while read line
do

cd /Users/liulu/Desktop/leftwakeup/$line/highsnr
ls|grep bicycle|grep wav |xargs -I {} mv {} bicycle
ls|grep cafe|grep wav |xargs -I {} mv {} cafe
ls|grep car|grep wav |xargs -I {} mv {} car
ls|grep mall|grep wav |xargs -I {} mv {} mall
ls|grep office|grep wav |xargs -I {} mv {} office
ls|grep quiet|grep wav |xargs -I {} mv {} quiet
ls|grep roadside|grep wav |xargs -I {} mv {} roadside
ls|grep subway|grep wav |xargs -I {} mv {} subway
cd /Users/liulu/Desktop/leftwakeup/$line/lowsnr
ls|grep bicycle|grep wav |xargs -I {} mv {} bicycle
ls|grep cafe|grep wav |xargs -I {} mv {} cafe
ls|grep car|grep wav |xargs -I {} mv {} car
ls|grep mall|grep wav |xargs -I {} mv {} mall
ls|grep office|grep wav |xargs -I {} mv {} office
ls|grep quiet|grep wav |xargs -I {} mv {} quiet
ls|grep roadside|grep wav |xargs -I {} mv {} roadside
ls|grep subway|grep wav |xargs -I {} mv {} subway
cd /Users/liulu/Desktop/leftwakeup/$line/midsnr
ls|grep bicycle|grep wav |xargs -I {} mv {} bicycle
ls|grep cafe|grep wav |xargs -I {} mv {} cafe
ls|grep car|grep wav |xargs -I {} mv {} car
ls|grep mall|grep wav |xargs -I {} mv {} mall
ls|grep office|grep wav |xargs -I {} mv {} office
ls|grep quiet|grep wav |xargs -I {} mv {} quiet
ls|grep roadside|grep wav |xargs -I {} mv {} roadside
ls|grep subway|grep wav |xargs -I {} mv {} subway

done
