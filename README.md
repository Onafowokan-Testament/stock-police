# Stock Market Alert System 📈

Welcome to the **Stock Market Alert System**! This Python script monitors stock price changes for a specified company (e.g., Tesla) and sends email alerts with relevant news articles if the stock price changes significantly (more than 1%). It integrates with the **Alpha Vantage API** for stock data and the **NewsAPI** for fetching the latest news.

---

## Features

- **Stock Price Monitoring**: Tracks daily closing prices for a specified stock.
- **Price Change Alerts**: Sends email alerts if the stock price changes by more than 1%.
- **News Integration**: Fetches the latest news articles related to the company.
- **Email Notifications**: Sends formatted email alerts with news headlines and descriptions.

---

## How It Works

1. **Fetch Stock Data**: Retrieves daily stock prices using the Alpha Vantage API.
2. **Calculate Price Change**: Compares the closing prices of the last two days.
3. **Check Threshold**: If the price change exceeds 1%, fetch the latest news articles.
4. **Send Email Alerts**: Sends an email with the news articles to the specified recipient.

---

## Installation

To use this script, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Alpha Vantage API key
- NewsAPI key
- Gmail account for sending emails

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/stock-market-alert-system.git
   cd stock-market-alert-system
   ```

2. **Install the required packages**:
   ```bash
   pip install requests
   ```

3. **Set up your environment variables**:
   Replace the placeholders in the script with your actual API keys and email credentials:
   ```python
   EMAIL = "your_email@gmail.com"
   PASSWORD = "your_email_password"
   API_KEY = "your_alphavantage_api_key"
   NEWS_API_KEY = "your_newsapi_key"
   ```

4. **Run the script**:
   ```bash
   python stock_alert.py
   ```

---

## Usage

1. Ensure the script is running daily (e.g., using a cron job or task scheduler).
2. If the stock price changes by more than 1%, you will receive an email with the latest news articles related to the company.

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Alpha Vantage](https://www.alphavantage.co/) for the stock data API.
- [NewsAPI](https://newsapi.org/) for the news data API.
- [smtplib](https://docs.python.org/3/library/smtplib.html) for sending email notifications.

---

Stay informed about stock market changes with the Stock Market Alert System! 📧📰
