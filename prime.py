import sys

def seive(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while(p * p <= n):
        if prime[p]:
            for i in range(p*p, n + 1, p):
                prime[i] = False

        p += 1


    for i in range(2, n + 1):
        if prime[i]:
            print(i)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise KeyError

    num = int(sys.argv[1])
    seive(num)

