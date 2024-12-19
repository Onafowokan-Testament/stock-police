import requests
import smtplib

STOCK_NAME = "TSLA"
EMAIL = "your mail"
PASSWORD = "your password"
rep_mail = "a rep email"
COMPANY_NAME = "Tesla Inc"
API_KEY = "api_key"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameter = {"function": "TIME_SERIES_DAILY",
             "symbol": STOCK_NAME,
             "apikey": API_KEY

             }
response = requests.get(url=STOCK_ENDPOINT, params=parameter)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]["4. close"]

day_before_yesterday_closing_price = data_list[1]["4. close"]

close_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if close_difference < 0:
    up_down = "🔻"
else:
    up_down = "⬆"
percent_diff = round((close_difference / float(yesterday_closing_price)) * 100)
if abs(percent_diff) > 1:
    NEWS_API_KEY = "b1d5364bf1e141e1a91b1fd6079e29c1"
    news_parameter = {"qInTitle": COMPANY_NAME,
                      "apikey": NEWS_API_KEY,
                      "sortBy": "publishedAt",
                      "language": "en"}
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameter)
    news_response.raise_for_status()
    news_data = (news_response.json()["articles"][:3])
    news_description = [news_data[i]["description"] for i in range(3)]
    news_title = [news_data[i]["title"] for i in range(3)]
    for i in range(3):
        news_title[i] = news_title[i].encode('ascii', 'ignore').decode('ascii')
        news_description[i] = news_description[i].encode('ascii', 'ignore').decode('ascii')
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=rep_mail,
                                msg='Subject: {}\n\n{}'.format(f"{news_title[i]}{abs(percent_diff)}",
                                f"{news_description[i]}\n This is a test for a program i am building")
                                )
            print("done")
