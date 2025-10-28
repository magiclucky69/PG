def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    #Ověří, zda se figurka může přesunout na danou pozici.
    #param figurka: Slovník s informacemi o figurce (typ, pozice).
    #param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec), číslování 1..8.
    #param obsazene_pozice: Množina obsazených pozic na šachovnici.
    #return: True, pokud je tah možný, jinak False.
    
    typ = figurka.get("typ", "").lower()
    start = figurka.get("pozice")
    if (
        not isinstance(start, tuple) or len(start) != 2
        or not isinstance(cilova_pozice, tuple) or len(cilova_pozice) != 2
    ):
        return False

    r0, c0 = start
    r1, c1 = cilova_pozice

    # 1) hranice šachovnice (1..8)
    if not (1 <= r1 <= 8 and 1 <= c1 <= 8):
        return False

    # 2) cíl musí být volný
    if cilova_pozice in obsazene_pozice:
        return False

    dr = r1 - r0
    dc = c1 - c0
    abs_dr = abs(dr)
    abs_dc = abs(dc)

    def cesta_volna(krok_r, krok_c):
        #Zkontroluje, že na dráze (mimo cíle) nestojí jiná figurka
        r, c = r0 + krok_r, c0 + krok_c
        while (r, c) != (r1, c1):
            if (r, c) in obsazene_pozice:
                return False
            r += krok_r
            c += krok_c
        return True

    # Pravidla figurek
    if typ in ("pěšec", "pesec"):
        # Pěšec jde dopředu (k vyšším řádkům)
        # 1 krok dopředu
        if dc == 0 and dr == 1:
            return True
        # 2 kroky dopředu pouze ze startovního řádku 1 a pokud je cesta volná
        if dc == 0 and dr == 2 and r0 == 1:
            return (r0 + 1, c0) not in obsazene_pozice
        # neřešíme braní šikmo, en passant, ani couvání
        return False

    if typ == "jezdec":
        # L-tvar: (2,1) nebo (1,2)
        return (abs_dr, abs_dc) in {(2, 1), (1, 2)}

    if typ in ("věž", "vez"):
        # Stejný řádek nebo sloupec, cesta musí být volná
        if r0 == r1 and c0 != c1:
            krok_c = 1 if dc > 0 else -1
            return cesta_volna(0, krok_c)
        if c0 == c1 and r0 != r1:
            krok_r = 1 if dr > 0 else -1
            return cesta_volna(krok_r, 0)
        return False

    if typ in ("střelec", "strelec"):
        # Diagonála => |dr| == |dc|, cesta volná
        if abs_dr == abs_dc and abs_dr != 0:
            krok_r = 1 if dr > 0 else -1
            krok_c = 1 if dc > 0 else -1
            return cesta_volna(krok_r, krok_c)
        return False

    if typ in ("dáma", "dama"):
        # Kombinace věže a střelce
        if r0 == r1 and c0 != c1:
            krok_c = 1 if dc > 0 else -1
            return cesta_volna(0, krok_c)
        if c0 == c1 and r0 != r1:
            krok_r = 1 if dr > 0 else -1
            return cesta_volna(krok_r, 0)
        if abs_dr == abs_dc and abs_dr != 0:
            krok_r = 1 if dr > 0 else -1
            krok_c = 1 if dc > 0 else -1
            return cesta_volna(krok_r, krok_c)
        return False

    if typ in ("král", "kral"):
        # O jedno pole libovolným směrem
        return max(abs_dr, abs_dc) == 1

    # Neznámý typ figurky
    return False


# ukázkové testy
if __name__ == "__main__":
    pesec   = {"typ": "pěšec",   "pozice": (2, 2)}
    jezdec  = {"typ": "jezdec",  "pozice": (3, 3)}
    vez     = {"typ": "věž",     "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama    = {"typ": "dáma",    "pozice": (8, 3)}
    kral    = {"typ": "král",    "pozice": (1, 4)}

    # Obsazená pole (nezáleží, jaká figura, jen že je pole obsazené)
    obsazene = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print("Pěšec (2,2) -> (3,2):", je_tah_mozny(pesec, (3, 2), obsazene))  # True
    print("Pěšec (2,2) -> (4,2):", je_tah_mozny(pesec, (4, 2), obsazene))  # False (2 vpřed jen z řádku 1)
    print("Pěšec (2,2) -> (1,2):", je_tah_mozny(pesec, (1, 2), obsazene))  # False (couvání)

    print("Jezdec (3,3) -> (4,4):", je_tah_mozny(jezdec, (4, 4), obsazene))  # False (není L)
    print("Jezdec (3,3) -> (5,4):", je_tah_mozny(jezdec, (5, 4), obsazene))  # False (obsazeno)
    print("Jezdec (3,3) -> (1,2):", je_tah_mozny(jezdec, (1, 2), obsazene))  # True
    print("Jezdec (3,3) -> (9,3):", je_tah_mozny(jezdec, (9, 3), obsazene))  # False (mimo)

    print("Dáma (8,3) -> (8,1):", je_tah_mozny(dama, (8, 1), obsazene))  # False (cesta blokovaná)
    print("Dáma (8,3) -> (1,3):", je_tah_mozny(dama, (1, 3), obsazene))  # False (cesta blokovaná)
    print("Dáma (8,3) -> (3,8):", je_tah_mozny(dama, (3, 8), obsazene))  # True

    print("Král (1,4) -> (2,5):", je_tah_mozny(kral, (2, 5), obsazene))    # True