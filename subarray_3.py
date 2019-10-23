def subArray(input, sum):
    result = []

    def dfs(node, path, total):
        total += input[node]
        path += str(node)
        if total == sum:
            result.append(path)

        for i in range(node + 1, len(input)):
            dfs(i, path, total)

    for i in range(len(input)):
        tmp_path = ""
        dfs(i, tmp_path, 0)
    print(result)



if __name__ == "__main__":
    input = [6,0,9,7,3,1,4,1,10]
    sum = 15
    subArray(input, sum)



