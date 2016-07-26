## 3. Csvlook ##

~$ head -n 10 Combined_hud.csv | csvlook

## 4. Csvcut ##

~$ csvcut -c 2 Combined_hud.csv | head -n 10

## 5. Csvstat ##

~$ csvstat --mean Combined_hud.csv

## 6. Csvcut | csvstat ##

~$ csvcut -c 2 Combined_hud.csv | csvstat

## 8. Filtering out problematic rows ##

~$ csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv