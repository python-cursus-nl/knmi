import requests

URL = "https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/maandgegevens/mndgeg_260_tg.txt"
TXT = "../data/knmi.txt"
CSV = "../data/knmi.csv"


def download():
    """ Download the file from the URL """

    # Get the data from the URL
    response = requests.get(URL)

    # If the status code is 400 or higher raise an error
    response.raise_for_status()

    # Write the data to a file
    with open(TXT, "w", encoding="utf-8") as file:
        file.write(response.text)


def clean_data():
    """
    Read in the raw data (txt) and clean it up. Remove help text,
    spaces and empty lines. Store as CSV.
    """

    try:
        # Open the raw data
        with open(TXT, "r", encoding="utf-8") as file:
            # Loop over every line. If it is the header
            # (starts with "STN,YYYY") or starts with 260,
            # we want to keep it. Remove spaces.
            lines = []
            for line in file:
                # Keep headers and rows with values
                if line.startswith("STN,YYYY") or line.startswith("260"):
                    # Remove spaces
                    lines.append(line.replace(" ", ""))

        # Write the cleaned lines to a new CSV-file.
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
