
f = open('blast.txt', 'r')
print(f.read())


def reader(blast):
    with open('blast.txt') as f:
        log = f.read()
        print(log)


if __name__ == '__main__':
    reader('log')
 