import config_setup as c_s
import findWordList as fWL
import LoadReadAndJudge as lRG

# This is the main function:
if __name__ == '__main__':

    print("############### WordList directory Loading #################")
    Defaultdirpath = c_s.getConfigValue("config_main","Defaultdirpath")
    print("The chosen directory is %s\n" % (Defaultdirpath))
    filepath = fWL.findDictionary(Defaultdirpath)

    Mode = ""
    while Mode!="1" and Mode!="2":
        Mode =  input("Please input the Mode for Word_Helper, Mode1, Mode2 are all available :")

    lRG.LRJ(filepath,int(Mode))

    print("############## Finished ###################################")



