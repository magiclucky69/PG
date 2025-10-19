def je_prvocislo(cislo):
    5
    #Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False
    
    if not isinstance(cislo, int):
        return False
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    limit = int(cislo ** 0.5) + 1
    for i in range(3, limit, 2):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    
    #Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    
    if not isinstance(maximum, int):
        try:
            maximum = int(maximum)
        except ValueError:
            return []
    return [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    try:
        maximum = int(cislo)
    except ValueError:
        print("Neplatny vstup, zadej cele cislo.")
        exit(1)

    # vypis True nebo False
    print(je_prvocislo(maximum))

    # vypis seznamu vsech prvocisel do maxima
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)
