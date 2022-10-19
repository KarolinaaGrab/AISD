def petla():
    a = 0
    while a != 100:
        print("Aktualna liczba: " + str(a))
        b = input("Podaj nastepna liczbe.")
        a = a + int(b)
    return "Osiagnieto liczbe 100"


print(petla())
