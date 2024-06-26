import requests
from send_email import send_email

topic = "tesla"
api_key = "db850158816d431fa3a623344ecf176e"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-09-18" \
      "&sortBy=publishedAt&apiKey=db850158816d431fa3a623344ecf176e" \
      "&language=en"  # Add language restriction

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""

for article in content["articles"][:21]:
    message = "Subject: Today's news"\
               + "\n" + message + article["title"] + '\n'\
               + article["description"] + '\n' \
               + article['url'] + 2*'\n'


message = message.encode("utf-8")

send_email(message)






