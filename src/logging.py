import logging

class logger(object):

def info(self, message):
  logging.info("[INFO] "+message)
  
def warning(self, message):
  logging.warning("[WARNING] "+message)
  
def error(self, message):
  logging.error("[ERROR] "+message)
  
def debug(self, message):
  logging.debug("[DEBUG] "+message)
  
def critical(self, message)
  logging.critical("[CRITICAL] "+message)
  
  logger = logger()
