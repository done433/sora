#!/bin/bash

while true; do
  # חילוץ נתונים לפורמט נקי: מניה זמן ערך צפי
  awk '
    BEGIN { OFS="\t"; i = 0 }
    /💲/ && /צפי:/ {
      match($0, /TSLA|AAPL|NVDA/, s)
      stock = s[0]
      match($0, /💲 *([0-9.]+)/, a)
      real = a[1]
      match($0, /צפי: *([0-9.]+)/, b)
      pred = b[1]
      if (stock && real && pred)
        print i++, stock, real, pred
    }
  ' prlrt.txt > data_clean.txt

  gnuplot -persist <<-EOF
    set title "Live Stock Price vs Prediction"
    set xlabel "Time Step"
    set ylabel "Price"
    set key outside
    set grid
    set style data linespoints

    plot \
      'data_clean.txt' using (\$2 eq "TSLA" ? \$1 : 1/0):3 title "TSLA 💲" with linespoints lc rgb "red", \
      'data_clean.txt' using (\$2 eq "TSLA" ? \$1 : 1/0):4 title "TSLA צפי" with linespoints lc rgb "pink", \
      'data_clean.txt' using (\$2 eq "AAPL" ? \$1 : 1/0):3 title "AAPL 💲" with linespoints lc rgb "green", \
      'data_clean.txt' using (\$2 eq "AAPL" ? \$1 : 1/0):4 title "AAPL צפי" with linespoints lc rgb "light-green", \
      'data_clean.txt' using (\$2 eq "NVDA" ? \$1 : 1/0):3 title "NVDA 💲" with linespoints lc rgb "blue", \
      'data_clean.txt' using (\$2 eq "NVDA" ? \$1 : 1/0):4 title "NVDA צפי" with linespoints lc rgb "cyan"
EOF

  sleep 5
done
