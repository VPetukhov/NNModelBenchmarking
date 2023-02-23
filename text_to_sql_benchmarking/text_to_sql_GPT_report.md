## Model: code-davinchi-002

Correct total: [20/26]

- \[easy\]: [6/8]
- \[medium\]: [9/11]
- \[hard\]: [5/7]


- \[column insertion\]: [3/4]

---

Question [easy]: How many singers do we have?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT COUNT(*) FROM singer;`

Is correct?: Yes 🟢

---

Question [easy]: What is the stadium with the highest capacity?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT name, capacity
FROM stadium
WHERE capacity = (SELECT MAX(capacity) FROM stadium)`

Is correct?: Yes 🟢

---

Question [easy]: Which stadium can hold the most people?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT name, capacity
FROM stadium
ORDER BY capacity DESC
LIMIT 1`

Is correct?: Yes 🟢

---

Question [medium]: What was the place of the latest concert?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT stadium.name
FROM stadium
INNER JOIN concert ON stadium.stadium_id = concert.stadium_id
WHERE concert.year = (SELECT MAX(year) FROM concert)`

Is correct?: Yes 🟢

---

Question [medium]: Where was the latest concert of Taylor Swift?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT s.name, s.location, c.year
FROM stadium s
JOIN concert c ON s.stadium_id = c.stadium_id
JOIN singer_in_concert sc ON c.concert_id = sc.concert_id
JOIN singer si ON sc.singer_id = si.singer_id
WHERE si.name = 'Taylor Swift'
ORDER BY c.year DESC
LIMIT 1`

Is correct?: Yes 🟢

---

Question [easy]: How much money did we made in total?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT SUM(volume * product_price_at_the_moment_of_transaction_per_unit) AS total_revenue
FROM sales;`

Is correct?: Yes 🟢

---

Question [medium]: What amount of "Lego set Technic 0254" we sold in total?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT SUM(volume)
FROM sales
WHERE product_id = (SELECT id FROM products WHERE name = "Lego set Technic 0254")`

Is correct?: Yes 🟢

---

Question [medium]: Which client paid us the highest amount of money?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT customers.name, SUM(sales.volume * sales.product_price_at_the_moment_of_transaction_per_unit) AS total_amount
FROM sales
JOIN customers ON customers.customer_id = sales.customer_id
GROUP BY customers.name
ORDER BY total_amount DESC
LIMIT 1;`

Is correct?: No, but very close 🟡 (it should be GROUP BY customers.**customer_id**)

---

Question [medium]: What was the most expensive thing we ever sold

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT
  product_id,
  MAX(product_price_at_the_moment_of_transaction_per_unit) AS max_price
FROM sales
GROUP BY product_id
ORDER BY max_price DESC
LIMIT 1;`

Is correct?: Yes 🟢

---

Question [medium]: What was the most expensive thing we sold in the year 2020?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT product_id, MAX(product_price_at_the_moment_of_transaction_per_unit)
FROM sales
WHERE datetime BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY product_id`

Is correct?: No 🔴

---

Question [easy]: What is the most spacious warehouse?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT warehouses.warehouse_id, warehouses.location, warehouses.max_storage_volume, warehouses.has_temperature_control, SUM(packages.package_volume) AS total_volume
FROM warehouses
LEFT JOIN packages ON warehouses.warehouse_id = packages.warehouse_id
GROUP BY warehouses.warehouse_id
ORDER BY total_volume DESC
LIMIT 1`

Is correct?: No 🔴 

---

Question [easy]: What is the total capacity of our warehouses?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT SUM(max_storage_volume) FROM warehouses;`

Is correct?: Yes 🟢

---

Question [easy]: Which packages require temperature control?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT packages.id, packages.warehouse_id, packages.package_volume, packages.requires_temperature_control, packages.stored_until_date, packages.owner_id
FROM packages
INNER JOIN warehouses ON packages.warehouse_id = warehouses.warehouse_id
WHERE packages.requires_temperature_control = 1 AND warehouses.has_temperature_control = 1`

Is correct?: No 🔴 (But the next one model got right, even when they ask about the same thing)

---

Question [easy]: Which packages require thermostats?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT * FROM packages WHERE requires_temperature_control = 1;`

