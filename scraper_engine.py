import requests
from bs4 import BeautifulSoup

PAGES = [
    "https://debales.ai/",
    "https://debales.ai/blog"
]

def fetch_website_text():
    collected = []

    for link in PAGES:
        try:
            r = requests.get(link, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")

            text = soup.get_text(" ", strip=True)
            collected.append(text)

        except:
            continue

    return " ".join(collected)