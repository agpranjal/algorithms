def solve(s, p):
    i = 0
    j = 1
    lps = [0]*len(p)

    while j < len(p):
        if p[i] == p[j]:
            lps[j] = i+1
            j += 1
            i += 1
        else:
            if i == 0:
                j += 1
            else:
                i = lps[i-1]
    
    i = 0
    j = 0

    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if not j:
                i += 1
            else:
                j = lps[j-1]

    if j == len(p):
        return f"Found at {i-j}"
    else:
        return False

    print(lps)

s = "adsgwadsxdsgwadsgz"
p = "xxdsgwadsgz"

print(solve(s, p))
