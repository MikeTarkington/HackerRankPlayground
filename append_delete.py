# https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def appendAndDelete(s, t, k):
    build_str = list(s)
    goal = list(t)
    # print(build_str)
    # print(len(t), len(s), t[:len(s) + 1], s)
    if len(t) > len(s):
        print("t is longer than s and s is equal to the first portion of t")
        for i, char in enumerate(reversed(t), start=1):
            print(t[:-i], ''.join(build_str[:-i]))
            if ''.join(build_str[:-i]) != t[:-i]:
                build_str.pop()
                k = k - 1
                print(k, s)
            elif s == t:
                return "Yes"
                # print(k)

            # if k <= 0 and build_str != t:
            #     return "No"
            # elif k >= 0 and build_str == t:
            #     return "Yes"
    
    elif len(s) > len(t):
        print("s length is greater than t length")
        if len(s) - len(t) > k:
            return "No"
        else:
            for i, char in enumerate(reversed(s), start=1):
                if ''.join(build_str[:-i]) == t and k >= 0:
                    return "Yes"
                if ''.join(build_str[:-i]) != t[:-i]:
                    build_str.pop()
                    k = k - 1
                elif ''.join(build_str[:-i]) == t[:-i] and ''.join(build_str[:-i]) != t:
                    build_str.append(t[-i:])
                    k = k - len(t[-i:])
                    print(k, build_str)

       
            # elif build_str == t:
            #     print("we're done deleting")

# if t is longer than s, may only need to add chars
# if s is longer than t, may only need to remove chars

# iterate in reverse on t and if there are no chars on
# the eqivalent position for s, check if s matches t[:i]
# and keep count of deletions for comparison against k to determine
# whether or not to end the loop and print/return "Yes/No"
# continue deleting until they're a match and then add characters
# back to s/build_str until a match is made to t or the limit of moves
# is reached, whichever happens first



    # s = s.split()
    # t = t.split()
    # print(s, t)
    # print("******")
    # for i, char in enumerate(t):
    #     if k <= 0:
    #         break
    #     elif char != s[i]:
    #         s[i] = char
    #         k = k - 2    
    
    # print(s)
    # print(t)
    
    # if s == t:
    #     return "Yes"
    # else:
    #     return "No"
print(appendAndDelete("ashley", "ash", 2))
print(appendAndDelete("picard", "pickles", 2))