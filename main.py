
def wc():
    with open("test.txt", "rb") as f:
        print(len(f.read()))


if __name__ == '__main__':
    wc()

