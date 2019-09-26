# -*- coding: utf-8 -*-

"""
Created on Wed Sept 25 11:21:15 2019

@author Joan Jon Iglesia
"""

# Importing all libraries
import json
import csv

# Class

class File:

	def __init__(self, name):
		self.name = name

	def write(self, output, response):
		pass

class Json(File):
	
	# Overwrite method specific for this file
	def write(self, output, response):
		# Opening the file
		with open(output, 'w') as file:
			# Writing to file
			json.dump(response.json(), file, indent=4)

class Csv(File):
	
	# Overwrite method specific for this file
	def write(self, output, response):
		if len(response.json()) > 0:
			# Creating array with fields name
			fields = []
			for key in response.json()[0]:
				fields.append(key)
			# Opening the file
			with open(output, 'w') as file:
				writer = csv.DictWriter(file, fieldnames=fields)
				# Writing header to file
				writer.writeheader()
				# Writing to file
				writer.writerows(response.json())
