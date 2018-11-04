def URLify(string, amount):
    string = string[:amount]
    string = string.replace(" ", "%20")
    return string
print(URLify("Mr John Smith      ", 13))
