x = input("Podaj slowo")


def palindrom(arg1):
    i = 0
    while i < (len(arg1) / 2):
        if arg1[i] != arg1[-1-i]:
            return "Nie jest to palindrom"
        i = i + 1
    return "Jest to palindrom"


print(palindrom(x))