#funkce zkontroluje, zda je cislo sude nebo liche a vypise "Cislo x je sude" nebo "Cislo x je liche"
def sudy_nebo_lichy(cislo):
    if (cislo) % 2 <1:
        print(f"{cislo} je sude")
    else:
        print(f"{cislo} je liche")
    

if __name__ == "__main__":
        sudy_nebo_lichy(5)
        sudy_nebo_lichy(1000000)
        

        hodnota = input("Zadej cislo: ")
        hodnota = int (hodnota)
        sudy_nebo_lichy(hodnota)