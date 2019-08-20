def print_nums():
    for x in range(1, 101):
        if not(x & (x - 1)):
            print("skipping", x)
            continue

        print(x)

if __name__ == "__main__":
    print_nums()
