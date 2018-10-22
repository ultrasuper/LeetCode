import sys
from copy import deepcopy

def func(string):
    string_list = list(string)
    return_list = []
    for i in range(len(string_list)):
        if i < len(string_list)-1 and (string_list[i] == string_list[i].lower() and string_list[i+1] == string_list[i+1].upper()):
            return_list.append(string_list[i])
            return_list.append("_")
        elif (i > 0 and i < len(string_list)-1) and (string_list[i] == string_list[i].upper() and string_list[i+1] == string_list[i+1].lower()):
            if string_list[i-1] == string_list[i-1].lower():
                return_list.append(string_list[i])
            else:                
                return_list.append("_")
                return_list.append(string_list[i])
        else:
            return_list.append(string_list[i])
    return "".join(return_list)
    
    
if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    li =[]
    for i in range(num):
        line = sys.stdin.readline().strip()
        li.append(func(line).lower())
    for value in li:
        print(value)
