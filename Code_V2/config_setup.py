
def getConfigValue(mode_name,value_name):
    import configparser
    cf = configparser.ConfigParser()
    cf.read("config.ini","utf-8-sig")
    value = cf.get(mode_name, value_name)
    return value