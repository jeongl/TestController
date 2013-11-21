TestController
==============

This utility is a controller for automated tests using the Squish tool from froglogic. 
This utility also serves as a controller for launching multiple .exe applications and monitoring the status.
The included script will launch two instances of notepad and attempt to connect to two squish GUI devices(will fail for sure).

===========================================================================
The squishrunner.exe accepts the following commands to run a test:

squishrunner.exe <ip> <port> <test_suite_directory>

To run this utility, Shell.py should be used as main() and run with all files in the same directory.
===========================================================================

The tool parses an included script (run_tests.txt) and runs all tests in the file. The menu options will be described here.

main - runs all tests included in text script
debug - used to query attached return values from applications
kill - stop all tests
stop - stop one test
report - report status of all tests during session, pass or fail
clear - report only tests that are still running
run - run single device or another application
list - run all test class instances 
quit - exit application

===========================================================================
This tool is capable of running any multiple number of executable applications. The included test script can be modified
to launch an application with the following syntax:

1  -app UserDefinedApp  --port NA    --rundir   C:\\Windows\\system32\\notepad.exe

Similarly, while tests are running, single tests can be run with the following syntax:

run UserDefinedApp NA <path_to_application>
==========================================================================

Lastly - any application can be launched and monitored, but they differ in returning polled status values.
Lines 36 should be modified to update the correct status depending on the application under test.
