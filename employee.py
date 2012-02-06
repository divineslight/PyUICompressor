import os
import string
import pprint

import empjs
import empcss


class Config:
	baseroot = ''
	jsroot = ''
	cssroot = ''
	outroot = ''
	job = ''

def startjob(job):
	Config.job = job
	print "Executing Job", Config.job, "\n\n"

	Config.baseroot = job['baseroot']
	Config.jsroot = job['jsroot']
	Config.cssroot = job['cssroot']
	Config.outroot = job['outroot']

	for chore in job['chores']:
		workchore(chore)

	return


def workchore(chore):
	print "Working on chore", chore, "\n\n"

	fileExtension = os.path.splitext(chore)[1]
	directory = Config.jsroot
	if fileExtension == '.css':
		directory = Config.cssroot

	Config.inputs = []
	for fl in Config.job['chores'][chore]:
		Config.inputs.append(Config.baseroot+directory+fl)

	inputsStr = ' '.join(Config.inputs)
	os.system("cat " + inputsStr + " > temp" + fileExtension)
	inputsStr = "temp"+fileExtension

	yuibin = "./yuicompressor-2.4.7.jar"
	basecmd = "java -jar " + yuibin + " -o " + Config.outroot + chore + " "
	cmd = basecmd + inputsStr

	print "Running command: ", cmd, "\n\n"
	os.system(cmd)
	return
