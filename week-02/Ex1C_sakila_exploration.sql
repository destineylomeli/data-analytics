/*
a) The information included is the actor_id, first_name, last_name, and last_update.
b) The information included is film_id, title, description, release_year, language_id, 
original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, 
special_features, and last_update. 
c) The other table that includes both actor_id and film_id is film_actor. 
d) It's very easy to read mainly because it includes all the key information like rental _id, 
rental_date, inventory_date, customer_id, return_date, staff_id, last_update along with
 the timestamps.
e) Inventory is also easy to read because it mostly contains information of the inventory_id,
 film_id, store_id, and last_update with timestamps.
f) The tables needed are the rental, inventory, and film. The rental table contains the rental 
date and inventory ID for each transactions. While the inventory table connects the inventory ID 
to a specific film ID. The film table contains the title of each film. The way these tables are
 related are through the inventory_id and film_id fields which allow us to link a rental on a specific
 date to the exact film that was rented.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;