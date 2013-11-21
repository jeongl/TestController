import os
class ParseScript(object):
    def __init__ (self):
        print "you have initialized ParseScript"
        self.countTest_num()
    def countTest_num(self):
        count=0
        current_dir=os.getcwd()
        file_open=open("run_tests.txt")
        for each in file_open:
            count+=1
        return count
    def parse_line(self):
        output=[]
        file_open=open("run_tests.txt")
        for each in file_open:
            temp = each.split()
            filter(None, output)
            output.append (temp)
        return output       

if __name__ == '__main__':
    new = ParseScript()
    print new.parse_line()