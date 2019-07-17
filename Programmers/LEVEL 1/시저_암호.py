def solution(s, n):
    answer = ''
    for word in s:
        if word != ' ':
            if ord('A') <= ord(word) and ord(word) <= ord('Z'):
                if ord(word) + n > ord('Z'):
                    answer += chr((ord(word)+n) % (ord('Z')+1) + ord('A'))
                else:
                    answer += chr(ord(word)+n)
            elif ord('a') <= ord(word) and ord(word) <= ord('z'):
                if ord(word) + n > ord('z'):
                    answer += chr((ord(word)+n) % (ord('z')+1) + ord('a'))
                else:
                    answer += chr(ord(word)+n)
        else:
            answer += ' '
            
    return answer