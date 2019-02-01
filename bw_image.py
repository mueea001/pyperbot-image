from PIL import Image
import requests
import numpy as np
from pyperbot.wrappers import plugin, cron, unload, onload

@plugin
class bwImage:
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config
		self.count = 0
		if 'count' in config:
			self.count = config['count']
			
	@regex(r'(?:http\:|https\:)?\/\/.*\.(?:png|jpg)')
    def get_image(self, msg, match):
        self.bot.send(msg.reply(gray_image(match)))
		
		
def gray_image(url):
	im = Image.open(requests.get(url, stream=True).raw)

	size = 64, 64

	im = im.convert('L')#.point(lambda x: 0 if x<200 else 255,  '1')
	thum = im.resize(size)#,Image.ANTIALIAS)
	array = np.asarray(thum)
	print(array.shape)
	string = ''
	for i in range(64):
		
		for j in range(64):
			#string = string + str(array[i][j]) 
			''' 
			if array[i][j] == True:
				string = string + ' '
			else:
				string = string + 'x'
			'''
			if array[i][j] <50:
				string = string + '  '
			elif array[i][j] < 150:
				string = string + '::'
			else:
				string = string + '##'
		string = string + '\n'
	return string