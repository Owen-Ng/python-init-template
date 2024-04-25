def RemoveTrailingNewLine(s):
    if s[0] == "\n":
        s = s[1:]
    if s[-1] == "\n":
        s = s[:-1]
    return s