def comp(txt1, txt2):
    """
    Compare Strings by Count of Characters
    """
    if len(txt1) == len(txt2):
        return True
    else:
        return False


print(comp("txt1", "txt2"))