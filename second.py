def cislo_text(cislo):
    # Funkce zkonvertuje číslo do jeho textové reprezentace
    # Například: 25 -> "dvacet pět", omezeno na čísla od 0 do 100

    # Seznam pro jednotky (0-9)
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]

    # Seznam pro desítky (20-90)
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    # Speciální čísla 10-19
    specialni = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    # Speciální případ pro číslo 100
    if cislo == 100:
        return "sto"

    # Pokud číslo je menší než 10 (jednotky)
    if cislo < 10:
        return jednotky[cislo]

    # Pokud číslo je mezi 10 a 19 (speciální čísla)
    if cislo < 20:
        return specialni[cislo - 10]

    # Pokud číslo je mezi 20 a 99 (desítky + jednotky)
    desitky_cislo = cislo // 10
    jednotky_cislo = cislo % 10
    if jednotky_cislo == 0:
        return desitky[desitky_cislo]
    else:
        return f"{desitky[desitky_cislo]} {jednotky[jednotky_cislo]}"

# Příklad použití funkce
if __name__ == "__main__":
    cislo = int(input("Zadejte číslo (0-100): "))
    if 0 <= cislo <= 100:
        print(cislo_text(cislo))
    else:
        print("Zadejte číslo mezi 0 a 100.")