import math
#import time
def pi_rat(limit):
    # j = 2mn
    # i = m^2 - n^2
    # m > n
    ansi = 0
    ansj = 0
    ansk = 0
    result = 99999
    for n in range(1, int(math.sqrt(limit/2)) + 1):
        for m in range(n + 1, limit // (2*n) + 1):
            i = m ** 2 - n ** 2
            j = 2 * m * n
            if i <= limit and abs(max(i, j) / min(i, j) - math.pi) <= result:
                result = abs(max(i, j) / min(i, j) - math.pi)
                ansi = min(i, j)
                ansj = max(i, j)
                ansk = m ** 2 + n ** 2
    return (ansi, ansj, ansk) if ansi else "No Solution"

# tests

assert pi_rat(limit=3) == "No Solution"
assert pi_rat(limit=4) == (3, 4, 5)
assert pi_rat(limit=8) == (6, 8, 10) # (3, 4, 5) and (6, 8, 10) are essentially the same
assert pi_rat(limit=12) == (5, 12, 13)
assert pi_rat(limit=50) == (12, 35, 37)

"""
print(pi_rat(10000)[1] / pi_rat(10000)[0])         # 3.1446360153256707
print(pi_rat(100000)[1] / pi_rat(100000)[0])       # 3.141641569864716
print(pi_rat(1000000)[1] / pi_rat(1000000)[0])     # 3.1415724657660142
print(pi_rat(10000000)[1] / pi_rat(10000000)[0])   # 3.1415935295894255
print(pi_rat(100000000)[1] / pi_rat(100000000)[0]) # 3.141592277510479

tstart = time.time()
print(pi_rat(100000000))
print(time.time() - tstart)
"""