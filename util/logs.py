import os,time,logging
path=os.path.dirname(os.getcwd())

class logs():
    def __init__(self,file_name):
        title = u'测试'
        day = time.strftime("%Y%m%d", time.localtime(time.time()))
        pad = path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        print(pad)
        file_dir = pad + '\\report'
        name = file_name+"_"+day + '.log'
        file = os.path.join(file_dir, name)
        # if os.path.exists(file):
        #     os.remove(file)
        self.logger = logging.Logger(title)
        self.logger.setLevel(logging.INFO)
        self.logfile = logging.FileHandler(file,encoding="utf8")
        self.logfile.setLevel(logging.INFO)
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)
    def debugInfo(self, message):
        self.logger.debug(message)
    def info_log(self, message):
        self.logger.info(message)
    def ware_log(self, message):
        self.logger.warn(message)
    def error_log(self, message):
        self.logger.error(message)