def bin_to_dec(binarni_cislo):
    # Pokud je vstup int, převede ho na string
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)

    # Kontrola že jde o binární řetězec (složený z 0 a 1)
    for ch in binarni_cislo:
        if ch not in "01":
            raise ValueError("Neplatné binární číslo")

    # převod bin → dec 
    vysledek = 0
    for cifra in binarni_cislo:
        vysledek = vysledek * 2 + int(cifra)

    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128