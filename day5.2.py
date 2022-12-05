import re
with open("input5.txt", 'r') as f:
    lines = f.readlines()
    
    stack = []
    i = 0
    while lines[i][:-1] != '':
        stack.append(lines[i][:-1])
        i += 1
    i += 1
    
    move = []
    for j in range(i, len(lines)):
        move.append( re.split(' from | to ', lines[j][:-1].replace('move ', '')) )
    
    for m in move:
        crates = stack[int(m[1]) - 1][-int(m[0]):]
        stack[int(m[1]) - 1] = stack[int(m[1]) - 1][:-int(m[0])]
        stack[int(m[2]) - 1] += crates
    result = ''
    for s in stack:
        result += s[-1]
    print(result)