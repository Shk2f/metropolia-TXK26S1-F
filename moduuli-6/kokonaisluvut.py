def luvut(luku_lista: list):
    return sum(luku_lista)

luku_lista = []

while True:
    luku = input("Anna luku: ")
    if luku:
        luku_lista.append(int(luku))
    else:
        print(luvut(luku_lista))
        break