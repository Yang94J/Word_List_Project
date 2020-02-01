import findWordList as fWL
import LoadReadAndJudge as lRG

# This is the main function:
if __name__ == '__main__':

    print("############### WordList directory Loading #################")
    Defaultdirpath = "C:/Users/yang hang/Desktop/10天入门python/WordList"
    filepath = fWL.findDictionary(Defaultdirpath)

    Mode =  int(input("Please input the Mode"))
    lRG.LRJ(filepath,Mode)

    print("############## Finished ###################################")



