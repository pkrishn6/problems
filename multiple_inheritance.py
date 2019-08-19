class B:
    def __init__(self):
        self.val = 10

class C:
    def __init__(self):
        self.val = 20

class A(C, B):
    pass
    def __repr__(self):
        return str(self.val)


if __name__ == "__main__":
    a = A()
    print(type(a))

    print(isinstance(a, A))
    print(isinstance(a, B))
    print(isinstance(a ,C))

    a.val = 50
    print(a)

