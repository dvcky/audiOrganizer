import eyed3
import os

artist = "a103"
artistpfx = "a103 - "
mp3count = -103

def countMp3(mp3dir):
    mp3count = 0
    for file in os.listdir(mp3dir):
        if(file.endswith(".mp3")):
            mp3count += 1
    return mp3count

for folder, subs, files in os.walk(os.getcwd()):
    if(folder.count('/') == 4):
        artist = os.path.basename(folder)
        artistpfx = artist + " - "
    if(folder.count('/') == 5):
        zfillnum = len(str(countMp3(folder)))
    for filename in files:
        if(filename.endswith(".mp3")):
            if(filename.startswith(artistpfx)):
                os.rename(os.path.join(folder,filename),os.path.join(folder,filename[len(artistpfx):]))
                filename = filename[len(artistpfx):]
            fileid3 = eyed3.load(os.path.join(folder,filename))
            if(not filename.startswith(str(fileid3.tag.track_num[0]).zfill(zfillnum) + " - ")):
                os.rename(os.path.join(folder,filename),os.path.join(folder,str(fileid3.tag.track_num[0]).zfill(zfillnum) + " - " + filename))
