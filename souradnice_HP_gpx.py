# načtení souboru hraniční přechody
with open('prechody_DE-AT-CR_uprava.gpx', encoding='utf-8') as vstup:
    obsah = vstup.readlines()

# vytvoření seznamu z obsahu
udaje = [udaj.split("\n") for udaj in obsah]

# vybrání pouze každého 3. řádku, tzn. řádku, který obsahuje souřadnice
seznam_souradnice = [udaje[i] for i in range(0, len(udaje), 3)]

# vytvoření seznamu latitude a longitud jednotlivých HP
hranicni_prechody = []
for udaj in seznam_souradnice:
    latitude = udaj[0][11:20]
    longitude = udaj[0][27:-2]
    souradnice = latitude + ';' + longitude + '\n'
    hranicni_prechody.append(souradnice)

# vložení hlavičky
hlavicka = 'LATITUDE' + ';' + 'LONGITUDE' + '\n'
hranicni_prechody.insert(0, hlavicka)

print(hranicni_prechody)

# uložení do souboru
with open('souradnice_HP.csv', mode='w',encoding='utf-8') as vystup:
    vystup.writelines(hranicni_prechody)