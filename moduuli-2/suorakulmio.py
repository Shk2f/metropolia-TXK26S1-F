suorakulmio_kanta = input("Anna suorakulmion kanta: ")
suorakulmio_kanta = float(suorakulmio_kanta)
suorakulmio_korkeus = input("Anna suorakulmion korkeus: ")
suorakulmio_korkeus = float(suorakulmio_korkeus)

pinta_ala = suorakulmio_kanta * suorakulmio_korkeus
piiri = 2 * (suorakulmio_kanta + suorakulmio_korkeus)

print(f"Suorakulmion pinta-ala on {pinta_ala}")
print(f"Suorakulmion piiri on {piiri}")