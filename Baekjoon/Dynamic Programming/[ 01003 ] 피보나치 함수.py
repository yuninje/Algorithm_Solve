def addList(a, b):
    list_ = []
    list_.append(a[0]+b[0])
    list_.append(a[1]+b[1])
    return list_

T = int(input())
fi = []
fi.append([1,0])
fi.append([0,1])
fi.append([1,1])
for i in range(3,41):
    fi.append(addList(fi[i-1], fi[i-2]))
for test in range(1,T+1):
    problem = int(input())
    print(str(fi[problem][0]) + " "+ str(fi[problem][1]))