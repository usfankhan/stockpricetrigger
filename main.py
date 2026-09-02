import yfinance as yf
from datetime import datetime
from pathlib import Path


STOCK = "INFY.NS"
TARGET_PRICE = 1000

ALERT_FILE = Path("stock_alerts.txt")


def get_stock_price():
    stock = yf.Ticker(STOCK)

    data = stock.history(period="1d")

    if data.empty:
        raise Exception("Unable to get stock data")

    return float(data["Close"].iloc[-1])


def save_alert(price):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = (
        f"[{current_time}] "
        f"ALERT: {STOCK} reached ₹{price:.2f} "
        f"(Target: ₹{TARGET_PRICE})\n"
    )

    with open(ALERT_FILE, "a", encoding="utf-8") as file:
        file.write(message)

    print(message)


def main():

    print("Checking stock price...")

    current_price = get_stock_price()

    print(f"Stock: {STOCK}")
    print(f"Current Price: ₹{current_price:.2f}")
    print(f"Target Price: ₹{TARGET_PRICE}")

    if current_price >= TARGET_PRICE:

        print("🚨 TARGET PRICE REACHED!")

        save_alert(current_price)

    else:

        print("Target price not reached.")


if __name__ == "__main__":
    main()