def allcaps(func):
    def wrapper():
        string1 = str(func())
        return string1.upper()
    return wrapper