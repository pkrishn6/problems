import sys

def pattern_match(source, pattern):
    def build_kmp(pattern):
        result = [0] * len(pattern)
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                result[j] = i + 1
                i += 1
                j += 1
            else:
                result[j] = 0
                j += 1
        print(result)
        return result

    kmp_array = build_kmp(pattern)
    j = 0
    i = 0
    index = 0
    while i < len(source) and j < len(pattern):
        if source[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j:
                j = kmp_array[j - 1]
            else:
               i += 1
            index = i
        if j == len(pattern):
            return index

    return float("-inf")

if __name__ == "__main__":
    print("args len", len(sys.argv))
    print(pattern_match(sys.argv[1], sys.argv[2]))
