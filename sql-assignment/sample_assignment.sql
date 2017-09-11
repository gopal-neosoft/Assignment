
/* Get customer information with address */
SELECT first_name,last_name,address_id FROM customer;

/*  Add some entries in film table   */
INSERT INTO film (title,description,release_year,language_id) VALUES('Spiderman','The superhero movie',2010,2);

/*  Get the first 10 customers who rented most dvds  */
SELECT CONCAT(customer.first_name,' ',customer.last_name) AS Name ,COUNT(rental.customer_id) AS NumberOfDVDS FROM rental LEFT JOIN customer ON customer.customer_id=rental.customer_id GROUP BY rental.customer_id ORDER BY COUNT(rental.customer_id) DESC,first_name ASC,last_name ASC LIMIT 10 ;

/* Get customers with dvd details for particular customer */

 SELECT c.first_name,c.last_name,r.rental_id,r.rental_date,i.store_id,f.title FROM customer c,rental r,inventory i,film f WHERE c.customer_id=r.customer_id AND r.inventory_id=i.inventory_id AND i.film_id=f.film_id AND c.customer_id=2 ;

/* Get the staff name who sold most dvds*/

SELECT CONCAT(staff.first_name,' ',staff.last_name) AS Name,staff.staff_id, COUNT(staff.staff_id) AS NumberOfDVDS  FROM staff  LEFT JOIN rental ON staff.staff_id=rental.staff_id   GROUP BY staff.staff_id ORDER BY COUNT(staff.staff_id) DESC,first_name ASC,last_name ASC;
