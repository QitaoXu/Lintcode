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

