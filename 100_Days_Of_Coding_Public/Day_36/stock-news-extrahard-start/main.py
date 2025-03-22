import requests
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Flag for messages 
get_news = False
first_price = None
second_price = None
percentage_change = None

ALPHAVANTAGE_API_KEY = ""
NEWS_API_KEY = NewsApiClient(api_key="")
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&datatype=json&apikey={ALPHAVANTAGE_API_KEY}"

# Twilio access
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_data():
    global get_news, first_price, second_price, percentage_change
    response = requests.get(url)
    print("HTTP-Statuscode:", response.status_code)  
    print("Data:", response.text)  
        
    response.raise_for_status()
    data = response.json()
    
    first_date_key = list(data["Time Series (Daily)"].keys())[0] 
    first_data_entry = data["Time Series (Daily)"][first_date_key]["4. close"]
    
    second_date_key = list(data["Time Series (Daily)"].keys())[1] 
    second_data_entry = data["Time Series (Daily)"][second_date_key]["4. close"]
    
    first_price = float(first_data_entry)
    second_price = float(second_data_entry)
    
    percentage_change = ((first_price - second_price) / second_price) * 100
    print("Percentage Change:", percentage_change)
    # abs() is a python function for the absoulte value. 
    if abs(percentage_change) >= 2:
        print("Get News")
        get_news = True
   

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news_data():
    news_message = ""
    from_date = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    
    news_response = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": COMPANY_NAME,
            "from": from_date,
            "sortBy": "relevancy",
            "language": "en",
            "apiKey": ""
        }
    )
    
    articles = news_response.json().get("articles", [])
    three_articles = articles[:3]
    
    for article in three_articles:
        news_message += f"Headline: {article['title']}\n"
        news_message += f"Brief: {article['description']}\n"
        news_message += f"Link: {article['url']}\n\n"
    
    return news_message


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
get_stock_data()
while get_news:
    
    if get_news:
        news_message = get_news_data()
        
        stock_message = f"TSLA: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n"
        stock_message += news_message
        
        message = client.messages.create(
            from_='whatsapp:',
            body= stock_message, 
            to='whatsapp:+'
        )
    print("Nachricht gesendet.")
    get_news = False


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

