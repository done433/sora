import subprocess
import time
from river import linear_model

# שרתים לבדיקת פינג (אפשר לשנות)
servers = ["1.1.1.1", "202.12.27.33", "8.8.8.8"]

# מודלים נפרדים לכל שרת
models = {server: linear_model.LinearRegression() for server in servers}

# שלב (כדי שהמודל יידע שיש סדר)
step = 0

# פונקציית פינג
def ping(server):
    try:
        output = subprocess.check_output(["ping", "-c", "1", "-W", "1", server], stderr=subprocess.DEVNULL)
        line = [l for l in output.decode().split("\n") if "time=" in l][0]
        return float(line.split("time=")[-1].split(" ")[0])
    except:
        return None

# לולאה
while True:
    step += 1
    for server in servers:
        latency = ping(server)
        if latency is not None:
            x = {}
            model = models[server]
            prediction = model.predict_one(x)
            model.learn_one(x, latency)
            deviation = round(abs(latency - prediction), 3)
            print(f"{server} ⏱️ {latency} ms | צפי: {round(prediction, 3)} | סטייה: {deviation}")
        else:
            print(f"{server} ❌ אין תגובה")

    time.sleep(1)
