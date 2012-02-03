import os
import json
import employee
from pprint import pprint

print "Initing Initing\n\n"

f = open('./rulebook.js', 'r')

rules_json = f.read()
rules = json.loads(rules_json)

print "Got following work from rules\n"
pprint(rules)

for job in rules:
	print "========== Performing ", job
	employee.startjob(rules[job])


