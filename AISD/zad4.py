def zad2(str1, str2):
    str1 = str1.title()
    str2 = str2.title()
    return str1[0] + ". " + str2


imie = "Karolina"
nazwisko = "Grabowska"
funkcja = zad2


def zad4(str1, str2, fun):
    return fun(str1, str2)


print(zad4(imie, nazwisko, funkcja))
