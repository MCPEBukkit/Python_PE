import socket
from src.logging import logger
import sys
import time

class interface(object):
	"""docstring for interface"""
	def __init__(self, arg):
		super(interface, self).__init__()
		self.arg = arg

	def connection(ip = "0.0.0.0", port = 19132):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bind = s.bind(ip, port)
		    if not bind:
		    	logger.warning("Couldn't bind to "+ ip +":"+port)
		    	time.sleep(5)
		    	sys.exit(0)
