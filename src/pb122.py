"""
Problem 122 of Project Euler.

https://projecteuler.net/problem=122
"""


def problem122(limit=200):
    gotten = {1}
    x = [(1,)]
    L = [set(x)]
    ans = 0
    for i in range(1, 20):
        lasts = set()
        L.append(set())
        for seq in L[i - 1]:
            for c in seq:
                nextt = seq[-1] + c
                if nextt in gotten or nextt > limit:
                    continue
                lasts.add(nextt)
                s = seq + (nextt,)
                L[i].add(s)
        for x in lasts:
            gotten.add(x)
        ans += i * len(lasts)
    print(ans)
