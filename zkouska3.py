# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`, která spočítá plochu obdelníku (zaokrouhlenou na 1 desetinné místo).
# - `Circle` má atribut `radius` a implementuje metodu `area`, která spočítá plochu kruhu (zaokrouhlenou na 1 desetinné místo).
# - ve třídě `Circle` navíc implementujte metodu `__str__`, která vrátí řetězec ve tvaru `{self.shape_name} with a radius of {self.radius} has an area of {self.area}`.
#
# Vaše řešení můžete otestovat pomocí pytest takto:
# pytest zkouska3.py
# pokud Vám pytest nazahlásí žádné chyby, máte hotovo!
#
# instalace pytest:
# pip install pytest


import math  # potřebujeme pro π (pi) u kruhu

# Základní třída Shape (abstraktní třída)
class Shape:
    def __init__(self, shape_name=None):
        # Konstruktor nastaví název tvaru
        self.shape_name = shape_name
    
    def __str__(self):
        # Defaultní řetězcová reprezentace tvaru
        # Volá metodu area(), která bude přepsaná v podtřídách
        return f'{self.shape_name} shape with area {self.area()}'

    def area(self):
        # Výchozí implementace plochy vrací 0.0
        # Podtřídy by měly tuto metodu přepsat
        return 0.0

# ---------------------------
# Podtřída Rectangle
# ---------------------------
class Rectangle(Shape):
    def __init__(self, width, height):
        # Rectangle má atributy width a height
        super().__init__("Rectangle")  # zavoláme konstruktor Shape a nastavíme název
        self.width = width
        self.height = height

    def area(self):
        # Přepíšeme metodu area: plocha obdélníku = width * height
        return float(self.width * self.height)  # zaokrouhleno na 1 desetinné místo

# ---------------------------
# Podtřída Circle
# ---------------------------
class Circle(Shape):
    def __init__(self, radius):
        # Circle má atribut radius
        super().__init__("Circle")  # zavoláme konstruktor Shape a nastavíme název
        self.radius = radius

    def area(self):
        # Přepíšeme metodu area: plocha kruhu = π * r^2
        return round(math.pi * self.radius ** 2, 1)  # zaokrouhleno na 1 desetinné místo

    def __str__(self):
        # Přepíšeme __str__ specificky pro kruh
        # Vrátí: "Circle with a radius of {radius} has an area of {area}"
        return f"{self.shape_name} with a radius of {self.radius} has an area of {self.area()}"

# ---------------------------
# Unit testy
# ---------------------------
def test_shapes():
    # Test obdélníku
    rect = Rectangle(4, 5)
    assert rect.area() == 20.0
    assert str(rect) == "Rectangle shape with area 20.0"

    # Test kruhu
    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
    assert str(circle) == "Circle with a radius of 3 has an area of 28.3"

# ---------------------------
# Testování při spuštění souboru
# ---------------------------
if __name__ == "__main__":
    # Test základní třídy
    shape = Shape()
    print(shape)  # "None shape with area 0.0"

    # Test Rectangle
    rect = Rectangle(4, 5)
    print(rect)  # "Rectangle shape with area 20.0"

    # Test Circle
    circle = Circle(3)
    print(circle)  # "Circle with a radius of 3 has an area of 28.3"