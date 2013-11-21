# !/usr/bin/env python
from TestRunner import *
from ParseScript import *
from TestController import *
from TestController import test_list
one_time_SWITCH="True"

def main():
    print "Main function is now running"
    print "When the main fucntion runs, each line will always be reserved for x number of entries"
    global one_time_SWITCH

    if one_time_SWITCH=="True":
        run = TestController() 
        run.runALL_tests()
        one_time_SWITCH="False"
    else:
        print "Run the script once when the program starts - no more"

def list_tests():
    for each in test_list:
        print each

def report_test_status():#this reports test_status in a debug mode 
    try:
        for i,each in enumerate(test_list):
            print test_list[i].check_testStatus()
    except AttributeError:
        print "Run test first"

def gatherTestInfo(clear):
    clear_list=[]
    for i,each in enumerate(test_list):
        try:
            if test_list[i].check_testStatus()==None:
                test_list[i].gatherINFO("True", i)
            else:
                if clear == "True":
                    pass
                else:
                    test_list[i].gatherINFO("False", i)
                    if i not in clear_list:
                        clear_list.append(i)
                        for each in clear_list:
                            pass    #for debug
        except AttributeError:
            print "Run Test first - this has been initialized by the script, but not ran through main()"

def kill_Processes():
    try:
        for i,each in enumerate(test_list):
            test_list[i].stop_Test() 
        for x in range(5):
            print
    except AttributeError:
        print "You should run a test first"

def stop_Test(input1):
    try:
        run = TestController()
        run.stop_Test(input1)
    except AttributeError:
        print "Run test first"

def add_New_Test(input1):
    run = TestController()
    run.addNEW_Test(input1)
 
def showmenu():
    prompt = """

-------------------------------------------------------------------------------------------------------
Choose one of the following options:

main            //This will run whatever is listed in the text script (once only)
debug           //This will give you a polled return of the app (diff apps return a range of error codes)
kill            //This will kill all devices under test
stop <number>   //Stops the test listed in console
report          //Shows a report history of all instances
clear           //Shows report of what's still running
run <ip> <port> <test_path>   //Runs a single test
list            //Debug info for showing all class instances
quit            //Quit application 

Enter choice: """
    menu_items=['main','debug','kill','report','stop','report','clear','run','list','quit']   
    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = raw_input(prompt)

            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            for i, each in enumerate (menu_items):
                if "stop" or "run" in choice:
                    break
                if choice != each:
                    if i==len(menu_items)-1:
                        print 'invalid menu option, try again'
                        break
            chosen = 1
        if choice == 'quit': done = 1
        if choice == 'main': main()
        if choice == 'debug': report_test_status()
        if choice == 'kill': kill_Processes()
        if "stop" in choice: stop_Test(choice)
        if choice == 'report': gatherTestInfo("False")
        if choice == 'clear': gatherTestInfo("True")
        if "run" in choice: add_New_Test(choice)
        if choice == 'list': list_tests()
            
if __name__ == '__main__':
    showmenu()