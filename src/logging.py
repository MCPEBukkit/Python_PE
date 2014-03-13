import logging

class logger:

def info(message):
  logging.info("[INFO] "+message)
  
def warning(message):
  logging.warning("[WARNING] "+message)
  
def error(message):
  logging.error("[ERROR] "+message)
  
def debug(message):
  logging.debug("[DEBUG] "+message)
  
def critical(message)
  logging.critical("[CRITICAL] "+message)
