luvut = []

while True:
    luku = input("Anna luku: ")
    if luku:
        luvut.append(int(luku))
    else:
        luvut.sort(reverse=True)
        print(luvut[:5])
        break