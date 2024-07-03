import requests
from data import clean_data, download, load_data

if __name__ == "__main__":
    # Download de gegevens
    try:
        download()
    except requests.exceptions.HTTPError as e:
        print("Error while downloading file:", e)

    # Schoon de gegevens op, sla op als CSV
    clean_data()

    # Laad de gegevens in een pandas DataFrame
    df = load_data()

    # Haal kolom 'Jaargemiddelde' op
    # jaargemiddelde = df["Jaargemiddelde"]  # Dit wordt niet aanbevolen
    # jaargemiddelde = df.Jaargemiddelde  # Dit wordt niet aanbevolen
    jaargemiddelde = df.loc[:, "Jaargemiddelde"]
    print(jaargemiddelde)

    # Selecteer meerdere kolommen
    jaargemiddelde = df.loc[:, ["Jaargemiddelde", "Jaar"]]
    print(jaargemiddelde)

    # Selecteer alle maand kolommen
    maanden = df.loc[:, "Januari": "December"]
    print(maanden)

    # Selecteer 'r in de maand'
    selector = maanden.columns.str.contains("r")
    print(selector)

    r_maanden = maanden.loc[:, selector]
    r_maanden = maanden.loc[:, maanden.columns.str.contains("r")]
    print(r_maanden)

    # Selecteer de eerste rij
    eerste_rij = df.loc[0, :]
    print(eerste_rij)

    # Wijzig de index van de rijen naar de jaren
    df.set_index("Jaar", inplace=True)
    print(df.head())

    # Selecteer de eerste rij
    eerste_rij = df.loc[1901, :]
    print(eerste_rij)

    # Selecteer meerdere rijen
    eerste_drie_jaren = df.loc[[1901, 1902, 1903], :]
    print(eerste_drie_jaren)

    # Of met slicing
    eerste_drie_jaren = df.loc[1901:1903, :]
    print(eerste_drie_jaren)

    # Filter rijen waar januari > 0 was
    selectie = df.loc[:, "Januari"] > 0
    januari_boven_0 = df.loc[selectie, :]
    print(januari_boven_0)

    # Als je alle kolommen wilt behouden, kun je het laatste argument weglaten
    eerste_drie_jaren = df.loc[1901:1903]
    print(eerste_drie_jaren)

    # Rijen en kolommen
    q1_80 = df.loc[1980:1990, "Januari": "Maart"]
    print(q1_80)

    boven_10 = df.loc[df.loc[:, "Jaargemiddelde"] > 10, "Jaargemiddelde"]
    print(boven_10)

    # Rijen ophalen met iloc en loc
    eerste_drie_jaren = df.loc[1901:1903]  # Let op: 1903 is inclusief
    eerste_drie_jaren = df.iloc[0:3]  # Let op: 3 is exclusief
    print(eerste_drie_jaren)

    # Waarde ophalen met at
    jan_2020 = df.at[2020, "Januari"]
    print(jan_2020)
