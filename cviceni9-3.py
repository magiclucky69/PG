from abc import ABC, abstractmethod


class Zamestnanec(ABC):
    def __init__(self, jmeno, zakladni_mzda):
        self.jmeno = jmeno
        self.zakladni_mzda = zakladni_mzda
        self.pocet_odpracovanych_let = 0

    def pridej_rok(self):
        self.pocet_odpracovanych_let += 1

    @abstractmethod
    def vypocitej_mzdu(self):
        # Zakladni mzda + 1000 Kc za kazdy odpracovany rok
        bonus = 1000 * self.pocet_odpracovanych_let
        return self.zakladni_mzda + bonus

    def __str__(self):
        return f"Zamestnanec {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"


# Programator dostava 10% navíc k vypočítané mzdě rodiče
class Programator(Zamestnanec):
    def vypocitej_mzdu(self):
        zaklad = super().vypocitej_mzdu()
        return int(zaklad * 1.10)  # 10 % navíc


# Manazer dostava 1000 Kč za každého podřízeného
class Manazer(Zamestnanec):
    def __init__(self, jmeno, zakladni_mzda, pocet_podrizenych):
        super().__init__(jmeno, zakladni_mzda)
        self.pocet_podrizenych = pocet_podrizenych

    def vypocitej_mzdu(self):
        zaklad = super().vypocitej_mzdu()
        return zaklad + 1000 * self.pocet_podrizenych


if __name__ == "__main__":
    p1 = Programator("Alice", 40000)
    m1 = Manazer("Bob", 50000, 5)

    zamestnanci = [p1, m1]

    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)

    # Přidáme 2 roky praxe
    for zamestnanec in zamestnanci:
        zamestnanec.pridej_rok()
        zamestnanec.pridej_rok()

    print("Po pripocteni odpracovanych let:")
    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)