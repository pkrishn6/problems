class check(object):

    def __init__(self):
        self._temperature = 30

    @property
    def temperature(self):
        print("Returning here")
        return self._temperature

    @temperature.setter
    def temperature(self, val):
        print("Setting val")
        if val < 10:
            raise ValueError
        self._temperature = val

    def __str__(self):
        return str(self._temperature)


if __name__ == "__main__":
    c = check()
    print(c.temperature)
    c.temperature = 5
