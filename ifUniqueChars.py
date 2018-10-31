def ifUniqueChars(string):
    for letter in range(len(string)-1):
        for otherLetter in range(letter+1 ,len(string)):
            if string[letter] == string[otherLetter]:
                return False
    return True


print(ifUniqueChars('qwertyq'))
