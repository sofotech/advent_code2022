with open("input3.txt", 'r') as f:
    lines = f.readlines()
    priority_sum = 0
    for i in range(0, len(lines), 3):
        common_char = ord(''.join(set(lines[i][:-1]).intersection(lines[i+1][:-1]).intersection(lines[i+2][:-1])))
        if common_char > 96:
            priority_sum += common_char - 96
        else:
            priority_sum += common_char - 38
            
print(priority_sum)