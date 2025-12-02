def p1():
    sum = 0
    with open("input/day02/in.txt") as f:
        line = f.read().strip()
        rs = line.split(",")
        for r in rs:
            r = r.split("-")
            f = int(r[0])
            l = int(r[1])
            for id in range(f, l+1):
                sid = str(id)
                if len(sid) % 2 == 0 and sid[:len(sid)//2] == sid[len(sid)//2:]:
                    sum += id
    print(sum)

def p2():
    sum = 0
    with open("input/day02/in.txt") as f:
        line = f.read().strip()
        rs = line.split(",")
        for r in rs:
            r = r.split("-")
            f = int(r[0])
            l = int(r[1])
            for id in range(f, l+1):
                sid = str(id)
                for s in range(1, len(sid)//2 + 1):
                    windows = []
                    for i in range(0, len(sid), s):
                        windows.append(sid[i:i+s])

                    if all(window == windows[0] for window in windows):
                        sum += id
                        break
    print(sum)

if __name__ == '__main__':
    p1()
    p2()

