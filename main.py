import requests

URL = "https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/maandgegevens/mndgeg_260_tg.txt"
TXT = "knmi.txt"
CSV = "knmi.csv"


def download():
    """Download het bestand van de KNMI-website en sla het op als txt."""

    response = requests.get(URL)

    # Als de HTTP-code 400 of hoger is, zal er een uitzondering worden opgeworpen
    response.raise_for_status()

    # Sla het bestand op
    with open(TXT, "w", encoding="utf-8") as file:
        file.write(response.text)


def clean_data():
    """
    Lees de ruwe gegevens (txt) in en schoon ze op. Verwijder helptekst,
    spaties en lege regels. Sla op als CSV.
    """

    try:
        # Open de ruwe gegevens
        with open(TXT, "r", encoding="utf-8") as file:
            # Loop over elke regel. Als het de kop is
            # (begint met "STN,YYYY") of de regel begint met 260,
            # dan willen we het houden. Verwijder spaties.
            lines = []
            for line in file:
                # Behoud de kop en de regels met gegevens
                if line.startswith("STN,YYYY") or line.startswith("260"):
                    # Verwijder spaties
                    lines.append(line.replace(" ", ""))

        # Schrijf de opgeschoonde regels naar een nieuw CSV-bestand.
        with open(CSV, "w", encoding="utf-8") as file:
            file.writelines(lines)

    except OSError as e:
        print("Could not open file.", e)


if __name__ == "__main__":
    try:
        download()
    except requests.exceptions.HTTPError as e:
        print("Error while downloading file:", e)

    clean_data()