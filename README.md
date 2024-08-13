# Apache-loganalyzer
This script was made as part of school assignment to analyze logfiles from Apache. Python 3.11 was being used for development at the time when this script was made and we received a sample logfile which is attached as part of this repository.

When running the script without any arguments you will get the following message:
"Usage: 'python loganalyzer.py filepath action'.", in which 'filepath' refers to the filepath of the log file and 'action' referring to the different commandline arguments you can use when running this script.

The script supports the following arguments

statistics

This provides a count of the amount of errors and notices which are present in the logfile.

error

This outputs all the error messages present in the logfile.

notice

This outputs all the notices present in the logfile.
