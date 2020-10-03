def solution(s):
    for i in range(1, len(s)+1):
        if check(s, i):
            return int(len(s)/i)
            
def check(s, x):
    for i in range(len(s)):
        if (s[i] == s[(i+x)%len(s)]):
            pass
        else:
            return False
    return True
