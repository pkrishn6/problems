def simplifyPath(input):
    if not input:
        return ""

    stack = []
    if input[0] == '/':
        stack.append(input[0])

    for token in input.split('/'):
        if token == "..":
            if stack and stack[-1] == "..":
                stack.append(token)
            elif stack[-1] == "/":
                continue
            else:
                stack.pop()
        elif token != "" and token != ".":
            stack.append(token)

    result = stack[0]
    for i in range(1, len(stack)):
        if i == 1 and result == '/':
            result += stack[i]
        else:
            result += '/' + stack[i]
    return result




