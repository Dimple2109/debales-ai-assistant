from scraper_engine import fetch_website_text
from vector_engine import build_db
from agent_flow import build_agent


def run():

    print("🔄 Loading data...")
    raw_text = fetch_website_text()

    print("🧠 Building knowledge base...")
    db = build_db(raw_text)

    agent = build_agent(db)

    print("\n🤖 Debales AI Ready (type exit)\n")

    while True:
        q = input("You: ")

        if q.lower() == "exit":
            break

        result = agent.invoke({
            "query": q,
            "mode": "",
            "context": "",
            "response": ""
        })

        print("\nBot:", result["response"], "\n")


if __name__ == "__main__":
    run()