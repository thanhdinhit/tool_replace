#/usr/bin/python
import time
import os
import sys
import re

ROOT_APP = "F:/Working/Programing/Python/development_tool/tool_replace/APP"
print(ROOT_APP)
name_file_default = "ADC_TS_"

def find_non_consecutive(sequence):
    l_index_not_consecutive = 0
    if len(sequence) <= 1:
        return

    # Check if each element is greater than the previous one
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] != 1:
            l_index_not_consecutive = i
            print(f"Non-consecutive number: {sequence[l_index_not_consecutive]}")
            print(l_index_not_consecutive)
            break
    return l_index_not_consecutive

def rename_file(old_filename,new_filename):
    try:
        os.rename(old_filename, new_filename)
        print(f"Successfully renamed '{old_filename}' to '{new_filename}'.")
    except OSError as error:
        print(f"Error renaming file: {error}")
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

def get_new_filename(old_number, new_number):
    print(f"old_number: {old_number}, new_number: {new_number}")
    get_old_number_with_new_format = get_new_number(old_number, count_digits(old_number))
    get_new_number_with_new_format = get_new_number(new_number, count_digits(new_number))
    old_filename = f"{ROOT_APP}/{name_file_default}{get_old_number_with_new_format}.c"
    new_filename = f"{ROOT_APP}/{name_file_default}{get_new_number_with_new_format}.c"
    
    print(old_filename)
    print(new_filename)
    rename_file(old_filename, new_filename)
    # print(old_filename)

def count_digits(number):
    if not isinstance(number, int) or number <= 0:
        return None
    return len(str(number))

def get_new_number(number,count_number):
    if count_number == 1:
        return "00"+ str(number)
    if count_number == 2:
        return "0" + str(number)
    if count_number == 3:
        return str(number)
    
def create_arr_virtual(length_number):
    arr = []
    for i in range(length_number):
        arr.append(i+1)
    return arr
    
def compare_2_arr_and_get_new_filename(arr1_first, arr2_virtual):
    check_diff = 0
    t = 0
    for(i, j) in zip(arr1_first, arr2_virtual):
        if i != j:
            get_new_filename(i,j)
            if t == 0:
                t = 1
                check_diff = 1
        else:
            continue
    return check_diff
def main():
    list_filename, list_number = get_all_filename_in_folder()
    list_number_virtual = list(create_arr_virtual(length_number=len(list_number)))
    get_diff = compare_2_arr_and_get_new_filename(list_number, list_number_virtual)
    print(get_diff)

if __name__ == "__main__":
    main()