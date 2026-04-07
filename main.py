import requests
from dotenv import load_dotenv  # Import the loader
import os   # Import os to access environment variables
from send_email import send_email

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

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

send_email(message=body)