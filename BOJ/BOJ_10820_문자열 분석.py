while True:
    try:
        lowerCount = 0
        upperCount = 0
        numCount = 0
        spaceCount = 0
        mystr = input()
        
        for chr in mystr:
            if chr.isupper():
                upperCount += 1
            elif chr.islower():
                lowerCount += 1
            elif chr.isdigit():
                numCount += 1
            elif chr.isspace():
                spaceCount += 1
        print(f"{lowerCount} {upperCount} {numCount} {spaceCount}")
    except:
        break