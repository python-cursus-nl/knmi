URL = "https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/maandgegevens/mndgeg_260_tg.txt"
TXT = "../data/knmi.txt"
CSV = "../data/knmi.csv"

KNMI_COLUMNS = {
    "STN": "Station",
    "JAN": "Januari",
    "FEB": "Februari",
    "MAR": "Maart",
    "APR": "April",
    "MAY": "Mei",
    "JUN": "Juni",
    "JUL": "Juli",
    "AUG": "Augustus",
    "SEP": "September",
    "OCT": "Oktober",
    "NOV": "November",
    "DEC": "December",
    "YYYY": "Jaar",
    "YEAR": "Jaargemiddelde",
}

MONTH_COLUMNS = []
for key, value in KNMI_COLUMNS.items():
    if key not in ["STN", "YYYY", "YEAR"]:
        MONTH_COLUMNS.append(value)
