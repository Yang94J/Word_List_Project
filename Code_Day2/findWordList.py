import os

def findDictionary(DefaultPath=" "):
    if DefaultPath == " ":
        Curpath = input("#######There is no preset DefaultPath， please input new directory path######")
    else:
        Curpath  = DefaultPath
    fileList = iter_files(Curpath,[])
    print("################### Searching finished #################")

    while (len(fileList)==0):
        Curpath = input("No available dictionary in the Curpath, pls choose Another directory path")
        fileList = iter_files(Curpath, [])

    if (len(fileList)!=1):
        print("There are "+ str(len(fileList)) + " dictionaries in the chosen directory "+DefaultPath)
    else:
        print("There are "+ str(len(fileList)) + " dictionary in the chosen directory "+DefaultPath)

    for i in range(len(fileList)):
        print("%d:%s" %(i,fileList[i]))

    indchosen = -1
    invalid = False
    while indchosen<0 or indchosen>=len(fileList) or invalid:
        try:
            indchosen = int(input("请输入对应编号： "))
            invalid = False
        except:
            invalid = True

    print("---chosen file is %s --------" %(fileList[indchosen]))
    return fileList[indchosen]


def iter_files(rootDir,List):

    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.normpath("%s\%s" %(root,file))
            List.append(file_name)
        for dirname in dirs:
            iter_files(dirname,List)
    return List