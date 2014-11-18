import numpy as np

class EstacaoCTD(object):
	"""
	Le e trata dados de CTD da 
	Seabird
	"""
	def __init__(self, filename):
		self.filename = filename
		f = open(filename)
		lines = f.readlines()
		self.TEMP, self.PROF = [], []

		for line in lines:
			# Gravando a latitude
			if "Latitude" in line:
				latG = int(line.split(' ')[4])
				latM = float(line.replace(',', '.').split(' ')[5])
				self.lat = (-1) * (latG + latM / 60)

			# Gravando a longitude		
			if "Longitude" in line:
				lonG = int(line.split(' ')[3])
				lonM = float(line.replace(',', '.').split(' ')[4])
				self.lon = (-1) * (lonG + lonM / 60)

			if "*" not in line and "#" not in line:
				self.PROF.append( -float(line.split()[0]) )
				self.TEMP.append( float(line.split()[1]) )

		self.PROF = np.array(self.PROF)
		self.TEMP = np.array(self.TEMP)


	def remover_subida(self):
		pass


	def bin_average(self):
		pass


	def filter(self):
		pass

	
	def save_filtered_file(self):
		pass











