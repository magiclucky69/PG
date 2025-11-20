class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"Osoba {self.jmeno} ma {self.vek} let"
    
    def pridej_rok(self):
        self.vek += 1

class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik=1):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f"Student {self.jmeno} ma {self.vek} let a studuje {self.rocnik} rocnik"
    
    def pridej_rok(self):
        super().pridej_rok()
        if self.rocnik < 5:
            self.rocnik +=1
        

class Ucitel(Osoba):
    def __init__(self, jmeno, vek, roky_praxe=0):
        super().__init__(jmeno, vek)
        self.roky_praxe = roky_praxe

    def __str__(self):
        return f"Ucitel {self.jmeno} ma {self.vek} let a ma praxy {self.roky_praxe} let" 
    
    def pridej_roky_praxe(self):
        super().pridej_rok()
        self.roky_praxe += 1 
    
class Udrzbar(Osoba):
    def __str__(self):
        return f"Udrzbar {self.jmeno} ma {self.vek} let"



if __name__ == "__main__":
    student1 = Student("Alice", 19, 2)
    student2 = Student("Bob", 20)
    ucitel = Ucitel("Karel", 25 )
    udrzbar = Udrzbar("Tomas", 55)

    osoby = [student1, ucitel, udrzbar, student2]  #polymorfismus


    print(student1)
    print(student2)
    print(ucitel)
    print(udrzbar)

    for i in range(10):
        for osoba in osoby:
            osoba.pridej_rok()
           
    for osoba in osoby:
        print(osoba)
