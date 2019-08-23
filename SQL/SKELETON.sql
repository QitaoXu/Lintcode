SELECT title, rental_rate
FROM film 
WHERE 
rental_rate = .99
;
 
SELECT first_name, last_name
FROM actor 
WHERE 
actor_id = 50
;

SELECT 
    first_name, last_name, email
FROM 
    customer 
WHERE 
    store_id = 2
;

# count function example
SELECT 
    count(title)
FROM 
    film 
;

SELECT 
    count(title)
FROM 
    film 
WHERE 
    rental_rate = 0.99
;

# group by example 
SELECT 
    count(title), rental_rate
FROM 
    film 
GROUP BY 
    rental_rate
;

SELECT 
    count(title), rental_rate
FROM 
    film 
GROUP BY 
    2
;

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

# Connecting table 
# customer id, name(first, last)
# mailing address
SELECT
    customer.customer_id, customer.first_name, customer.last_name, address.address
FROM 
    customer, address
WHERE 
    customer.address_id = address.address_id
;

# Connecting mutiple tables
SELECT
    film.title, category.name, language.name
FROM 
    film, category, film_category, language
WHERE
    film.language_id = language.language_id 
    AND 
    film.film_id = film_category.film_id 
    AND 
    film_category.category_id = category.category_id
;






