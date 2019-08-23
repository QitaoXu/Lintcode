# which rating is the most prevelent
SELECT 
    count(film_id), rating
FROM 
    film 
GROUP BY 
    rating 
;

# Which rating is the most prevelent for each rental parice
SELECT 
    count(film_id), rating, rental_rate
from 
    film 
GROUP BY 
    rental_rate
;

SELECT 
    count(rating), rating, rental_rate
from 
    film 
GROUP BY rating, rental_rate
;

SELECT 
    count(film_id)
from 
    film 
WHERE 
    rating = "R" AND rental_rate = .99
;

SELECT 
    rating, rental_rate, count(film_id)
FROM 
    film 
GROUP BY 
    1, 2
;