#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Sept 25 10:03:25 2019

@author Joan Jon Iglesia
"""

# Importing all libraries
import argparse
import sys

# Importing class
from Util import *
from File import *

# Global Vars API
api = 'https://jsonplaceholder.typicode.com'

# Creating a parser
parser = argparse.ArgumentParser(description='Challenge Python.')

# Adding arguments
parser.add_argument('-d', '--data', help='Data to send with request')
parser.add_argument('-o', '--output', help='Output to .json or .csv file (default: dump to stdout)')
parser.add_argument('method', choices=['get', 'post'], help='Request method')
parser.add_argument('endpoint', help='Request endpoint URI fragment')

# Parsing arguments
args = parser.parse_args()
 
#def jsonDefault(object):
#    return object.__dict__

# Create a instance of object Util
util = Util(api)

if args.method == 'get':
	# Call get class method Util 
	response = util.get(args)
else:
	# Call post class method Util
	response = util.post(args)

# Print always the response's HTTP status code
print(response.status_code)

# Exit with an error message and non-zero exit code
if response.status_code < 200 or response.status_code > 299:
    print('An error has occurred.')
    sys.exit(1)


if args.output:
	# If OUTFILE provided
	if len(args.output) >= 5 and args.output[-5:] == '.json':
		# Create a instance of object Json and call write class method
		file = Json(args.output)
		file.write(args.output, response)
	elif len(args.output) >= 4 and args.output[-4:] == '.csv':
		# Create a instance of object Csv and call write class method
		file = Csv(args.output)
		file.write(args.output, response)
	else:
		# If OUTFILE not is .json or .csv print a message error
		print('An error has occurred with output, because the output only .json or .csv.')
		sys.exit(1)
else:
	# If OUTFILE not provided, print response JSON to stdout.
	print(response.text)

