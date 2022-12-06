with open("input6.txt", 'r') as f:
    lines = f.readlines()
    datastream = lines[0][:-1]
    read = ''
    for i in range(len(datastream)):
        if len(read) == 14:
            read = read[1:]
        read += datastream[i]
        if len(set(read)) == 14:
            print(i+1)
            break