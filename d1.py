def p1():
    password = 0
    dial = 50
    with open("input/day01/in.txt") as f:
        for line in f.readlines():
            line = line.strip()
            num = int(line[1:])
            if line[0] == 'L':
                dial = (dial - num) % 100
            else:
                dial = (dial + num) % 100

            if dial == 0:
                password += 1
    print(password)

def p2():
    password = 0
    dial = 50
    with open("input/day01/in.txt") as f:
        for line in f.readlines():
            line = line.strip()
            num = int(line[1:])
            for n in range(num):
                if line[0] == 'L':
                    dial = (dial - 1) % 100
                else:
                    dial = (dial + 1) % 100
                if dial == 0:
                    password += 1
    print(password)

if __name__ == '__main__':
    p1()
    p2()

