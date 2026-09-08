lentoasemat = {}

while True:
    valikko = input("Haluatko lisätä lentoaseman (l), hakea lentoasemaa (h) vai lopettaa (tyhjä)? ")
    if valikko == "":
        break
    elif valikko == "l":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
    elif valikko == "h":
        koodi = input("Anna haettavan lentoaseman ICAO-koodi: ")
        if koodi in lentoasemat:
            print(f"Lentoasema {koodi}: {lentoasemat[koodi]}")
        else:
            print("Lentoasemaa ei löytynyt.")