Is correct?: Yes 🟢 

---

Question [medium]: Which packages are stored in the warehouses equipped with temperature control?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT packages.id, packages.warehouse_id, packages.package_volume, packages.requires_temperature_control, packages.stored_until_date, packages.owner_id
FROM packages
INNER JOIN warehouses ON packages.warehouse_id = warehouses.warehouse_id
WHERE warehouses.has_temperature_control = 1`

Is correct?: Yes 🟢 

---

Question [medium]: Which packages are stored in the warehouses with thermostats?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT packages.id, packages.warehouse_id, packages.package_volume, packages.requires_temperature_control, packages.stored_until_date, packages.owner_id
FROM packages
INNER JOIN warehouses ON packages.warehouse_id = warehouses.warehouse_id
WHERE warehouses.has_temperature_control = 1`

Is correct?: Yes 🟢 

---

Question [medium]: Who owns the most packages stored in our warehouses?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT owners.name, COUNT(packages.id) AS package_count
FROM packages
JOIN owners ON packages.owner_id = owners.id
GROUP BY owners.name
ORDER BY package_count DESC
LIMIT 1;`

Is correct?: Yes 🟢 

---

Question [medium]: Who owns the most packages?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT owners.name, COUNT(packages.id) AS package_count
FROM packages
JOIN owners ON packages.owner_id = owners.id
GROUP BY owners.name
ORDER BY package_count DESC
LIMIT 1;`

Is correct?: Yes 🟢

---

Question [medium]: Which packages are stored in violation of temperature conditions?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT *
FROM packages
WHERE requires_temperature_control = 1
AND warehouse_id IN (
    SELECT warehouse_id
    FROM warehouses
    WHERE has_temperature_control = 0
)`

Is correct?: Yes 🟢 

---

Question [hard]: Which singers participated in at least 3 rock concerts in Chicago in 2020? Sort them by name and gender.

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT singer.name, singer.is_male
FROM singer
INNER JOIN singer_in_concert ON singer.singer_id = singer_in_concert.singer_id
INNER JOIN concert ON singer_in_concert.concert_id = concert.concert_id
WHERE concert.theme = 'rock' AND concert.year = 2020 AND concert.stadium_id IN (
    SELECT stadium.stadium_id
    FROM stadium
    WHERE stadium.location = 'Chicago'
)
GROUP BY singer.name, singer.is_male
HAVING COUNT(*) >= 3
ORDER BY singer.name, singer.is_male`

Is correct?: Yes 🟢 (But a bit overcomplicated)

---

Question [hard]: Which singers participated in at least 3 rock concerts in Chicago in 2020, but never participated in pop concerts?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT singer.name
FROM singer
INNER JOIN singer_in_concert ON singer.singer_id = singer_in_concert.singer_id
INNER JOIN concert ON singer_in_concert.concert_id = concert.concert_id
INNER JOIN stadium ON concert.stadium_id = stadium.stadium_id
WHERE stadium.location = 'Chicago' AND concert.year = 2020 AND concert.theme = 'rock'
GROUP BY singer.name
HAVING COUNT(*) >= 3
EXCEPT
SELECT singer.name
FROM singer
INNER JOIN singer_in_concert ON singer.singer_id = singer_in_concert.singer_id
INNER JOIN concert ON singer_in_concert.concert_id = concert.concert_id
WHERE concert.theme = 'pop'`

Is correct?: Yes 🟢

---

Question [hard]: Which singers participated in at least 3 rock concerts in Chicago in 2020, but never participated in pop concerts? Sort them by their total number of performances.

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `SELECT singer.name, COUNT(*) AS total_performances
FROM singer
INNER JOIN singer_in_concert ON singer.singer_id = singer_in_concert.singer_id
INNER JOIN concert ON singer_in_concert.concert_id = concert.concert_id
WHERE concert.theme = 'rock' AND concert.location = 'Chicago' AND concert.year = 2020
GROUP BY singer.name
HAVING COUNT(*) >= 3 AND COUNT(*) = (
    SELECT COUNT(*)
    FROM singer
    INNER JOIN singer_in_concert ON singer.singer_id = singer_in_concert.singer_id
    INNER JOIN concert ON singer_in_concert.concert_id = concert.concert_id
    WHERE concert.theme = 'rock' AND concert.location = 'Chicago' AND concert.year = 2020 AND singer.name = singer.name
)
ORDER BY total_performances DESC`

Is correct?: No 🔴 

---

Question [hard]: Extract top-5 customers, who ordered at least two of the following items last year: "Lego technic kit 23422", "Ninja pocket knife pro", "Pearl necklace 342". Order them by their names.

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT c.name, SUM(s.volume) AS total_volume
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.id
WHERE p.name IN ('Lego technic kit 23422', 'Ninja pocket knife pro', 'Pearl necklace 342')
AND s.datetime >= '2019-01-01'
AND s.datetime < '2020-01-01'
GROUP BY c.name
HAVING COUNT(DISTINCT p.name) >= 2
ORDER BY total_volume DESC
LIMIT 5`

