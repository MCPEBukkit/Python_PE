import logging

class logger(object):
	"""docstring for logger"""
	def __init__(self, arg):
		super(logger, self).__init__()
		self.arg = arg

	def info(self, message):
		logging.info("[INFO] "+message)

	def warning(self, message):
		logging.warning("[INFO] "+message)

	def errors(self, message):
		logging.error("[ERROR] "+message)

	def debug(self, message):
		logging.debug("[DEBUG] "+message)

	def critical(self, message):
		logging.critical("[CRITICAL] "+message)

logger = logger()
