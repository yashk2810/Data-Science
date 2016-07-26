## 1. Appending ##

~$ echo "Take one down, pass it around, 98 bottles of beer on the wall..." >> be

## 2. Redirecting from a file ##

~$ sort -r < beer.txt

## 3. The grep command ##

~$ grep "bottles of" beer.txt coffee.txt

## 4. Special characters ##

~$ grep "beer" beer?.txt

## 5. The star wildcard ##

~$ grep "beer" *.txt

## 6. Piping output ##

~$ python rand.py | grep 9

## 7. Chaining commands ##

~$ echo "Beers are bad for health" >> beer.txt && cat beer.txt

## 8. Escaping characters ##

~$ echo "\"Get out of here,\" said Neil Armstrong to the moon people." >> famous