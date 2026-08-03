set title "Stock Actual vs Prediction (Live)"
set xlabel "Entry Number"
set ylabel "Price"
set key outside
set grid
set style data linespoints
set datafile separator " "

# פונקציית עזר לניתוח הקובץ inline עם awk, בלי ליצור קבצים
stats 'prlrt.txt' nooutput

plot '< awk '\'' 
    { 
        stock=$1; 
        match($0, /💲 *([0-9.]+)/, a); 
        real=a[1]; 
        match($0, /צפי: *([0-9.]+)/, b); 
        pred=b[1]; 
        if(stock && real && pred) print stock, real, pred 
    } '\'' ' using ($0):2:(strcol(1) eq "TSLA" ? 1 : 1/0) with linespoints lt rgb "red" title "TSLA Real", \
     '' using ($0):3:(strcol(1) eq "TSLA" ? 1 : 1/0) with linespoints lt rgb "pink" title "TSLA Pred", \
     '' using ($0):2:(strcol(1) eq "AAPL" ? 1 : 1/0) with linespoints lt rgb "green" title "AAPL Real", \
     '' using ($0):3:(strcol(1) eq "AAPL" ? 1 : 1/0) with linespoints lt rgb "light-green" title "AAPL Pred", \
     '' using ($0):2:(strcol(1) eq "NVDA" ? 1 : 1/0) with linespoints lt rgb "blue" title "NVDA Real", \
     '' using ($0):3:(strcol(1) eq "NVDA" ? 1 : 1/0) with linespoints lt rgb "light-blue" title "NVDA Pred"

pause 5
reread
