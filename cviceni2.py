def vrat_treti(seznam):
        if (seznam) >= 3:
            return seznam[2]
        else:
               return None

def prumer(cisla):
       #vrati pocet hodnot v promenne cisla vydeleny jejich poctem
       return sum(cisla) / len(cisla)

def naformatuj_text(student):
       jmeno = student["jmeno"]
       prijimeni = student["prijimeni"]
       vek = student["vek"]
       prumer_znamek = round(prumer(student["znamky"]),2)
       return f"Student: {jmeno} {prijimeni}, Vek: {vek}, Prumer znamek: {prumer_znamek}"


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
        
        seznam2 = [1,2,3]
        #vrat_treti(seznam2)
        print(prumer(seznam))


student = {
       "jmeno": "Jan",
       "prijimeni": "Novak",
       "vek": 22,
       "znamky": [1,2,1,3,1,2,1]
}
student["vek"] += 1
#print (student["znamky"][4])
print (naformatuj_text(student))