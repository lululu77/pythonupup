#coding:utf-8
import os
import wave
import matplotlib.pyplot as plt
import numpy as np
filename = './test'

#second_silence = AudioSegment.silent(duration=3000)
for root, dirs, files in os.walk(filename):
#print('files:', files)  # 当前路径下所有非目录子文件
    for file in files:
        pathname = filename + '/' + file
        soundpro = wave.open(pathname, 'rb')
        params = soundpro.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        data = soundpro.readframes(nframes)
        #waveData = np.frombuffer(data,dtype=np.int16)
        #waveData = waveData*1.0/(max(abs(waveData)))
        #waveData = np.reshape(waveData,[nframes,nchannels])
        #time = np.arange(0,nframes)*(1.0 / framerate)
        #plt.figure()
        #plt.subplot(5,1,1)
        #plt.plot(time, waveData[:,0])
        #plt.xlabel("Time(s)")
        #plt.ylabel("Amplitude")
        #plt.title("Single channel wavedata"+file.replace('wav',''))
        #plt.grid('on')#标尺，on：有，off:无。
        #plt.savefig("wavedata.png")
        soundpro.close()
#sound.export('./volumeup-3s.wav', format = 'wav')
