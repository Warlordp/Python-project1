print ("Type filename")
fname = input(str)
#print(fname)
findex = fname.find('.')
#print(findex)
fkey = fname[findex:]
Pystring = ".py"
Txtstring = ".txt"
Pptstring = ".ppt"
Mp4string = ".mp4"
if fkey == Pystring:
    print("Python")
elif fkey == Txtstring:
    print ("Text file")
elif fkey == Pptstring:
    print("Powerpoint")
elif fkey == Mp4string:
    print("MP4")
else:
    print("File not recognized.")