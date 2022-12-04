with open("input4.txt", 'r') as f:
    lines = f.readlines()
    result = 0
    for l in lines:
        assignments = l[:-1].split(",")
        elf1 = assignments[0].split("-")
        elf2 = assignments[1].split("-")
        if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]) or int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
            result += 1
            
print(result)