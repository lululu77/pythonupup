#coding:utf-8
import struct
import sys
import os
#from pydub import AudioSegment
paths = str(sys.argv[1])
despaths = str(sys.argv[2])
for root, dirs, files in os.walk(paths):
    for file in files:
        filename = paths+ '/' + file
        #print("filename is {}".format(filename))
        newfilename = despaths + '/' + file.replace('wav', 'snd')
        #print("newfilename is {}".format(newfilename))
        file = open(filename, 'rb')
        newfile = open(newfilename, 'wb')
        file.seek(44,0)
        pos = file.tell()
        wavdata = file.read()
        newpos = file.tell()
        wavlen = newpos - pos
        newfile.write(b'.snd')
        newfile.write(struct.pack('>i',24))
        newfile.write(struct.pack('>i',wavlen))
        newfile.write(struct.pack('>i',3))
        newfile.write(struct.pack('>i',16000))
        newfile.write(struct.pack('>i',1))
        newfile.write(wavdata)
        print("wavlength is {}".format(wavlen))
        file.close()
        newfile.close()
