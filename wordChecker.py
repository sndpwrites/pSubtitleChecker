import glob, os


def countWords(subtitle):
    wordCnt = 0
    with open(subtitle,'r') as f:
        for line in f:
            if line.upper().find("FRIENDS")!=-1 or line.upper().find("FRIEND")!=-1:
                wordCnt+=1
    return wordCnt


def listFiles(filetype):
    for file in glob.glob(filetype):
        wordCnt = countWords(file)
        if wordCnt==0:
            print file+ " : " + wordCnt.__str__()


def remove_dup_files(filetype):
    unique = []
    for file in glob.glob(filetype):
        episode = file[8:16]
        if episode not in unique:
            unique.append(episode)
        else:
            print "Duplicate found for "+ file
            os.remove(file)
    print "Duplicate files found and removed."


def cleanUp(filetype):
    for file in glob.glob(filetype):
        os.remove(file)


print "Initiating counter"
remove_dup_files("*.srt")
remove_dup_files("*.sub")
listFiles("*.srt")
listFiles("*.sub")
cleanUp("*.srt")
cleanUp("*.sub")
print "Done!"