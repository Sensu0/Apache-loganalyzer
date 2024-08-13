# Copyright (c) 2023 Simon Bränntström, using the MIT License.
# Written by Simon Brännström <simon.brannstrom1@gamil.com>

# Should be noted that the script runs on a single CPU thread. For use in a production environment, the script
# should be preferably be rewritten to support multiple CPU threads in case of log files being of a large file size
# or in the event that the CPU is under heavy load from other processes running on the system. Adding multi-threaded
# functionality will make sure the script is able to complete the execution of various tasks faster.

# Needed modules.
import sys
import re

# General function defining command line arguments. Using a defined "action" argument results in a specific function being called.
# "Action" arguments that are used, but not defined will result in an illegal aciton.
def func_print(filepath, action):
    try:
        with open(filepath, 'r') as file:
            log_entries = file.readlines()

            if action == 'statistics':
                func_statistics(log_entries)
            elif action == 'error':
                func_error(log_entries)
            elif action == 'notice':
                func_notice(log_entries)
            else:
                print(f"Illegal action: '{action}'. Run 'python loganalyzer.py' to see available arguments." '\n\n' "We'll be sending the SWAT team next time to put you in jail for breaking the syntax law!")

# Exception if user provides a path in which the file does not exist.
    except FileNotFoundError:
        print(f"What do you mean '{filepath}'? Consult your memory for the correct path, 'cause it's not in here!")

# Function designed to count the amount of 'error' and 'notice' log entries 
def func_statistics(log_entries):
    # Count begins from 0.
    error_count = 0
    notice_count = 0

# Add +1 to count for each line containing 'error' and 'notice' in separate counts.
    for linje in log_entries:
        if '[error]' in linje.lower():
            error_count += 1
        elif '[notice]' in linje.lower():
            notice_count += 1

# Print the count of the respective amount of entries.
    print(f"errors {error_count}")
    print(f"notice {notice_count}")

# Function designed to print ONLY the date and message or "error" log entries.
def func_error(log_entries):
    for linje in log_entries:
        # Convert string to lowercase using lower() method.
        if 'error' in linje.lower():
            # Using re.search in a varible. By using escape sequence "\", all "[" "]" characters will be removed.
            #"." will match any character except newline ("\n")
            # Need to use "*" and "?" to avoid greedy matching when looking up date.
            # As I understand it, this will match any 0 or 1 characters in the "date" field.
            # The entire "[error]" field will be escaped from output.
            # "(.*)" will match any remaining characters in the line.
            # And finally, it will start looking at the next entry in the line below until all lines has been looked at.
            matchat_textstycke = re.search(r'\[(.*?)\] \[error\] (.*)', linje)
            if matchat_textstycke:
                date = matchat_textstycke.group(1)
                message = matchat_textstycke.group(2)
                print(f"{date} {message}")

# Function designed to print ONLY the date and message or "notice" log entries.
def func_notice(log_entries):
    for linje in log_entries:
        # Same as line 60, but for strings that contain 'notice'
        if 'notice' in linje.lower():
            # re.search works in the same manner as described in line 62-68, except "[notice]" fields will be escaped from
            # output.
            matchat_textstycke = re.search(r'\[(.*?)\] \[notice\] (.*)', linje)
            if matchat_textstycke:
                date = matchat_textstycke.group(1)
                message = matchat_textstycke.group(2)
                print(f"{date} {message}")
# Using pythone built-in variable __name__ cointaing string "__main__", since no additional string variable needs to
# be defined.
if __name__ == "__main__":
    # If you use more or less arguments in the command line than expected
    # (which is 2: filepath and action), instructions on how to run script will be printed. This is using python
    # built-in function "len()" with the array "sys.argv" (which lets script accept command-line arguments)
    # to return printing the string in line 95.
    if len(sys.argv) != 3:
        print("Usage: 'python loganalyzer.py filepath action'. Anything else is fake news propaganda!")
    # Else run the script using the provided filepath and action argument via sys.argv in "func_print" function.
    else:
        filepath = sys.argv[1]
        action = sys.argv[2]
        func_print(filepath, action)
