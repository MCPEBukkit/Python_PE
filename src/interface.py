import socket
import src.logging
import sys
import time

class interface:
  
def connection(ip = "0.0.0.0", port = 19132):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  bind = s.bind(ip, port)
  if(!bind):
    logging.warning("Couldn't bind to "+ ip +":"+port)
    time.sleep(5)
    sys.exit("process eliminated.")
