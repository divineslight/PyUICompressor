import sys
import os
import json
import employee
from pprint import pprint

print "Initing\n\n"

f = open('./rulebook.json', 'r')

rules_json = f.read()
rules = json.loads(rules_json)

#print "Got following work from rules\n"
#pprint(rules)

#sys.exit(1)

for job in rules:
	print "========== Performing ", job['name']
	employee.startjob(job)


