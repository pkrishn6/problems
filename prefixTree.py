
class TreeNode:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

def prefixTree(expr):
    if not expr:
        return None

    ch = expr[0]
    expr = expr[1:]

    node = TreeNode(ch)

    if expr and expr[0] in ["+", "-", "*", "/"]:
        node.left, expr = prefixTree(expr)
    elif expr:
        node.left = TreeNode(expr[0])
        expr = expr[1:]

    if expr and expr[0] in ["+", "-", "*", "/"]:
        node.right, expr = prefixTree(expr)
    elif expr:
        node.right = TreeNode(expr[0])
        expr = expr[1:]

    return node, expr

def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)


if __name__ == "__main__":
    expr = "*-A/BC-/AKL"
    root, _ = prefixTree(expr)
    printTree(root)
