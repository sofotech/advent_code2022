with open("input2.txt", 'r') as f:
    lines = f.readlines()
    total_score = 0
    for l in lines:
        outcome = (ord(l[2]) - ord(l[0])) % 3
        total_score += ord(l[2]) - 81 - ((3 - outcome) % 3) * 3
            
print(total_score)