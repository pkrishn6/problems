def sum_of_int(*args):
    sum = 0
    for num in args:
        if not isinstance(num, int):
            raise Exception("sum_of_int does not support", type(num))
        sum += num
    return sum


if __name__ == "__main__":
    print(sum_of_int(1,2,3,4,5,6,"hi"))


