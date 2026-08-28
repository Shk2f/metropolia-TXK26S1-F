luvut = []

while True:
    luku = input("Anna luku: ")
    if luku:
        luvut.append(int(luku))
    else:
        luvut.sort()
        print(luvut)
        break