#!/bin/bash

symbols=("TSLA" "AAPL" "NVDA")

for symbol in "${symbols[@]}"; do
  price=$(curl -s -H "User-Agent: Mozilla/5.0" \
    "https://query1.finance.yahoo.com/v8/finance/chart/$symbol" | \
    jq '.chart.result[0].meta.regularMarketPrice')
  echo "$symbol: \$${price}"
done
