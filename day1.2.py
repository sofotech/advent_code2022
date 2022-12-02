with open("input1.txt", 'r') as f:
    lines = f.readlines()
    top = []
    c = 0
    for l in lines:
        if l.strip():
            c = c + int(l)
        else:
            top.append(c)
            c = 0
top.sort(reverse=True)
print(top[0]+top[1]+top[2])

