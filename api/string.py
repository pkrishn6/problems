import sys

def patternMatch(source, pattern):
    if not source or not pattern:
        return float("-inf")

    for start in range(len(source)):
        i = start
        for j in range(len(pattern)):
            if source[i] == pattern[j]:
                i += 1
                j += 1
            else:
                break
        if j == len(pattern):
            return start

if __name__ == "__main__":
    print("args len", len(sys.argv))
    print(patternMatch(sys.argv[1], sys.argv[2]))
