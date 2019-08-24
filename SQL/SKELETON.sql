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

# How many times has each movie been rented out?
SELECT 
    film.title, count(rental.rental_id)
FROM
    film, inventory, rental 
WHERE
    film.film_id = inventory.film_id
    AND 
    inventory.inventory_id = rental.inventory_id
GROUP BY
    film.title
;

# revenue per video title 
SELECT 
    f.title AS "Film Title", 
    count(r.rental_id) AS "Rental Times", 
    f.rental_rate AS "Rental Price", 
    count(r.rental_id) * f.rental_rate AS Revenue
FROM
    film f, inventory i, rental r
WHERE
    f.film_id = i.film_id
    AND 
    i.inventory_id = r.inventory_id
GROUP BY
    1
ORDER BY 
    4 desc
;


# SUM()

# What customer has paid us most money 
SELECT 
    c.first_name, c.last_name, SUM(p.amount)
FROM
    payment p, customer c
WHERE
    p.customer_id = c.customer_id
GROUP BY 
    c.customer_id
ORDER BY 
    SUM(p.amount) desc
;

# What store has historically brought the most revenue 
SELECT 
    i.store_id, SUM(p.amount)
FROM
    inventory i, rental r, payment p
WHERE
    r.rental_id = p.rental_id
    AND 
    r.inventory_id = i.inventory_id 
    AND 
    r.rental_id = p.rental_id
GROUP BY 
    i.store_id
ORDER BY 
    SUM(p.amount) desc
;

# How many rentals we had each month, LEFT 
SELECT 
    LEFT(r.rental_date, 7), count(r.rental_id)
FROM
    rental r
GROUP BY 
    1 
;

# MIN MAX 
SELECT 
    f.title AS "Film Name", MIN(r.rental_date), MAX(r.rental_date)
FROM
    rental r, film f, inventory i
WHERE
    r.inventory_id = i.inventory_id
    AND 
    f.film_id = i.film_id
GROUP BY 
    f.film_id
;

# Every customers last rental date 
SELECT 
    CONCAT(c.first_name, " ", c.last_name) AS "Name",
    c.email as Email, 
    MAX(r.rental_date) AS "Last Rental Date"
FROM
    rental r, customer c 
WHERE 
    r.customer_id = c.customer_id
GROUP BY 
    c.customer_id
ORDER BY 
    3 desc
;

# Revenue by Month 

SELECT 
    LEFT(p.payment_date, 7) AS Month, SUM(p.amount) AS Revnue
FROM
    payment p
GROUP BY 
    1
;

# How many distinct rentors per month
SELECT 
    LEFT(r.rental_date, 7) AS Month, 
    COUNT(r.rental_id) AS "Total Rental", 
    COUNT(DISTINCT r.customer_id) AS "Number of Customers", 
    COUNT(r.rental_id) / COUNT(DISTINCT r.customer_id) as Average
FROM 
    rental r
GROUP BY 
    1
;

# Number of distinct films rented each month 
SELECT 
    LEFT(r.rental_date, 7) AS MONTH, 
    COUNT(DISTINCT i.film_id) AS "Number of Rented Films"
FROM 
    rental r, inventory i
WHERE 
    r.inventory_id = i.inventory_id
GROUP BY 
    1 
;

