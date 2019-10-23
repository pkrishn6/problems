class SingleTone:
    __instance = None
    def get_instance(val):
        if not SingleTone.__instance:
            SingleTone.__instance = SingleTone(val)
        return SingleTone.__instance
    def __init__(self, val):
        if SingleTone.__instance is not None:
            raise KeyError
        self.val = val
        SingleTone.__instance = self


a = SingleTone(10)
print(a.val)
print(a)
assert isinstance(a, SingleTone) == True
b = SingleTone(20)
print(b.val)
print(b)



