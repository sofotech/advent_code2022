with open("input2.txt", 'r') as f:
    lines = f.readlines()
    total_score = 0
    for l in lines:
        outcome = ord(l[2]) - 88
        total_score += outcome * 3 + ((outcome + ord(l[0])) % 3) + 1
            
print(total_score)