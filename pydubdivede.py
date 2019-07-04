#coding:utf-8
import os
import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence
filename = sys.argv[1]
newfilename = sys.argv[2]
for file in os.listdir(filename):
    if 'wav' in file:
        pathname = filename + '/' + file
        sound1 = AudioSegment.from_file(pathname, format = 'wav')
        chunks = split_on_silence(sound1, min_silence_len = 360, silence_thresh = -35)
        for i, chunk in enumerate(chunks):
            newpathname = newfilename + '/' + file.replace('.wav', '') + '-' + '{:0>2d}.wav'.format(i)
            if len(chunk) > 500 and len(chunk) < 4000:
                chunk.export(newpathname, format = 'wav')
            elif len(chunk) >= 4000:
                newchunks = split_on_silence(chunk, min_silence_len = 350, silence_thresh = -33)
                for n, newchunk in enumerate(newchunks):
                    newestpathname = newfilename + '/' + file.replace('.wav', '') + '-' + '{:0>2d}{:0>2d}.wav'.format(i, n)
                    if len(newchunk) > 500 and len(newchunk) < 4000:
                        newchunk.export(newestpathname, format = 'wav')
                    elif len(newchunk)>= 4000:
                        newstchunks = split_on_silence(newchunk, min_silence_len = 300, silence_thresh = -31)
                        for m, newstchunk in enumerate(newstchunks):
                            newestnewpathname = newfilename + '/' + file.replace('.wav', '') + '-' + '{:0>2d}{:0>2d}{:0>2d}.wav'.format(i, n, m)
                            newstchunk.export(newestnewpathname, format = 'wav')
                    else:
                        print('abandon chunk {}'.format(newestpathname))
            else:
                print('abandon chunk {}'.format(newpathname))

