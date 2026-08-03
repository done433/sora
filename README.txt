# 💥 Realtime Stock Trend Predictor

**חיזוי מניות קצר טווח בזמן אמת – עדכונים כל 10 שניות!**  
מערכת שמגרדת נתונים ישירות מהאתרים (ללא API רשמי 🕵️‍♂️), מסננת ומעבדת אותם, ולומדת מגמות כמעט מידיות.  
**מושלם לבוטים סוחרים** שרוצים להיות צעד אחד לפני השוק – או לפחות לא אחרי.

---

### 🔥 למה זה מגניב
- 🖥 **Web Scraping כמו סוכן חשאי** – נתונים חיים ישירות מהדפדפן  
- ⚡ **Realtime Predictions** – תחזיות כל 10 שניות עם סטייה מינימלית  
- 🤖 **Learning Pipeline** – לומד מגמות מיידיות ומתקדם עם כל דאטה חדש  
- 🌐 **Browser Simulation** – מתחזה לדפדפן כדי לגשת לנתונים כמו משתמש אמיתי  
- 📈 **Trading Bot Ready** – קנייה/מכירה אוטומטית  
- 📊 **Realtime Visualization** – עם **Gnuplot**, ניתן לראות את המחירים בזמן אמת

---

### ⚙️ Stack & Tools
- Python 🐍  
- Scrapy / Selenium / Playwright  
- Pandas / NumPy / scikit-learn  
- Matplotlib / Plotly (למחקר/דשבורד)  
- **Gnuplot** – גרפים בזמן אמת עם קובץ `plot_live.gnu`

---

### 🔄 Pipeline גרפי

```
Web Scraping → Data Cleaning → Feature Extraction → Realtime ML Prediction → Trading Decision → Realtime Plot (Gnuplot)
```

---

### 📊 דוגמת Gnuplot Live Graph

`plot_live.gnu`:

```
set title "Realtime Stock Price"
set xlabel "Time (s)"
set ylabel "Price ($)"
set grid
set term qt
set key left top

# גרפים של TSLA ו-AAPL (ניתן להוסיף עוד מניות)
plot "prices.csv" using 1:2 with linespoints title "TSLA", \
     "prices.csv" using 1:3 with linespoints title "AAPL"
```

הרצה:

```
gnuplot -persist plot_live.gnu
```

💡 הנתונים (`prices.csv`) מתעדכנים כל 10 שניות מהמודל – כך הגרף **מראה את המניות בזמן אמת**.

---

### 💡 נקודות עיקריות למראיינים
- מערכת **Realtime**, לא מודל סטטי  
- שימוש ב‑**דאטה גולמי מאתרים**, כולל JavaScript  
- **למידה מתמשכת** – המודל מתעדכן עם כל דאטה חדש  
- **גרפים חיים עם Gnuplot** – המחשה חזותית של תחזיות בזמן אמת  
- מוכנה **לבוטי מסחר אוטומטיים**  
- בלעדי: הרגשה של **Wall Street בזמן אמת**, בלי הסחות דעת

---

> ⚠️ למטרות לימוד בלבד – אין פה ייעוץ פיננסי  
> 🎯 “Wall Street בזמן אמת, בלי גרפים משעממים, עם Python, ML ו‑Gnuplot במקום.”
