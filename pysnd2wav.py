#coding:utf-8
import struct
import sys
import os
import wave
#from pydub import AudioSegment
paths = str(sys.argv[1])
despaths = str(sys.argv[2])
for root, dirs, files in os.walk(paths):
    for file in files:
        filename = paths+ '/' + file
        #print("filename is {}".format(filename))
        newfilename = despaths + '/' + file.replace('snd', 'wav')
        #print("newfilename is {}".format(newfilename))
        file = open(filename, 'rb')
        newfile = wave.open(newfilename, 'wb')
        file.seek(24,0)
        pos = file.tell()
        snddata = file.read()
        newpos = file.tell()
        sndlen = newpos - pos
        newfile.setnchannels(1)
        newfile.setsampwidth(2)
        newfile.setframerate(16000)
        newfile.writeframes(snddata)
        print("sndlength is {}".format(sndlen))
        file.close()
        newfile.close()
