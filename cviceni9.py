def filtruj_cisla(typ, cisla):
    vysledek = []
    for x in cisla:
        if typ == "kladna" and x > 0:
            vysledek.append(x)
        elif typ == "zaporna" and x < 0:
            vysledek.append(x)
        elif typ == "suda" and x % 2 == 0:
            vysledek.append(x)
        elif typ == "licha" and x % 2 != 0:
            vysledek.append(x)
            
        
    return vysledek

if __name__ == "__main__":
    print(filtruj_cisla("kladna", [1, -2, 0, 5, -3]))   # [1, 5]
    print(filtruj_cisla("suda", [1, 2, 3, 4, 5]))       # [2, 4]
    print(filtruj_cisla("zaporna", [1, -2, 0, 5, -3]))   # [-2, -3]
    print(filtruj_cisla("licha", [1, 2, 3, 4, 5]))       # [1, 3, 5]
    # neexistující typ
    print(filtruj_cisla("xxx", [1, 2, 3]))    #[]