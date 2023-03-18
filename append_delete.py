# https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def appendAndDelete(s, t, k):
    s = s.split()
    t = t.split()
    print(s, t)
    print("******")
    for i, char in enumerate(t):
        print(t[i])
        if k <= 0:
            break
        elif t[i] is None:
            print("i had none")
            continue
        elif char != s[i]:
            s[i] = char
            k = k - 2
        print(s)
        print(t)
        
    if s == t:
        return "Yes"
    else:
        return "No"
print(appendAndDelete("ashley", "ash", 2))