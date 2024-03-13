import requests
from bs4 import BeautifulSoup

def extract_text(tag, class_name, default_value="Non disponible"):
    result = tag.find(class_=class_name)
    print(result)
    return result.text.strip() if result else default_value


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Lien de la page à scraper
url = "https://www.metacritic.com/game/the-legend-of-zelda-tears-of-the-kingdom/user-reviews/?platform=nintendo-switch"

# Faites une requête HTTP pour obtenir le contenu de la page
response = requests.get(url,headers=headers)
# Vérifiez si la requête a réussi (code 200)
if response.status_code == 200:
    # Utilisez BeautifulSoup pour analyser le contenu HTML de la page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Recherchez la balise div avec la classe spécifiée
    reviews_divs = soup.find_all('div', class_='c-pageProductReviews_row g-outer-spacing-bottom-xxlarge')

    # Parcourez les divs de revues et extrayez les informations nécessaires
    for review_div in reviews_divs:
        username = extract_text(review_div, 'c-siteReviewHeader_username', "Nom d'utilisateur non disponible")
        score = extract_text(review_div, 'c-siteReviewScore', "Score non disponible")
        review_date = extract_text(review_div, 'c-siteReviewHeader_reviewDate', "Date de la critique non disponible")
        platform = extract_text(review_div, 'c-siteReview_platform', "Plateforme non disponible")
        review_text = extract_text(review_div, 'c-siteReview_quote', "Aucun texte de critique disponible")

        # Imprimez ou faites ce que vous voulez avec les données extraites
        print(f"Username: {username}")
        print(f"Score: {score}")
        print(f"Review Date: {review_date}")
        print(f"Platform: {platform}")
        print(f"Review Text: {review_text}")
        print("-" * 50)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
