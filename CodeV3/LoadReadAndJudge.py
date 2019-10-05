import random
import config_setup as c_s
import matplotlib.pyplot as plt

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

def QuestionPrintandJudge(English, Chinese, PrintMode, queind):

    if PrintMode == 1:
        print("中文含义：%s" %(Chinese[queind]))
        s = input("英文：%s :" %(English[queind][:2]))
        if s == English[queind]:
            print("Correct")
            return True
        else:
            print("Error, ans is %s" %(English[queind]))
            return False

    if PrintMode == 2:
        print("单词: %s" %(English[queind]))
        resls = [Chinese[queind]]
        for i in range(1,4):
            resls.append(Chinese[(queind+i)%len(Chinese)])
        random.shuffle(resls)
        for i in range(4):
            print("%d : %s" %(i,resls[i]))

        try:
            s = int(input())
        except:
            print(Chinese[queind])
            return False
        if resls[s]==Chinese[queind]:
            print("Correct")
            return True
        else:
            print(Chinese[queind])
            return False


def new_word_learning(English,Chinese,filepath):
    print("############## Mission Start! #######################")

    N = c_s.getConfigValue("Config_LRJ", "Question_Num")
    N = int(N)

    print("############# You are going to learn ",str(N)," new words in the mission ##########")
    N_Start = 0
    dict_path = c_s.getConfigValue("Config_LRJ", "dict_path")

    with open(dict_path, 'r') as f:
        dict = eval(f.read())

    if filepath in dict:
        N_Start = dict[filepath]

        continue_flag = ""
        while (continue_flag != "Y" and continue_flag != "N"):
            continue_flag = input("Your latest point is %d, do you want to continue? Y/N" % (N_Start))

        if continue_flag == "N":
            N_Start = 0

    Error_wordind = []
    for i in range(N):
        if N_Start + i >= len(English):
            print("You have finished your word_list so far")
            break
        flag = QuestionPrintandJudge(English, Chinese, random.randint(1,2), N_Start + i)
        if not flag:
            Error_wordind.append(N_Start+i)

    error_word_path = c_s.getConfigValue("Config_LRJ", "error_word_path")
    with open(error_word_path, 'r') as f:
        error_info = eval(f.read())
    wordind_set,acc = error_info.get(filepath, [set(), []])
    for tmpind in Error_wordind:
        wordind_set.add(tmpind)
    acc.append(1-len(Error_wordind)/N)
    error_info[filepath]=[wordind_set,acc]
    with open(error_word_path, 'w') as f:
        f.write(str(error_info))
    maxlen = min(len(acc),10)
    plt.plot(acc[-maxlen:])
    plt.show()

    dict[filepath] = N_Start + N
    with open(dict_path, 'w') as f:
        f.write(str(dict))
    print("######### Record has been saved ########")

def error_word_revising(English,Chinese,filepath):
    print("############## Mission Start! #######################")
    N = c_s.getConfigValue("Config_LRJ", "Question_Num")
    N = int(N)
    error_word_path = c_s.getConfigValue("Config_LRJ", "error_word_path")
    with open(error_word_path, 'r') as f:
        error_info = eval(f.read())
    wordind_set,acc = error_info.get(filepath, [set(), []])
    print("So far, you have ", str(len(wordind_set))," in the list")
    NumToLearn = min(N,len(wordind_set))
    tmplist = list(wordind_set)
    random.shuffle(tmplist)
    for i in range(NumToLearn):
        flag = QuestionPrintandJudge(English, Chinese, random.randint(1, 2), tmplist[i])
        if flag:
            wordind_set.remove(tmplist[i])
    print("Your revision is finished.")
    error_info[filepath] = [wordind_set, acc]
    with open(error_word_path, 'w') as f:
        f.write(str(error_info))


def LRJ(filepath,Mode):
    rawwordList = loadlist(filepath)
    print("#########print first five raw - sentences##########")
    for i in range(5):
        print(rawwordList[i])
    English,Chinese = preprocessing(rawwordList)
    print("############# We have "+str(len(English))+ " pairs ##############")
    for i in range(5):
        print(English[i],Chinese[i])

    if Mode==1:
        new_word_learning(English,Chinese,filepath)
    if Mode==2:
        error_word_revising(English,Chinese,filepath)






