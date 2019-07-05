fr=open("./phonefilename.txt",'r')
names = fr.readlines()
biaozhu=open("./phonebiaozhu.txt",'r')
content = biaozhu.readlines()
fw=open("asr.mlf","w")
fw.write("#!MLF!#\n")
count=0
for name in names:
    name = name.replace('.wav', '.lab"')
    fw.write('"*/{}'.format(name))
    text = content[count].replace('\n', '')
    n = 0
    chindex = 0
    strlength = len(text)
    for ch in text:
	if ch >= 'A' and ch <= 'Z':
	    fw.write(ch)
	    if  text[chindex+1] < 'A' or text[chindex+1] > 'Z':
		fw.write('\n')
	elif ch == ' ':
	    print('space')
        else:
	    if n % 3 == 0:
        	wtxt = text[chindex:chindex+3]
		new = wtxt.replace('\n', '').replace('\t', '').replace('\r', '')
		fw.write(new)
		if (chindex+3) < strlength:
		    fw.write('\n')
	    n += 1
	chindex += 1        
    fw.write(".\n")
    count+=1
fr.close()
biaozhu.close()
fw.close()
