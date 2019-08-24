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