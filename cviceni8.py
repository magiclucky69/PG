def nejvetsi(seznam_cisel):
    if not seznam_cisel:   # pokud je seznam prázdný
        return None

    maximum = seznam_cisel[0]   # vezmeme první prvek jako výchozí

    for cislo in seznam_cisel:
        if cislo > maximum:
            maximum = cislo

    return maximum

def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([100, 50, 30, 10]) == 100
    assert nejvetsi([]) == None