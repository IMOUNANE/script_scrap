
import requests
import json
from bs4 import BeautifulSoup

def scrape_reviews(source,url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        review_cards = soup.find_all('div', class_='review-card')
        reviews = []
        for card in review_cards:
            review = {}
            
            author_element = card.find(class_='review-card__user-info')
            author_elementAuthor = author_element.find(class_='review-card__user-link')
            review['author'] = author_elementAuthor.get_text(strip=True) if author_element else ""

            text_element = card.find('div', class_='review-card__text')
            review['text'] = text_element.get_text(strip=True) if text_element else ""
            
            date_elementdate = author_element.find(class_='review-card__date')
            review['date'] = date_elementdate.get_text(strip=True) if text_element else ""
            
            review['source']=source
            
            reviews.append(review)
        return reviews
    else:
        print("Une erreur s'est produite lors de la récupération de la page.")

url = "https://rawg.io/games/the-legend-of-zelda-breath-of-the-wild-sequel"

def main(params):
    dataset_metacritic=params.get('dataset_metacritic',0)
    reviews = scrape_reviews("rawg",url)
    dataset_rawg= json.dumps(reviews)
    return {"dataset_rawg":dataset_rawg,"dataset_rawg":dataset_metacritic}
