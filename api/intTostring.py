import sys

def intToString(num):
    num = int(num)
    str_result = ""
    chars = ['A', 'B', 'C', 'D', 'E', 'F']
    while num:
        r = num % 16
        val = str(r) if r <= 9 else chars[r - 10]
        str_result += val
        num = num // 16
    str_result += "X0"
    str_result = str_result[::-1]
    print(str_result)

if __name__ == "__main__":
    intToString(sys.argv[1])

