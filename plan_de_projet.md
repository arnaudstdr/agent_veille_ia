# 🧠 PLAN DU PROJET : Agent de Veille IA + Générateur de Thread Recap

## 🔹 Étape 0 – Objectif & périmètre
- 🎯 Objectif : Collecter, résumer et formater les meilleures actualités IA de la semaine, automatiquement.
- 🧩 Sortie attendue :
- Résumés quotidiens ou hebdo
- Fichier Markdown pour threads Twitter
- (Optionnel) Envoi automatique ou préprogrammation sur X

## 🔹 Étape 1 – Choix des sources d’information
- 🔍 À surveiller :
- Hugging Face blog
- ArXiv (cs.AI, cs.CL, cs.LG)
- Google Research Blog
- OpenAI blog
- Twitter/X : comptes comme @levelsio, @swyx, @karpathy, @leandro, @marktechpost
- Mistral.ai
- ✅ Action :
  - Créer un script de scraping/API/feedparser pour chaque source

## 🔹 Étape 2 – Stockage et historique
- Base de données légère (📦 SQLite ou JSON)
- Contenu brut
- Date, source, lien
- Statut : non lu, filtré, résumé, threadé
- Option : taguer les actus par thème (modèles, tools, papers…)

## 🔹 Étape 3 – Filtrage & nettoyage
- 🧹 Retirer :
  - Contenu non-IA
  - Doublons
  - Pubs ou titres clickbait
- ✨ Utiliser :
  - Règles simples (mots-clés IA, DL, LLM, agent…)
  - Ou un petit classifieur avec LLM (optionnel)

## 🔹 Étape 4 – Résumé automatique
- Pour chaque article sélectionné :
  - Résumé court (~300 caractères)
  - Résumé long (~800 caractères)
- ⚙️ Tools :
  - LLM (Gemini ou GPT-4)
  - Format standardisé : titre – résumé – lien

## 🔹 Étape 5 – Génération du thread
- Créer une structure hebdo :
```markdown
🚀 Weekly AI Recap – Semaine du 1er au 7 avril

🧠 1. OpenAI publie GPT-5 ?
Résumé...
👉 https://...

🧪 2. Paper ArXiv : "LLaVA-Next"
Résumé...
👉 https://...

📦 Fait avec ❤️ par [ton pseudo]
```
- Stockage dans un fichier .md
- (Optionnel) conversion vers .txt ou publication auto via Tweepy

## 🔹 Étape 6 – Automatisation & routine
- 🤖 Script hebdomadaire :
  - Scrape > Filtre > Résume > Génère le thread
- (Optionnel)
  - Interface Streamlit simple ou ligne de commande
  - Prévisualisation des tweets
  - Commande “publier maintenant” ou “planifier”

## 🔹 Étape 7 – Bonus (plus tard)
- 🧩 Intégration Notion (base des actus, recap intégré)
- 🧠 Fine-tuning d’un LLM sur ton style de thread
- 📈 Ajout de tracking de vues/interactions
