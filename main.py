import requests
from dotenv import load_dotenv  # Import the loader
import os   # Import os to access environment variables

# Step 3a: Load the .env file into the environment
load_dotenv()

# Step 3b: Access your variable using os.getenv()
api_key = os.getenv("API_KEY")

news_api_url=(
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&"
    f"category=business&"
    f"apiKey={api_key}"
)
request = requests.get(news_api_url)

content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print()