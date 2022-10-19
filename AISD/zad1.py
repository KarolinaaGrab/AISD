#Zad1
#Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia, oraz nazwisko, a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski.

imie = "Karolina"
nazwisko = "Grabowska"

def zad1(str1, str2):
    return str1[0] + ". " + str2

print(zad1(imie, nazwisko))