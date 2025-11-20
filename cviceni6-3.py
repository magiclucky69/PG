class ChybnaSuma(Exception):
    pass

class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def __str__(self):
        return f"Ucet {self.jmeno} ma zustatek: {self.__zustatek} kc"
    
    def vloz(self, suma):
        if suma <= 0:
            raise ChybnaSuma("Nelze vlozit nulovou nebo zapornou sumu")
        self.__zustatek += suma

    def vyber(self, suma):
        if suma <= 0:
            raise ChybnaSuma("Nelze vybrat nulovou nebo zapornou sumu")
        if suma > self.__zustatek:
            raise ChybnaSuma("Nelze vybrat, malo penez na uctu")
        self.__zustatek -= suma 


if __name__ == "__main__":
    try:
        ucet = BankovniUcet("Alice")
        print(ucet)
        ucet.vloz(100)
        print(ucet)
        ucet.vyber(50)
        print(ucet)
    except ChybnaSuma as e:
        print(e)
