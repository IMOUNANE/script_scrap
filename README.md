# PYG

# Description

Probe your Game est un outil de scraping basé sur openwisk dédié à la collecte de données provenant de sites web de critiques de jeux vidéo. L'objectif principal est de centraliser ces données en vue d'une analyse ultérieure. L'outil sera développé pour automatiser le processus de collecte, garantissant ainsi une extraction régulière et efficace des critiques de jeux vidéo à partir de diverses sources en ligne. À terme, il permettra d'explorer les jeux vidéo sous différents angles, comme illustré dans l'exemple ci-dessous.

![brainstorming](public/brainstorming.png)

## Installation

Voici les commande à lancer afin de lancer le projet et permettre de le visualiser. les actions peuvent se lancer indépendament grace aux fichier bash dans le dossier `bash_script`. Il y a un aperçu des données scrapé en local dans le dossier `public/json_example`.

```sh
sh build.sh
wsk action get seqeunce_web --url
```

Liste des actions et séquences pouvant être lancé indépendamment

```sh
sh metacritic.sh
sh rawg.sh
sh render_web.sh
wsk action get seqeunce.sh
```
