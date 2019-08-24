# How much Revenue has a single store made over PG-13 and R-rated films 
SELECT 
    s.store_id as Store, COUNT(p.amount) AS "Revenue of PG-13 and R"
FROM 
    rental r, inventory i, store s, film f, payment p
WHERE 
    r.inventory_id = i.inventory_id
    AND i.store_id = s.store_id 
    AND i.film_id = f.film_id 
    AND r.rental_id = p.rental_id
    AND f.rating IN ("PG-13", "R")
GROUP BY 
    1
;