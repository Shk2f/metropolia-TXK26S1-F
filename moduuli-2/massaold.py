leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

yhteensa_luodit = luodit + (naulat * 32) + (leiviskat * 20 * 32)
yhteensa_grammat = yhteensa_luodit * 13.3

kilogrammat = int(yhteensa_grammat // 1000)

grammat = yhteensa_grammat % 1000

print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
