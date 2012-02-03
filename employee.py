import os
import string
import pprint

class EmployeeConfig:
	baseroot = ''
	jsroot = ''
	cssroot = ''
	outroot = ''
	job = ''

def startjob(job):
	EmployeeConfig.job = job
	print "Executing Job", EmployeeConfig.job, "\n\n"

	EmployeeConfig.baseroot = job['baseroot']
	EmployeeConfig.jsroot = job['jsroot']
	EmployeeConfig.cssroot = job['cssroot']
	EmployeeConfig.outroot = job['outroot']

	for chore in job['chores']:
		workchore(chore)

	return


def workchore(chore):
	print "Working on chore", EmployeeConfig.job, "=>"#, EmployeeConfig.inputs, "\n\n"

	inputs = []
	for fl in EmployeeConfig.job['chores'][chore]:
		inputs.append(EmployeeConfig.baseroot+EmployeeConfig.jsroot+fl)

	yuibin = "./yuicompressor-2.4.7.jar"
	cmd = "java -jar " + yuibin + " -o " + EmployeeConfig.outroot + chore + " " + ' '.join(inputs)


	print "Running command: ", cmd
	os.system(cmd)
	return
