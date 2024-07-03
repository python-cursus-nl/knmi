# KNMI
Voorbeeld project om te leren automatisch gegevens te downloaden met [requests](https://requests.readthedocs.io/en/latest/) en dit te verwerken met [pandas](https://pandas.pydata.org/). Dit project bevat meerdere git branches, elk met een andere versie. Bij elke branch hoort een tutorial op [python-cursus.nl](https://python-cursus.nl). De `main`-branch verwijst altijd naar de laatste versie.

| Branch   | Toelichting                                                                                                                                                                           |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| main     | Zie versie-2                                                                                                                                                                          |
| versie-1 | Eenvoudige versie, zoals beschreven in  [Geautomatiseerd gegevens downloaden](https://python-cursus.nl/blog/geautomatiseerd-gegevens-downloaden/).                                    |
| versie-2 | Versie met  `pandas`, zoals beschreven in  [Werken met pandas](https://python-cursus.nl/blog/pandas-introductie/).                                                                    |
| versie-3 | Versie met  `pandas`, waarin dieper wordt ingegaan op gegevens selecteren. Beschreven in [Gegevens selecteren met pandas](https://python-cursus.nl/blog/pandas-gegevens-selecteren/). |

Om het project lokaal te kopiëren neem je de volgende stappen:

```shell
cd projects  // Lokatie van je projecten
git clone https://github.com/python-cursus-nl/knmi.git  // Of git@github.com:python-cursus-nl/knmi.git als je via ssh werkt
git switch versie-3  // Of een andere versie
```

## Versies

### Versie 1
Eenvoudige versie waarin je leert [requests](https://requests.readthedocs.io/en/latest/) te gebruiken om een `txt`-bestand te downloaden van de KNMI-website. Vervolgens schoon je dit bestand op en sla je het op als CSV-bestand.

### Versie 2
In deze versie leer je de basis van het werken met [pandas](https://pandas.pydata.org/). Na het downloaden / opschonen van de data, laad je het CSV-bestand in een `DataFrame` in en voer je een eenvoudige analyse uit.

Daarnaast zijn er in versie-2 nog enkele aanpassingen doorgevoerd:

* De data wordt in een aparte map opgeslagen, welke wordt genegeerd door `git`.
* Met [requests-cache](https://requests-cache.readthedocs.io/en/stable/) wordt de response in een cache opgeslagen, zodat je rustig de functie `download` kunt aanroepen, zonder elke keer daadwerkelijk het bestand te downloaden. Zie [Cache je HTTP requests](https://python-cursus.nl/blog/requests-cache/) voor meer informatie.
* De code is opgesplitst in meerdere modules.

### Versie 3

In deze versie vind je vele voorbeelden om gegevens uit een `DataFrame` te selecteren met behulp van `.loc` en `.iloc`.