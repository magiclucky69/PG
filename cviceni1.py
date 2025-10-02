
def cislo_mensi_nez_3(hodnota):
    if hodnota < 3:
        print(f"Hodnota {hodnota} je mensi nez 3")
    elif hodnota > 3:
        print(f"Hodnota {hodnota} je vetsi nez 3")
    else:
        print(f"Hodnota {hodnota} je rovna 3")



if __name__=="__main__":
    cislo = input("Zadej cislo: ")  #vlozime cislo
    cislo = int(cislo)              #upravime si format cisla
    #cislo *= 3                      #vynasobime cislo
    print(f"Zadane cislo je: {cislo}")    #vypiseme vynasobene cislo


    cislo_mensi_nez_3(1)
    cislo_mensi_nez_3(cislo)