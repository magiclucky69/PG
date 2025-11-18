import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    
    #Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    #zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    #pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    #<a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    
    hrefs = []

    # stáhne stránku
    response = requests.get(url)

    # zkontroluje návratový kód
    if response.status_code != 200:
        raise Exception(f"Chyba pri stahovani URL {url}, status code: {response.status_code}")

    # dekóduje obsah stránky (response.content jsou byty)
    content = response.content.decode(response.encoding or "utf-8", errors="ignore")

    # najde všechny odkazy ve tvaru <a ... href="něco" ...>
    # skupinu v závorkách () vrací jen samotné URL v href=""
    hrefs = re.findall(r'<a\s+[^>]*href="([^"]+)"', content)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        # vypiš nalezené odkazy po jednom na řádek
        for h in hrefs:
            print(h)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")