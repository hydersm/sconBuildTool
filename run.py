import os
import sys
import subprocess

if(sys.argv[1] == '-h' or sys.argv[1] == '--help'):
	help = """Use this python script to easily run built programs. Use syntax:
			python run.py [flavor] [module.programName]"""
	print help
else:
	flavor = sys.argv[1]
	fileName = sys.argv[2]
	filePath = 'build/' + flavor + '/bin/' + fileName
	subprocess.call(filePath)

