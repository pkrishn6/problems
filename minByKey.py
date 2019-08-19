

class MyDict(dict):
    def __init__(self, *args):
        super(MyDict, self).__init__(args)

    def minByKey(self):
        min_key = min(dict.keys(self), key=lambda k: dict.__getitem__(self, k))
        return dict.__getitem__(self, min_key)


class MyList(list):
    def __init__(self, *args):
        list.__init__(self, args)

    def __getitem__(self, index):
        list.__getitem__(self, index)

    def __setitem__(self, index, val):
        list.__setitem__(self, index, val)

    def __str__(self):
        return list.__str__(self)

    def minByKey(self):
        min_val = min(list(self), key=lambda k:k[1])

        return min_val

class NewDict:
    def __init__(self):
        self.mapping = {}
    def __getitem__(self, key):
        return self.mapping[key]
    def __setitem__(self, key, val):
        self.mapping[key] = val
    def minByKey(self):
        min_key = ""
        count = 0
        for key in self.mapping.keys():
            if not count:
                min_key = key
            else:
                min_key = min(min_key, key)
            count += 1
        if not count:
            raise ValueError("Dict is empty")

        return self.mapping[min_key]


if __name__ == "__main__":
    md = MyDict()
    nd = NewDict()
    md["prasanna"] = "dad"
    md["nila"] = "daughter"
    md["nalini"] = "mom"
    print(md)
    print(md.get("nalini"))

    nd["hi"] = "hello"
    nd["print"] = "paper"
    nd["book"] = "novel"

    # print(nd["hi"])
    # print(nd.minByKey())

    print("md minByKey", md.minByKey())

    ml = MyList()
    # print(ml.minByKey())
    ml.append(("book", 3))
    ml.append(("paper", 2))
    ml.append(("pen", 1))

    print(ml)
    # print(ml.minByKey())


