import requests

from src.data import clean_data, download, get_highest_mean_temp, load_data

if __name__ == "__main__":
    # Download de gegevens
    try:
        download()
    except requests.exceptions.HTTPError as e:
        print("Error while downloading file:", e)

    # Schoon de gegevens op, sla op als CSV
    clean_data()

    # Laad de gegevens in een pandas DataFrame en voer een aantal analyses uit
    df = load_data()
    get_highest_mean_temp(df=df)
