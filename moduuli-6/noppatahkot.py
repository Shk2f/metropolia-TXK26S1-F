import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä: "))

while True:
    heitto = heita_noppaa(maksimi)
    print(heitto)
    
    if heitto == maksimi:
        break