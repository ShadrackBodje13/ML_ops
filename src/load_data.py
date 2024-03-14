# Librairies
import csv
import pandas as pd


# Data
URL = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-tertiaire-2/lines?size=10000&format=csv&after=10000%2C965634&header=true"

data = pd.read_csv(URL)

# Verifier que data contient des donnée
assert len(data) > 0

# print la taille de data
print(data.shape)

# Enregistre le fichier qu'on crée en sortie

output_file = f"./data/dpe_tertiaire_20240314.csv"
data.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL)
