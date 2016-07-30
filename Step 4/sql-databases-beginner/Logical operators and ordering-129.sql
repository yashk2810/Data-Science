## 2. And operator ##

SELECT Major,ShareWomen,Employed FROM recent_grads 
WHERE ShareWomen>0.5 AND Employed>10000 limit 10;

## 3. Or operator ##

select Major, Median, Unemployed from recent_grads where (Median>=10000) OR (Unemployed<=1000) limit 20;

## 6. Order by ##

select Major from recent_grads order by Major DESC limit 10;

## 7. Order using multiple columns ##

select Major_category, Median, Major from recent_grads order by Major asc, Median desc limit 20;