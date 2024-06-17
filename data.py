from datetime import datetime, timedelta

import pandas as pd
from requests_cache import CachedSession, SQLiteCache

from consts import CSV, KNMI_COLUMNS, MONTH_COLUMNS, TXT, URL

now = datetime.now()
tonight = datetime(now.year, now.month, now.day) + timedelta(days=1)


def download():
    """Download het bestand van de KNMI-website en sla het op als txt."""

    # Haal de gegevens op van de URL, cache de gegevens voor de rest van de dag
    backend = SQLiteCache(db_path="../data/knmi_cache.sqlite")
    session = CachedSession(expire_after=tonight, backend=backend)
    response = session.get(URL)

    # Als de statuscode 400 of hoger is, werp dan een foutmelding op
    response.raise_for_status()

    # Schrijf de gegevens naar een bestand
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


def load_data():
    """Laad de gegevens uit het CSV-bestand in een pandas DataFrame en maak enkele aanpassingen."""

    # Maak een DataFrame van het CSV-bestand
    df = pd.read_csv(CSV, delimiter=",")

    # Hernoem de kolommen
    df.rename(columns=KNMI_COLUMNS, inplace=True)

    # Van 0.1 °C naar 1°C
    columns = MONTH_COLUMNS + ["Jaargemiddelde"]
    updated_columns = df[columns].map(lambda x: x / 10, na_action="ignore")
    df[columns] = updated_columns

    # Toon de eerste 5 rijen voor een snelle inspectie
    print(df.head(), "\n")

    return df


def get_highest_mean_temp(df):
    """
    Haal de hoogste jaargemiddelde temperatuur op.
    """

    # Haal de hoogste jaargemiddelde temperatuur op
    highest_mean_temp = df["Jaargemiddelde"].max()  # Temperatuur in °C
    index = df["Jaargemiddelde"].idxmax()  # Index van de rij met de hoogste temperatuur
    year = df.at[index, "Jaar"]  # Jaar van de hoogste temperatuur

    print(f"Hoogste jaargemiddelde: {highest_mean_temp}°C")
    print(f"Dit was in jaar: {year}")

    return highest_mean_temp, year
