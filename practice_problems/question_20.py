# Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Hints: Consider use yield


def itern():
    for x in range(10):
        yield x




def main():
    for y in itern():
        print(y)


if __name__ == '__main__':
    main()