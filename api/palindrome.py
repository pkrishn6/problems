import sys

def isPalindrome(input):
    if not input:
        return False
    if len(input) == 1:
        return True

    i = 0
    j = len(input) - 1
    while(i < j):
        if input[i].lower() != input[j].lower():
            print("Returning false for", input[i], input[j])
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    print(isPalindrome(sys.argv[1]))
