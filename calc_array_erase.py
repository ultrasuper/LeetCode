import sys
from copy import deepcopy

def func(string):
    a = deepcopy(string).sort()
    b = []
    b.append(a[-1])
    a.pop()
    flag = 1
    while a:
        if flag == 1:
            b.insert(0, a[-1])
            a.pop()
        else:
            b.append(a[-1])
            a.pop()
        flag = flag * (-1)
    return b
def calc(l):
    n = len(l)
    total = 0
    while l:
        id = int(n/2)
        if n >= 3:
            if id = 0:
                tmp = l[id]*l[id+1]
            elif id = n-1:
                tmp = l[id]*l[id-1]
            else:
                tmp = l[id]*l[id-1]*l[id+1]
        elif n = 2:
            tmp = l[0]*l[1]
        elif n = 1:
            tmp = l[0]
        total += tmp
        l.pop(id)
    return total
        
if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    origin = []
    for i in range(num):
        value = int(sys.stdin.readline().strip())
        origin.append(value)
    b = func(origin)
    result = calc(b)
    print(result)
    
