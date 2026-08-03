import subprocess
import time
from river import linear_model

# מניות שתרצה לעקוב אחריהן
symbols = ["TSLA", "AAPL", "NVDA"]

# מודלים לכל מניה
models = {symbol: linear_model.LinearRegression() for symbol in symbols}

# צעד זמן (שלב)
step = 0

while True:
    step += 1

    # הפעלת הסקריפט ssstoks.sh וקריאת הפלט
    try:
        output = subprocess.check_output(["./ssstoks.sh"], text=True).strip().split('\n')
    except Exception as e:
        print("שגיאה בהרצת ssstoks.sh:", e)
        time.sleep(1)
        continue

    for line in output:
        try:
            symbol, price = line.strip().split()
            price = float(price)
        except:
            continue  # מדלג על שורות בעייתיות

        model = models.get(symbol)
        if model:
            x = {}
            prediction = model.predict_one(x)
            model.learn_one(x, price)
            deviation = round(abs(price - prediction), 3)
            print(f"{symbol} 💲 {price} | צפי: {round(prediction, 3)} | סטייה: {deviation}")

    time.sleep(5)  # כל כמה שניות לרענן (אפשר לשנות
