import requests

# Replace 'YOUR_API_KEY' with your actual NewsAPI API key
API_KEY = 'YOUR_API_KEY'
base_url = 'https://newsapi.org/v2/top-headlines'

topics = ['business', 'technology', 'health', 'science']

for topic in topics:
    params = {
        'apiKey': API_KEY,
        'category': topic,
        'country': 'us'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        print(f"Top news articles in {topic.capitalize()}:")

        for article in news_data['articles']:
            title = article['title']
            description = article['description']
            print(f"Title: {title}")
            print(f"Description: {description}")
            print("-" * 30)
    else:
        print(f"Error fetching news for {topic}: {response.status_code}")