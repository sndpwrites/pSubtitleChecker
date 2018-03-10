import glob, os


def countWords(subtitle):
    wordCnt = 0
    with open(subtitle,'r') as f:
        for line in f:
            if line.upper().find("FRIENDS")!=-1 or line.upper().find("FRIEND")!=-1:
                wordCnt+=1
    return wordCnt


def listFiles():
    for file in glob.glob("*.srt"):
        wordCnt = countWords(file)
        if wordCnt==0:
            print file+ " : " + wordCnt.__str__()


def remove_dup_files():
    unique = []
    print "Following duplicate files found and removed."
    for file in glob.glob("*.srt"):
        episode = file[8:16]
        if episode not in unique:
            unique.append(episode)
        else:
            print file
            os.remove(file)


def cleanUp():
    for file in glob.glob("*.srt"):
        os.remove(file)


print "Initiating counter"
remove_dup_files()
listFiles()
cleanUp()