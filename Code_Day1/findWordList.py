import os

def findDictionary(DefaultPath=" "):
    if DefaultPath == " ":
        Curpath = input("---------There is no preset DefaultPath， please input new directory path---------")
    else:
        Curpath  = DefaultPath
    fileList = iter_files(Curpath,[])
    print("------------------- Searching finished -----------------")
    print("There are "+ str(len(fileList)) + " dictionaries in the chosen directory")
    for i in range(len(fileList)):
        print("%d:%s" %(i,fileList[i]))

    indchosen = int(input("请输入对应编号： "))
    while indchosen<0 or indchosen>=len(fileList):
        indchosen = int(input("请输入对应编号： "))
    print("---chosen file is %s --------" %(fileList[indchosen]))
    return fileList[indchosen]


def iter_files(rootDir,List):
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root,file)
            List.append(file_name)
        for dirname in dirs:
            iter_files(dirname,List)
    return List