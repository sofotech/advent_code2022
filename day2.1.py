with open("input2.txt", 'r') as f:
    lines = f.readlines()
    total_score = 0
    for l in lines:
        outcome = (ord(l[2]) - ord(l[0])) % 3
        if outcome == 0:
            total_score += ord(l[2]) - 81
        elif outcome == 2:
            total_score += ord(l[2]) - 84
        else:
            total_score += ord(l[2]) - 87
            
print(total_score)