import json
import os
import requests

def fetch_and_save_data(url_file, result_dir):
    # Charger les données depuis le fichier url.json
    with open(url_file, 'r') as f:
        data = json.load(f)

    # Extraire l'URL et le payload
    url = data['url']
    payload = data['payload']

    # Effectuer la requête GET avec le payload
    response = requests.get(url, params=payload)

    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Créer le dossier result_dir s'il n'existe pas
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        # Enregistrer la réponse dans le fichier result.json dans le dossier result_dir
        result_file = os.path.join(result_dir, "result.json")
        with open(result_file, 'w') as f:
            json.dump(response.json(), f)
        print("Données enregistrées avec succès dans", result_file)
    else:
        print("La requête a échoué avec le code", response.status_code)

# Appel de la fonction avec les chemins appropriés
fetch_and_save_data("./data/api/url.json", "./data/api/result_data_json")
