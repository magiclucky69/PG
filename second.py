def cislo_na_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět",
                "šest", "sedm", "osm", "devět"]
    teens = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
             "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát",
               "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo < 0 or cislo > 100:
        return "Mimo rozsah (0–100)"
    if cislo < 10:
        return jednotky[cislo]
    if 10 <= cislo < 20:
        return teens[cislo - 10]
    if cislo == 100:
        return "sto"

    d = cislo // 10
    j = cislo % 10

    if j == 0:
        return desitky[d]
    else:
        return desitky[d] + " " + jednotky[j]


# --- test ---
for n in [0, 5, 10, 13, 25, 40, 58, 73, 99, 100]:
    print(f"{n} → {cislo_na_text(n)}")