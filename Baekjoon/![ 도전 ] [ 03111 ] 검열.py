# https://www.acmicpc.net/problem/3111
# A <= 25
# T <= 300,000


word = input()
arr = list(input())
turn = 0
start = 0
end = len(arr)-1
endFlag = False
before = []
after = []
while start < end :
    # print('start : ' + str(start) + '  end : ' + str(end))
    # print(visit)
    if turn % 2 == 0:
        for i in range(start, len(arr)):
            for w in range(len(word)):
                if i + w > end:
                    endFlag = True
                    break

                if arr[i+w] == word[w]:
                    pass
                else:
                    break
            else:
                start = i + len(word)
                for 
                before += arr[:i]
                break
            if endFlag:
                before += arr[start:i+w]
                break
    else:
        for i in range(end - len(word) +1 , -1, -1):
            for w in range(len(word)):
                if i < start:
                    endFlag = True
                    break

                if arr[i+w] == word[w]:
                    pass
                else:
                    break
            else:
                end = i - 1
                for j in range(i+len(word), end+1):
                    after.insert(0,arr[j])
                break
            if endFlag:
                for j in range(start, end+1):
                    after.insert(0,arr[j])
                break       

    if endFlag:
        break
    turn += 1
before += after
print(''.join(before))
