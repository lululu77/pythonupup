#coding:utf-8
import os
from scipy.io import wavfile
import numpy as np
filename = './test'
newfilename = './test2'
#second_silence = AudioSegment.silent(duration=3000)
for root, dirs, files in os.walk(filename):
#print('files:', files)  # 当前路径下所有非目录子文件
    for file in files:
        pathname = filename + '/' + file
        samplerate, musicdata = wavfile.read(pathname)
        left = []
        right = []
        for item in musicdata:
            left.append(item[0])
            right.append(item[1])
        wavfile.write(newfilename + '/left' + file, samplerate, np.array(left))
#wavfile.write('right'+file, samplerate, np.array(right))

