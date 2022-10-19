liczba1 = 49
liczba2 = 7
liczba3 = 0


def iloraz(num1, num2):
    if num1 > 0 and num2 > 0 and num2 != 0:
        return num1 / num2
    return "Bledne argumenty"


print(iloraz(liczba1, liczba2))
print(iloraz(liczba2, liczba3))