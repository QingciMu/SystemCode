import os.path


def getFileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = int(round(fsize /1024))
    return fsize