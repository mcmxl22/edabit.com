def give_me_something(a):
    """
    Write a function that returns the string
    "something" joined with a space and the given parameter a
    """
    something = "something"

    return "{} {}".format(something, a)


print(give_me_something("very bad"))