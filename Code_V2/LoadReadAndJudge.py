import random
import config_setup as c_s

def loadlist(filepath):
    with open(filepath,'r',encoding='utf-8-sig') as f:
        rawwordList = f.readlines()
    return rawwordList

def preprocessing(rawword):
    English =[]
    Chinese = []
    for sentence in rawword:
        if "[" in sentence or "/" in sentence or "{" in sentence:
            ind1 = 0
            while sentence[ind1] not in ("[","/","{"):
                ind1+=1
            EnglishWord = sentence[:ind1]
            English.append(EnglishWord.strip().replace('*',''))
            ind2 = len(sentence)-1
            while sentence[ind2] not in ("]","/","}"):
                ind2-=1
            ChineseWord = sentence[ind2+1:]
            Chinese.append(ChineseWord.strip().replace('*',''))
        else:
            continue
    return English,Chinese

def QuestionPrintandJudge(English, Chinese, Mode, queind):

    if Mode == 1:
        print("中文含义：%s" %(Chinese[queind]))
        s = input("英文：%s :" %(English[queind][:2]))
        if s == English[queind]:
            print("Correct")
        else:
            print("Error, ans is %s" %(English[queind]))

    if Mode == 2:
        print("单词: %s" %(English[queind]))
        resls = [Chinese[queind]]
        for i in range(3):
            resls.append(Chinese[(queind+i)%len(Chinese)])
        random.shuffle(resls)
        for i in range(4):
            print("%d : %s" %(i,resls[i]))
        s = int(input())
        if resls[s]==Chinese[queind]:
            print("Correct")
        else:
            print(Chinese[queind])


def LRJ(filepath,Mode):
    rawwordList = loadlist(filepath)
    print("#########print first five raw - sentences##########")
    for i in range(5):
        print(rawwordList[i])
    English,Chinese = preprocessing(rawwordList)
    print("############# We have "+str(len(English))+ " pairs ##############")
    for i in range(5):
        print(English[i],Chinese[i])

    print("############## Mission Start! #######################")
    N = c_s.getConfigValue("Config_LRJ","Question_Num")
    N = int(N)

    N_Start = 0
    dict_path =c_s.getConfigValue("Config_LRJ","dict_path")

    with open(dict_path,'r') as f:
        dict = eval(f.read())

    if filepath in dict:
        N_Start = dict[filepath]

        continue_flag = ""
        while (continue_flag!="Y" and continue_flag!="N"):
            continue_flag = input("Your latest point is %d, do you want to continue? Y/N" %(N_Start))

        if continue_flag=="N":
            N_Start = 0

    for i in range(N):
        QuestionPrintandJudge(English,Chinese,Mode,N_Start+i)

    dict[filepath]=N_Start+N
    with open(dict_path,'w') as f:
        f.write(str(dict))
    print("######### Record has been saved ########")






