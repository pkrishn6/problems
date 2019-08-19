def A():
    a = 10
    b =5
    def B():
        global b
        print(a)
        b = 4
        print(b)
    B()

A()
