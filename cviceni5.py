import requests

def download_rates(url):
    return ""

if __name__ == "__main__":

    url = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

    rates = download_rates(url)

    print(rates)