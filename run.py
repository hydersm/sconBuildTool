import os
import sys
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()

def configSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

if(sys.argv[1] == '-h' or sys.argv[1] == '--help'):
	help = """Use this python script to easily run built programs. Use syntax:
			python run.py [module.programName]"""
	print help
else:
	fileName = sys.argv[1]
	config.read('site_scons/config.ini')
	flavor = configSectionMap('Environment')['flavor']

	filePath = 'build/' + flavor + '/bin/' + fileName
	subprocess.call(filePath)

