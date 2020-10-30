def solve(s, string):
    n = len(string)
    key = 0
    value = 0

    for i in range(len(string)):
        digit = ord(string[i])-ord('a')+1
        key += digit*(26**(n-i-1))
        
        d = ord(s[i])-ord('a')+1
        value += d*(26**(n-1-i))

    j = n
    i = 0

    while j < len(s):
        digit = ord(s[i])-ord('a')+1
        d = ord(s[j])-ord('a')+1

        value = (value - digit*(26**(n-1)))*26
        value += d

        if value == key:
            if s[i+1:j+1] == string:
                return True

        i += 1
        j += 1

    return False

s = "ccaccaaedba"
string = "dba"
print(solve(s, string))
