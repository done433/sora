
![Sora, my cat](sora.jpeg)
![My Project Cat](sora.jpeg)
In memory of Sora — the most beautiful cat in the world. He loved Bamba and
helped me chase away bugs. My silly little boy, the one I loved most of all.
I miss you, Sora.


---




---
## License

Released under the **MIT License** — use it, copy it, change it, share it, even
commercially, no strings attached beyond keeping the copyright notice. See
[LICENSE](LICENSE) for the full text.

---


# Realtime Stock Trend Predictor

**Short-term stock trend prediction in real time — fresh signals every 10 seconds.**

A pipeline that scrapes live market data straight from the browser (no official
API), cleans and processes it, and learns near-instant trends. Built for trading
bots that need to stay a step ahead of the market — or at least not a step behind.

> ⚠️ For educational purposes only. Not financial advice.

---

## Why it's interesting

This isn't a static model trained once and left alone. It's a live system that
keeps learning as new data arrives:

- **Live web scraping** — pulls data directly from the rendered page, including
  JavaScript-loaded content, by driving a real browser session.
- **Realtime predictions** — a new forecast every 10 seconds with minimal drift.
- **Continuous learning** — the model updates with every incoming batch instead
  of relying on a frozen snapshot.
- **Trading-bot ready** — exposes buy/sell signals an automated strategy can act on.
- **Live visualization** — prices and predictions plotted in real time with Gnuplot.

---

## Tech stack

| Layer | Tools |
|-------|-------|
| Language | Python |
| Scraping | Scrapy · Selenium · Playwright |
| Data & ML | Pandas · NumPy · scikit-learn |
| Dashboards / research | Matplotlib · Plotly |
| Realtime plotting | Gnuplot (`plot_live.gnu`) |

---

## Pipeline
