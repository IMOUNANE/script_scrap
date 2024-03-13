import requests
import json
import time
from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "unknown"
def scrape_and_save_data(base_url, num_iterations,limit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Liste pour stocker tous les objets filtrés
    all_filtered_items = []
    detected_languages = set()

    # Itérer sur les différentes valeurs de l'offset
    for remaining_iterations in reversed(range(num_iterations)):
        # Construire l'URL avec l'offset
        url = f"{base_url}&offset={remaining_iterations}&limit={limit}"
        # Faire la requête HTTP pour obtenir le contenu de la page
        response = requests.get(url, headers=headers)
        time.sleep(1)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Charger le JSON
            response_data = response.json()

            # Accéder aux valeurs des clés "data" et "totalResults"
            data = response_data.get('data', {})
            total_count = data.get('totalResults', 0)
            items_list = data.get('items', [])

            keys_to_keep = ["id", "quote", "score", "date", "author", "platform"]

            # Appliquer le filtrage à chaque objet de la liste
            filtered_items = [{key: item[key] for key in keys_to_keep} for item in items_list]


            filtered_items = [
                        {key: item[key] for key in keys_to_keep} | {"lang": detect_language(item["quote"])} 
                        for item in items_list
            ]

            # Ajouter les objets filtrés à la liste
            all_filtered_items.extend(filtered_items)

            # Mettre à jour les langues détectées
            detected_languages.update(item["lang"] for item in filtered_items)

            print(f"Boucles restantes : {remaining_iterations}")

        else:
            print(f"Échec de la requête. Code d'état : {response.status_code}")

    print("Langues détectées :", detected_languages)
    # Afficher le total count
    print("Total Count :", total_count)

    # Créer le fichier JSON avec le nom spécifié
    output_file_name = f"comment_zelda_{len(all_filtered_items)}.json"
    with open(output_file_name, 'w') as output_file:
        json.dump(all_filtered_items, output_file, indent=2)

    print(f"Les données ont été sauvegardées dans {output_file_name}")

# URL de base sans l'offset
base_url = "https://internal-prod.apigee.fandom.net/v1/xapi/reviews/metacritic/user/games/the-legend-of-zelda-tears-of-the-kingdom/platform/nintendo-switch/web?"

# Nombre d'itérations (offsets) que vous souhaitez
num_iterations = 4
limit=250

# Appeler la fonction pour scraper et sauvegarder les données
scrape_and_save_data(base_url, num_iterations,limit)
