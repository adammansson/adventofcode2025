def base(width):
    with open("input/day03/in.txt") as f:
        sum = 0
        for line in f.readlines():
            line = [int(c) for c in line.strip()]
            found = 0
            i = 0
            for w in range(width - 1, -1, -1):
                for j in range(i, len(line) - w):
                    if line[j] > line[i]:
                        i = j
                found = found * 10 + line[i]
                i = i + 1
            sum += found
    print(sum)

def p1():
    base(2)

def p2():
    base(12)

p1()
p2()

