import sys, mytimer
reps = 10000
repslist = range(reps)

from math import sqrt
def mathMod():
	for i in repslist:
		res = pow(i)
	return res

def powCall(): 
	for i in repslist:
		res = pow(i, .5)
	return res

def powExpr():
	for i in repslist:
		res = i ** .5
	return res

print(sys.version)
for tester in (mytimer.run_timer, mytimer.best):
	print('<%s>' % tester._name_)
	for test in (mathMod, powCall, powExpr):
		elapsed, result = tester(test)
		print('-'*35)
		print('%s: %.5f => %s' %(test._name_, elapsed, result))
