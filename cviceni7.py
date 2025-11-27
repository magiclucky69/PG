class Uzivatel:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.telefon = telefon
        self.email=email

    def __str__(self):
        return f"Uzivatel({self.jmeno}, {self.telefon}, {self.email})"

    @property
    def jmeno(self):
        return self.__jmeno

    @property
    def telefon(self):
       return self.__telefon
    
    @property
    def email(self):
        return self.__email
    
    @telefon.setter
    def telefon(self, hodnota):
        if len(hodnota) != 13 or hodnota[0] != "+" or not hodnota[1:].isnumeric():
            raise Exception(f"Cybny format cisla: {hodnota}")
        self.__telefon = hodnota

    @email.setter
    def email(self, kontrola):
        if "@" not in kontrola or not kontrola.endswith(".cz") or not kontrola.replace("@", "").replace(".","").isalnum():
            raise Exception(f"Chybny format emailu: {kontrola}")
        self.__email = kontrola


if __name__ == "__main__":
    u = Uzivatel("Jan", "+420777545655", "jan@novak.cz")
    print(u.jmeno)

    u.telefon ="+420546845688"
    print(u)

