import feedparser
import json
from datetime import datetime, timedelta
import os
import re

# config
RSS_LIST_PATH = os.path.join(os.path.dirname(__file__), "flux_rss.json")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "outputs")
DAYS_LIMIT = 7

def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')

def load_rss_sources(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def scrape_rss_source(name, url, days_limit=DAYS_LIMIT):
    print(f"[INFO] Lecture du flux RSS pour : {name}")
    feed = feedparser.parse(url)
    if not feed.entries:
        print(f"[WARNING] Aucun article trouvé pour {name}")
        return []
    
    results = []
    date_limit = datetime.now() - timedelta(days=days_limit)

    for entry in feed.entries:
        if hasattr(entry, 'published_parsed'):
            published = datetime(*entry.published_parsed[:6])
            if published >= date_limit:
                results.append({
                    "title": entry.title,
                    "url": entry.link,
                    "date": published.isoformat(),
                    "scraped_at": datetime.now().isoformat()
                })
            else:
                print(f"[DEBUG] Article trop ancien, ignoré")
        else:
            print(f"[DEBUG] Pas de date de publication trouvée")
            # On ajoute quand même l'article sans date
            results.append({
                "title": entry.title,
                "url": entry.link,
                "date": None,
                "scraped_at": datetime.now().isoformat()
            })
    
    return results

def save_results(source_name, articles):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{slugify(source_name)}.json"
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"[INFO] {len(articles)} articles enregistrés dans {path}")

def run_all():
    sources = load_rss_sources(RSS_LIST_PATH)
    for source in sources:
        name = source["name"]
        url = source["url"]
        articles = scrape_rss_source(name, url)
        save_results(name, articles)

if __name__ == "__main__":
    run_all()    
