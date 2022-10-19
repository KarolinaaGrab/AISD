x = input("Podaj liczbe dnia")


def foo(arg1):
    dni = ("poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela")
    return dni[int(arg1)-1]


print(foo(x))
