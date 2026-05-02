import requests
from config import SERP_KEY

def web_search(query):
    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": SERP_KEY,
        "Content-Type": "application/json"
    }

    res = requests.post(url, headers=headers, json={"q": query})
    data = res.json()

    snippets = []

    for item in data.get("organic", [])[:3]:
        snippets.append(item.get("snippet", ""))

    return "\n".join(snippets)