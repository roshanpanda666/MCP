import requests
import numpy as np
from sklearn.linear_model import LinearRegression
from tqdm import tqdm
import time

def predict_prices():
    print("📡 Fetching data from backend...")
    response = requests.get("http://127.0.0.1:8000/")
    data = response.json()
    print("✅ Data fetched!")

    raw = data[-1]  # use latest entry
    years = [int(raw["year1"]), int(raw["year2"]), int(raw["year3"])]
    prices = [int(raw["price1"]), int(raw["price2"]), int(raw["price3"])]

    X = np.array(years).reshape(-1, 1)
    y = np.array(prices)

    print("\n⚙️ Training Model...")
    for _ in tqdm(range(100), desc="🔧 Analyzing", ncols=75):
        time.sleep(0.005)

    model = LinearRegression()
    model.fit(X, y)

    last_year = max(years)
    future_years = np.array([last_year + i for i in range(1, 11)]).reshape(-1, 1)
    predicted_prices = []

    print("\n📊 Predicting next 10 years...")
    for year in tqdm(future_years, desc="📈 Predicting", ncols=75):
        time.sleep(0.01)
        price = model.predict(year.reshape(1, -1))[0]
        predicted_prices.append(int(price))

    print("\n📌 Actual Data:")
    for year, price in zip(years, prices):
        print(f"Year: {year} | Price: ₹{price}")

    print("\n🔮 Predicted Prices for Next 10 Years:")
    for year, price in zip(future_years.ravel(), predicted_prices):
        print(f"Year: {year} | Predicted Price: ₹{price}")

    return list(zip(future_years.ravel(), predicted_prices))
