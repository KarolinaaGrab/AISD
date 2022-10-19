def foo(list):
    return tuple(list)


def foo2():
    i = 0
    templist = []
    while i < 5:
        b = input("Podaj nastepna wartosc.")
        templist.append(b)
        i = i + 1
    return foo(templist)


print(())