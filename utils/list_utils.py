# ListToWords convert the list of strings 
# to a list of words.
# Words has alphabet or numbers
# Ex: qwe1, qwe, 123
def ListToWords(ls):
    currentStr = ""
    words = []
    for line in ls:
        for c in line:
            if c != "\n" and c != "\t" and c  != " ":
                currentStr += c
            else:
                if len(currentStr) > 0:
                    words.append(currentStr)
                    currentStr = ""
    if currentStr != "":
        words.append(currentStr)
    return words