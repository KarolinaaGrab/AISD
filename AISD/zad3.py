rok1 = 20
rok2 = 22
wiek = 20


def rokur(r1, r2, age):
    rok = str(r1) + str(r2)
    rok = int(rok)
    return rok - age


print(rokur(rok1, rok2, wiek))