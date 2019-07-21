import os,time,logging
path=os.path.dirname(os.getcwd())

class log_message():
	def __init__(self):
		title = u'测试'
		day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
		pad = path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
		print(pad)
		file_dir = pad + '\\logco'
		file = os.path.join(file_dir, (day + '.log'))
		self.logger = logging.Logger(title)
		self.logger.setLevel(logging.INFO)
		self.logfile = logging.FileHandler(file)
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