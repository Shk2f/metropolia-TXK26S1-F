def luvut_summa_parilliset(luku_lista: list):
    parilliset = [luku for luku in luku_lista if luku % 2 == 0]
    return sum(parilliset)

luku_lista = []

while True:
    luku = input("Anna luku: ")
    if luku:
        luku_lista.append(int(luku))
    else:
        print(luvut_summa_parilliset(luku_lista))
        break