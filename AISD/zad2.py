#Zad2
#Przygotować funkcję, która przyjmie w parametrach imię i nazwisko, oraz zwróci pierwszą literę imienia i nazwisko połączone kropką. Funkcja powinna również dbać o poprawność wielkich liter. Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.

def zad2(str1, str2):
    str1 = str1.title()
    str2 = str2.title()
    return str1[0] + ". " + str2

print("Podaj imie:")
imie = input()
print("Podaj nazwisko:")
nazw = input()
print(zad2(imie, nazw))