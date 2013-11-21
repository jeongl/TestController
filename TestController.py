from ParseScript import *
from TestRunner import *
import copy
script=None
test_list=[]
script=ParseScript()
test_list=[TestRunner() for i in range(script.countTest_num()-1)]
# test_list=[TestRunner() for i in range(200)]
testCOUNT = script.countTest_num()-1


class TestController(object):
	def __init__(self):
		print "You have initialized the Test Controller"
	def runALL_tests(self):
		##Create TestRunner instance for each in script file
		script1 = ParseScript()
		self.testNUM = script1.countTest_num()
		self.eachTest = script1.parse_line()
		try:
			for i, each in enumerate(self.eachTest):
				ip = self.eachTest[i][2]
				port = self.eachTest[i][4]
				di_r = self.eachTest[i][6]
				test_list[i].start_test(ip,port,di_r)
		except IndexError:
			pass
	def addNEW_Test(self,choice):
		global testCOUNT
		temp = choice.split(" ")
		if len(temp) !=4:
			print "Check your input format-it should look like this: run 10.112.2.116 4323 c:\\users\\UserName\\desktop\\testSuite"
			return
		else:
			test_list.append(TestRunner()) 
			test_list[testCOUNT].start_test(temp[1],temp[2],temp[3])
			testCOUNT+=1
	def stop_Test(self,choice):
		temp = choice.split(" ")
		print temp
		if len(temp) !=2:
			print "Check your input format-it should look like this: stop <number>"
			return
		else:
			try:
				test_list[int(temp[1])].stop_Test()
			except IndexError:
				print "No such test"