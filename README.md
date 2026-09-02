# 📈 Stock Price Trigger

A Python-based stock price monitoring automation that checks the latest stock price using `yfinance`.

The project can run automatically using **GitHub Actions**. When a stock reaches or exceeds a target price, an alert is generated and saved to `stock_alerts.txt`.

## 🚀 Features

* 📊 Fetches the latest stock price
* 🎯 Supports customizable stock symbols
* 💰 Set your own target price
* 🚨 Triggers an alert when the target price is reached
* 📝 Saves alerts to `stock_alerts.txt`
* 🕒 Adds a timestamp to every alert
* ⚙️ Runs automatically using GitHub Actions
* 🔄 Automatically commits updated alerts back to the repository

## 📁 Project Structure

```text
stockpricetrigger/
│
├── .github/
│   └── workflows/
│       └── stock-check.yml
│
├── main.py
├── requirements.txt
├── stock_alerts.txt
└── README.md
```

## ⚙️ Configuration

Open `main.py` and change the stock symbol and target price:

```python
STOCK = "INFY.NS"
TARGET_PRICE = 1000
```

### Example Stock Symbols

| Company             | Symbol          |
| ------------------- | --------------- |
| Infosys             | `INFY.NS`       |
| TCS                 | `TCS.NS`        |
| Reliance Industries | `RELIANCE.NS`   |
| HDFC Bank           | `HDFCBANK.NS`   |
| ICICI Bank          | `ICICIBANK.NS`  |
| State Bank of India | `SBIN.NS`       |
| Wipro               | `WIPRO.NS`      |
| Tata Motors         | `TATAMOTORS.NS` |
| ITC                 | `ITC.NS`        |

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/usfankhan/stockpricetrigger.git
```

Go to the project folder:

```bash
cd stockpricetrigger
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python main.py
```

Example output:

```text
Checking stock price...

Stock: INFY.NS
Current Price: ₹1131.40
Target Price: ₹1000

🚨 TARGET PRICE REACHED!

[2026-09-02 08:55:12] ALERT: INFY.NS reached ₹1131.40 (Target: ₹1000)
```

## 📝 Alert File

When the target price is reached, the project saves the alert in:

```text
stock_alerts.txt
```

Example:

```text
[2026-09-02 13:20:16] ALERT: TCS.NS reached ₹2342.90 (Target: ₹2300)
[2026-09-02 13:21:35] ALERT: INFY.NS reached ₹1133.40 (Target: ₹1000)
```

## 🤖 GitHub Actions Automation

The project uses GitHub Actions to automatically run the stock price checker.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs the stock price checker.
5. Updates `stock_alerts.txt`.
6. Commits the updated alert file.
7. Pushes the changes back to the repository.

Example workflow:

```yaml
name: Stock Price Check

on:
  schedule:
    - cron: "*/30 * * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  check-stock:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Check stock price
        run: python main.py

      - name: Commit and push alert file
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"

          git add stock_alerts.txt

          git diff --staged --quiet || git commit -m "Update stock alerts"

          git push
```

## 📦 Requirements

```text
yfinance
```

## 🔮 Future Improvements

* 📧 Email notifications
* 📱 Telegram alerts
* 💬 Discord or Slack notifications
* 📊 Multiple stock monitoring
* 📈 Price history and charts
* 🔔 Real-time notifications
* 🌐 Web dashboard

## 🛠️ Technologies Used

* Python
* yfinance
* GitHub Actions

## 👨‍💻 Author

**Usfan Khan**

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.
