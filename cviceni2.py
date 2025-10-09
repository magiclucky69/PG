def vrat_treti(seznam):
        return seznam[2]

if __name__ == "__main__":
        # vytvorime novy seznam (list)
        seznam = [12, 50, 1, 3, 5]
        # vezmeme 3. prvek a vynasobime tremi
        seznam[3] *=3
        # na konec seznamu pripojime hodnotu 100
        seznam.append(100)
        # seznam setridime a otocime poradi prvku
        seznam.sort()
        seznam.reverse()
        
        seznam2 = [1,2]
        treti_prvek = vrat_treti(seznam2)
        print(treti_prvek)