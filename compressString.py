def compressString(unCompressed):
    charIter = 1
    compressedString = ''

    #checks each char against each other
    for char in range(1, len(unCompressed)):
        if unCompressed[char-1] == unCompressed[char]:
            charIter += 1
        else:
            compressedString += unCompressed[char-1] + str(charIter)
            charIter = 1
    compressedString += unCompressed[char] + str(charIter)

    #prints the smaller of the two strings
    if len(compressedString) >= len(unCompressed):
        return unCompressed
    else:
        return compressedString

print(compressString('aaabbccddddddddd'))
