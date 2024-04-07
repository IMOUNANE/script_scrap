
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

def scrape_and_save_data(source, base_url, num_iterations,limit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    all_filtered_items = []
    detected_languages = set()

    for remaining_iterations in reversed(range(num_iterations)):
        url = f"{base_url}&offset={remaining_iterations}&limit={limit}"
        response = requests.get(url, headers=headers)
        time.sleep(1)

        if response.status_code == 200:
            response_data = response.json(encoding='utf-8')
            data = response_data.get('data', {})
            items_list = data.get('items', [])

            keys_to_keep = ["id", "quote", "score", "date", "author", "platform"]

            filtered_items = [{key: item[key] for key in keys_to_keep} for item in items_list]

            filtered_items = [
                {**{key: item[key] for key in keys_to_keep}, "lang": detect_language(item["quote"]),"origin":source} 
                for item in items_list
            ]

            all_filtered_items.extend(filtered_items)

            detected_languages.update(item["lang"] for item in filtered_items)

            all_filtered_items_json = json.dumps(all_filtered_items)
            return all_filtered_items_json
        else:
            print(f"Échec de la requête. Code d'état : {response.status_code}")
   


def main(source="metacritic",base_url="https://internal-prod.apigee.fandom.net/v1/xapi/reviews/metacritic/user/games/the-legend-of-zelda-tears-of-the-kingdom/platform/nintendo-switch/web?",num_iterations=1,limit=50):
    dataset = scrape_and_save_data(source, base_url, num_iterations,limit)
    return {"dataset_metacritic":dataset}

