# -*- coding: utf-8 -*-

"""
Created on Wed Sept 25 13:41:45 2019

@author Joan Jon Iglesia
"""

# Importing all libraries
import requests

# Class

class Util:

	def __init__(self, api):
		self.api = api

	# Get data to API
	def get(self, args):
		return requests.get(self.api + args.endpoint)

	# Post virtual data to API
	def post(self, args):
		return requests.post(self.api + args.endpoint, args.data)