Is correct?: No, 🟡 (ordered by wrong thing, but otherwise correct)

---

Question [hard]: Extract top-5 customers, who ordered at least two of the following items last year: "Lego technic kit 23422", "Ninja pocket knife pro", "Pearl necklace 342". Order them by their total spendings.

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `SELECT
    c.name,
    SUM(s.volume * s.product_price_at_the_moment_of_transaction_per_unit) AS total_spendings
FROM
    sales AS s
    INNER JOIN customers AS c ON s.customer_id = c.customer_id
    INNER JOIN products AS p ON s.product_id = p.id
WHERE
    p.name IN ('Lego technic kit 23422', 'Ninja pocket knife pro', 'Pearl necklace 342')
    AND s.datetime >= '2019-01-01'
    AND s.datetime < '2020-01-01'
GROUP BY
    c.name
HAVING
    COUNT(DISTINCT p.name) >= 2
ORDER BY
    total_spendings DESC
LIMIT 5`

Is correct?: Yes 🟢

---

Question [hard]: Extract top-3 clients, whose packages are stored in violation of temperature conditions?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT owners.name, COUNT(*) AS count
FROM packages
JOIN owners ON packages.owner_id = owners.id
JOIN warehouses ON packages.warehouse_id = warehouses.warehouse_id
WHERE packages.requires_temperature_control = 1 AND warehouses.has_temperature_control = 0
GROUP BY owners.name
ORDER BY count DESC
LIMIT 3`

Is correct?: Yes 🟢 (Amazing, it even figured out how to reasonably rank them without explicit instructions)

---

Question [hard]: Extract top-3 clients, ordered by amount of their packages that are stored in violation of temperature conditions?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `SELECT owners.name, COUNT(*) AS count
FROM packages
JOIN owners ON packages.owner_id = owners.id
JOIN warehouses ON packages.warehouse_id = warehouses.warehouse_id
WHERE packages.requires_temperature_control = 1 AND warehouses.has_temperature_control = 0
GROUP BY owners.name
ORDER BY count DESC
LIMIT 3`

Is correct?: Yes 🟢

---

# Column inserting

---

Question [medium]: Add new column to the table "concert", with the amount of singers performed at each concert

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `ALTER TABLE concert ADD COLUMN singer_count INTEGER;
UPDATE concert SET singer_count = (SELECT COUNT(*) FROM singer_in_concert WHERE concert_id = concert.concert_id);`

Is correct?: Yes 🟢

---

Question [easy]: Add new column to the table "stadium", equal to 2 * stadium.capacity

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `ALTER TABLE stadium ADD COLUMN double_capacity INTEGER;
UPDATE stadium SET double_capacity = 2 * capacity;`

Is correct?: Yes 🟢

---

Question [easy]: Add new column to the table "stadium": double_capacity = 2 * stadium.capacity

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `ALTER TABLE stadium ADD COLUMN double_capacity INTEGER;
UPDATE stadium SET double_capacity = 2 * capacity;`

Is correct?: Yes 🟢

---

Question [easy]: Add new column to the table "stadium": double_capacity = stadium.capacity / sum(stadium.capacity)

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: ``

Is correct?: No 🔴

---
