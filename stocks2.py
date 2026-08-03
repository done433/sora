import subprocess
import time
import os
import pickle
from river import linear_model

symbols = ["TSLA", "AAPL", "NVDA"]
model_file = "models.pkl"
step_file = "step.txt"

# טעינת מודלים אם קיימים
if os.path.exists(model_file):
    with open(model_file, "rb") as f:
        models = pickle.load(f)
else:
    models = {symbol: linear_model.LinearRegression() for symbol in symbols}

# טעינת מספר הצעד האחרון אם קיים
if os.path.exists(step_file):
    with open(step_file, "r") as f:
        step = int(f.read().strip())
else:
    step = 0

while True:
    step += 1

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
            continue

        model = models.get(symbol)
        if model:
            x = {}
            prediction = model.predict_one(x)
            model.learn_one(x, price)
            deviation = round(abs(price - prediction), 3)
            print(f"{symbol} 💲 {price} | צפי: {round(prediction, 3)} | סטייה: {deviation}")

    # שמירת מצב המודלים
    with open(model_file, "wb") as f:
        pickle.dump(models, f)

    # שמירת הצעד האחרון
    with open(step_file, "w") as f:
        f.write(str(step))

    time.sleep(5)
