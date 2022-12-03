with open("input3.txt", 'r') as f:
    lines = f.readlines()
    priority_sum = 0
    for l in lines:
        items_in_compartment = (len(l) - 1) // 2
        compartment1 = l[0:items_in_compartment]
        compartment2 = l[items_in_compartment:len(l)-1]
        common_char = ord(''.join(set(compartment1).intersection(compartment2)))
        if common_char > 96:
            priority_sum += common_char - 96
        else:
            priority_sum += common_char - 38
            
print(priority_sum)