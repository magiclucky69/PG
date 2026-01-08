# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.
#
# Vaše řešení můžete otestovat pomocí pytest takto:
# pytest zkouska2.py
# pokud Vám pytest nazahlásí žádné chyby, máte hotovo!
#
# instalace pytest:
# pip install pytest

import requests

def convert_to_czk(amount, currency):
    #Převádí částku z libovolné měny na české koruny podle aktuálního kurzovního lístku ČNB.

    #param amount: částka v původní měně (float)
    #param currency: kód měny, např. "USD", "EUR" (str)
    #return: částka v CZK zaokrouhlená na 2 desetinná místa
    #raises ValueError: pokud měna není nalezena v kurzovním lístku
    
    # URL s denním kurzovním lístkem
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

    # Stáhneme data z webu
    response = requests.get(url)
    response.raise_for_status()  # vyhodí chybu, pokud se stránka nenačetla

    # Text kurzovního lístku
    data = response.text

    # Rozdělíme data do jednotlivých řádků
    lines = data.splitlines()

    # První dva řádky jsou hlavička a datum, začneme od třetího
    rates = {}
    for line in lines[2:]:
        # Řádek je rozdělen podle "|"
        parts = line.split('|')
        if len(parts) < 5:
            continue  # přeskočíme prázdné nebo nevalidní řádky

        country, currency_name, amount_str, code, rate_str = parts

        # kurz v lístku je napsán s čárkou, převedeme na tečku a pak float
        rate = float(rate_str.replace(',', '.'))
        amount_in_currency = float(amount_str)

        # uložíme kurz v poměru 1 jednotka měny = ? CZK
        rates[code] = rate / amount_in_currency

    # Pokud měna není v seznamu, vyhodíme chybu
    if currency not in rates:
        raise ValueError(f"Currency {currency} not found in the exchange rate list.")

    # Vypočítáme částku v CZK
    czk_amount = amount * rates[currency]

    # Zaokrouhlíme na 2 desetinná místa
    return round(czk_amount, 2)


# Unit testy
from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."

if __name__ == "__main__":
    test_convert_to_czk()