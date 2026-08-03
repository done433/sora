# sora


# 💥 Realtime Stock Trend Predictor  

![חתול הפרויקט שלי – My Cat](cute-cat-eyes-profile-picture-uq3edzmg1guze2hh.webp)


## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

* [Create](https://docs.gitlab.com/user/project/repository/web_editor/#create-a-file) or [upload](https://docs.gitlab.com/user/project/repository/web_editor/#upload-a-file) files
* [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/done433/sora.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

* [Set up project integrations](https://gitlab.com/done433/sora/-/settings/integrations)

## Collaborate with your team




############################################################################################


# 💥 Realtime Stock Trend Predictor  

![חתול הפרויקט שלי – My Cat](images/my_cat.webp)

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


