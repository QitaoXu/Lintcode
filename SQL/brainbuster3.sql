# Connecting 3 tables
SELECT
    film.title, category.name, language.name
FROM 
    film, category, film_category, language
WHERE
    film.language_id = language.language_id AND film.film_id = film_category.film_id AND film_category.category_id = category.category_id
;