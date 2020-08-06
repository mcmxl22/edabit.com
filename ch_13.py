def stutter(word):
    """
    Stuttering Function
    """
    letters = word[0:2]
    stutter = "{}... {}... {}?".format(letters, letters, word)
    return stutter


print(stutter("word"))
