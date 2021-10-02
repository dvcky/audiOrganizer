import eyed3 #INSTALL THIS
import os
import shutil
eyed3.log.setLevel("ERROR")

i = 0
filelist = []
filetypes = (".flac",".mp3",".wav")

folder = input("Drop folder to scan/organize here: ")

#create organized output folder
outDir = os.path.join(folder, "out")
if not os.path.isdir(outDir):
    os.mkdir(outDir)

print("Building array...")
for root, subdirs, files in os.walk(folder):
    for file in files:
        if file.endswith(filetypes):
            filelist.append(os.path.join(root, file))

print("Done! Creating organized library...")
for file in filelist:
    audiofile = eyed3.load(file)

    artistDir = os.path.join(outDir, audiofile.tag.artist)
    albumDir = os.path.join(artistDir, audiofile.tag.album)
    if not os.path.isdir(artistDir):
        os.mkdir(artistDir)
    if not os.path.isdir(albumDir):
        os.mkdir(albumDir)

    numZeros = 2
    if(audiofile.tag.track_num[1]):
        numTracks = audiofile.tag.track_num[1]
        while(numTracks > 99):
            numTracks /= 10
            numZeros += 1
    songFile = os.path.join(albumDir, str(audiofile.tag.track_num[0]).zfill(numZeros) + " - " + audiofile.tag.title + ".mp3")
    if not os.path.isfile(songFile):
        hasImageData = False
        for i in audiofile.tag.images:
            if i:
                hasImageData = True
        if not hasImageData:
            if not os.path.isfile(os.path.join(albumDir, "cover.jpg")) and not os.path.isfile(os.path.join(albumDir, "cover.png")) and not os.path.isfile(os.path.join(albumDir, "folder.jpg")) and not os.path.isfile(os.path.join(albumDir, "folder.png")):
                copyArt = input(file + " - No image data found! Would you like to copy over album art? (y/*): ")
                if copyArt == 'y':
                    print("OK, please copy the image to this folder: " + albumDir)
                    print("Then, rename it to one of these variants: [cover/folder].[jpg/png]")
                    input("Once finished, press any key to continue...")
        shutil.copyfile(file, songFile)
        newFile = eyed3.load(songFile)
print("Done! Checking for albums with multiple artists...")
#for root, subdirs, files in os.walk(outDir):
#    for file in files:
#        if file.endswith(filetypes):
#            filelist.append(os.path.join(root, file))
