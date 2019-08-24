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