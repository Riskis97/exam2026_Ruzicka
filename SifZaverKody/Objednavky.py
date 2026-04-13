import csv

def zpracuj_csv(soubor):
    objednavky = {}

    with open(soubor, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                cislo = (row.get('cislo_objednavky') or '').strip()
                zakaznik = (row.get('zakaznik') or '').strip()
                nazev = (row.get('nazev_polozky') or '').strip()
                
            
                mnozstvi = int(row.get('mnozstvi', 0))
                cena = int(row.get('cena_za_kus', 0))
                
                
                zaplaceno_raw = (row.get('zaplaceno') or '').strip().lower()
                if zaplaceno_raw != 'true':
                    continue

    
                if not cislo or not zakaznik or not nazev or mnozstvi <= 0 or cena <= 0:
                    continue

               
                if cislo not in objednavky:
                    objednavky[cislo] = {
                        'cislo': cislo,
                        'zakaznik': zakaznik,
                        'pocet_polozek': 0,
                        'celkem': 0
                    }

              
                objednavky[cislo]['pocet_polozek'] += mnozstvi
                objednavky[cislo]['celkem'] += mnozstvi * cena

            except (ValueError, TypeError):
                
                continue

    
    vysledek = list(objednavky.values())

 
    vysledek.sort(
        key=lambda o: (-o['celkem'], -o['pocet_polozek'], int(o['cislo']))
    )

    return vysledek


zpracovane = zpracuj_csv("complex.csv")

for poradi, o in enumerate(zpracovane, start=1):
    print(
        f"{poradi}. Objednávka {o['cislo']} – {o['zakaznik']} – "
        f"Položek: {o['pocet_polozek']} – Celkem: {o['celkem']} Kč"
    )