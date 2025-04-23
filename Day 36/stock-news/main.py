import requests
from twilio.rest import Client

SENDER = '15551234444'
RECEIVER = '15551234444'
TWILIO_ACCOUNT_SID = 'ssid here'
TWILIO_AUTH_TOKEN = 'auth token here'
STOCK_NAME = "DE"
COMPANY_NAME = "Deere & Company"
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_KEY = "AV key here"
AV_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_KEY
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "news key here"
NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "pageSize": 4,
    "apiKey": NEWS_KEY
}

response = requests.get(AV_ENDPOINT, params=AV_PARAMETERS)
response.raise_for_status()
stock_data = response.json()

closing_price_yesterday = [stock_data["Time Series (Daily)"][date]["4. close"] for date in stock_data["Time Series (Daily)"]][0]

closing_price_dby = [stock_data["Time Series (Daily)"][date]["4. close"] for date in stock_data["Time Series (Daily)"]][1]

shift = ((float(closing_price_yesterday) - float(closing_price_dby)) / float(closing_price_dby)) * 100
if abs(shift) > 5:
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    response.raise_for_status()
    news_data = response.json()

    article_summaries = [
        {"title": article["title"], "description": article["description"]}
        for article in news_data["articles"][:3]
    ]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in article_summaries:
        message_body = f"Headline: {article['title']}\nBrief: {article['description']}"
        sent_message = client.messages.create(
            from_=SENDER,
            body=message_body,
            to=RECEIVER
        )
        print(f"Sent message SID: {sent_message.sid}")

