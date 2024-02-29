#/usr/bin/python
import time
import os
import sys
import re

ROOT_APP = "H:/Python/development_tool/tool_replace/APP"
print(ROOT_APP)

def find_non_consecutive(sequence):

    if len(sequence) <= 1:
        return

    # Check if each element is greater than the previous one
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] != 1:
            print(f"Non-consecutive number: {sequence[i]}")

def get_all_filename_in_folder():
    list_filename = []
    list_number = []
    entries = os.listdir(ROOT_APP)
    files = [entry for entry in entries if not entry.endswith("/")]

    for file in files:
        file, extension = os.path.splitext(file) # remove ".c"
        list_filename.append(file)
        # Use regular expression to extract the number
        number = int(re.findall(r'\d+', file)[0])
        list_number.append(number)
    
    return list_filename, list_number

def main():
    list_filename, list_number = get_all_filename_in_folder()
    print(list_number)
    find_non_consecutive(list_number)

if __name__ == "__main__":
    main()