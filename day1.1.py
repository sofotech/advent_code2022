with open("input1.txt", 'r') as f:
    lines = f.readlines()
    m = 0
    c = 0
    for l in lines:
        if l.strip():
            c = c + int(l)
        elif m < c:
            m = c
            c = 0
        else:
            c = 0
            
print(m)