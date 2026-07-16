import requests
from config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/everything"


def execute(arguments: dict):

    query = arguments.get("query")

    if not query:
        return "❌ News Error: Query is required."

    if not NEWS_API_KEY:
        return "❌ News Error: NEWS_API_KEY not found."

    try:

        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 5,
            "apiKey": NEWS_API_KEY
        }

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return f"❌ News API Error:\n{response.text}"

        data = response.json()

        if data.get("status") != "ok":
            return f"❌ News API Error: {data.get('message', 'Unknown Error')}"

        articles = data.get("articles", [])

        if len(articles) == 0:
            return f"❌ No news found for '{query}'."

        result = []

        for i, article in enumerate(articles, start=1):

            title = article.get("title", "No Title")
            source = article.get("source", {}).get("name", "Unknown")
            published = article.get("publishedAt", "")
            url = article.get("url", "")

            result.append(
                f"{i}. {title}\n"
                f"📰 Source : {source}\n"
                f"📅 Published : {published}\n"
                f"🔗 Link : {url}\n"
            )

        return "\n".join(result)

    except requests.exceptions.Timeout:
        return "❌ News Error: Request timed out."

    except requests.exceptions.ConnectionError:
        return "❌ News Error: Unable to connect to News API."

    except Exception as e:
        return f"❌ News Error: {e}"


if __name__ == "__main__":

    print(
        execute(
            {
                "query": "Artificial Intelligence"
            }
        )
    )