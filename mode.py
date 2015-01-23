import ConfigParser
import sys

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
	help = """Use this script to set the build flavor. Usage:
			python mode.py [flavor]"""
	print help

else:
	flavor = sys.argv[1]
	if flavor in ['debug', 'release']:
		config = ConfigParser.ConfigParser()
		configFile = open('site_scons/config.ini', 'w')
		config.add_section('Environment')
		config.set('Environment', 'flavor', flavor)
		config.write(configFile)
		configFile.close()

	else:
		print "Please specify a correct flavor (debug or release)"