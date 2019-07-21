import configparser,os


class Config(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        path = os.getcwd()+r"\config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(path)
    
    
    def getConfigUrl(self):
        
        
        return self.config["Url"]["url"]
    

    