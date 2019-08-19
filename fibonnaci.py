import sys

def fib(num, result):
    for i in range(2, num + 1):
        result[i] = result[i - 1] + result[i - 2]

if __name__ == "__main__":
    print("args len", len(sys.argv))
    num = int(sys.argv[1])
    result = [0] * (num + 1)
    if num > 0:
        result[1] = 1
    fib(num, result)
    print(result[num])


