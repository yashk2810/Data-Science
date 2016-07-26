## 1. Data munging ##

~$ ls -l

## 2. Data exploration ##

~$ head -n 10 *.csv

## 3. Filtering ##

~$ head -n 10 combined_hud.csv

## 4. Consolidating datasets ##

~$ tail -n 64535 Hud_2013.csv >> combined_hud.csv

## 5. Counting ##

~$ grep "1980-1989" combined_hud.csv | wc -l