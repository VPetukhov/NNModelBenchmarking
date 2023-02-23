## Model: T5-3B, finetuned on spider

Correct total: [10/26]

- \[easy\]: [7/8]
- \[medium\]: [3/11]
- \[hard\]: [0/7]


- \[column insertion\]: [0/4] (this model seems to only be capable of selects)

---

Question [easy]: How many singers do we have?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select count(*) from singer`

Is correct?: Yes 🟢

---

Question [easy]: What is the stadium with the highest capacity?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select name from stadium order by capacity desc limit 1`

Is correct?: Yes 🟢

---

Question [easy]: Which stadium can hold the most people?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select name from stadium order by capacity desc limit 1`

Is correct?: Yes 🟢

---

Question [medium]: What was the place of the latest concert?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select t3.location from concert as t1 join stadium as t2 on t1.stadium_id = t2.stadium_id join singer as t3 on t1.concert_id = t3.singer_id order by t1.year desc limit 1`

Is correct?: No, but close 🟡 (should be select **t2**.location...)

---

Question [medium]: Where was the latest concert of Taylor Swift?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select t3.location from singer_in_concert as t1 join concert as t2 on t1.concert_id = t2.concert_id join singer as t3 on t1.singer_id = t3.singer_id where t3.song_name = "Taylor Swift" and t2.year = 2017`

Is correct?: No 🔴

---

Question [easy]: How much money did we made in total?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select sum(t1.profit) from sales as t1 join products as t2 on t1.product_id = t2.id group by t1.product_id`

Is correct?: No 🔴

---

Question [medium]: What amount of "Lego set Technic 0254" we sold in total?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select sum(t1.amount_in_stock) from products as t1 join sales as t2 on t1.id = t2.product_id where t1.name = "Lego set Technic 0254"`

Is correct?: No 🔴

---

Question [medium]: Which client paid us the highest amount of money?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select t1.name from customers as t1 join sales as t2 on t1.customer_id = t2.customer_id group by t1.customer_id order by sum(t2.amount_in_stock) desc limit 1`

Is correct?: No 🔴

---

Question [medium]: What was the most expensive thing we ever sold

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select max(product_price_at_the_moment_of_transaction_per_unit) from sales`

Is correct?: No 🔴

---

Question [medium]: What was the most expensive thing we sold in the year 2020?

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select max(product_price_per_unit) from sales where datetime = 2020`

Is correct?: No 🔴

---

Question [easy]: What is the most spacious warehouse?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select location from warehouses order by max_storage_volume desc limit 1`

Is correct?: Yes 🟢

---

Question [easy]: What is the total capacity of our warehouses?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select sum(max_storage_volume) from warehouses`

Is correct?: Yes 🟢

---

Question [easy]: Which packages require temperature control?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select * from packages where requires_temperature_control = 'Y'`

Is correct?: Yes 🟢

---

Question [easy]: Which packages require thermostats?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select distinct t1.id from packages as t1 join warehouses as t2 on t1.warehouse_id = t2.warehouse_id where t1.requires_temperature_control = 'Yes'`

Is correct?: Yes, but not optimal (no joins required) 🟡

---

Question [medium]: Which packages are stored in the warehouses equipped with temperature control?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select t1.packages from packages as t1 join warehouses as t2 on t1.warehouse_id = t2.warehouse_id where t2.has_temperature_control = 'Yes'`

Is correct?: No, but close 🟡 (should be select t1.**id** ...)

---

Question [medium]: Which packages are stored in the warehouses with thermostats?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select t1.id from packages as t1 join warehouses as t2 on t1.warehouse_id = t2.warehouse_id where t2.has_temperature_control = 'Yes'`

Is correct?: Yes 🟢 (But why couldn't it do the previous one?)

---

Question [medium]: Who owns the most packages stored in our warehouses?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select t1.name from owners as t1 join packages as t2 on t1.id = t2.owner_id group by t1.id order by count(*) desc limit 1`

Is correct?: Yes 🟢 

---

Question [medium]: Who owns the most packages?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select owner_id from packages group by owner_id order by count(*) desc limit 1`

Is correct?: Yes 🟢 

---

Question [medium]: Which packages are stored in violation of temperature conditions?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select t1.id from packages as t1 join warehouses as t2 on t1.warehouse_id = t2.warehouse_id where t1.requires_temperature_control = 'No'`

Is correct?: No 🟡

---

Question [hard]: Which singers participated in at least 3 rock concerts in Chicago in 2020? Sort them by name and gender.

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select t2.name, t2.is_male from singer_in_concert as t1 join singer as t2 on t1.singer_id = t2.singer_id join concert as t3 on t3.concert_id = t1.concert_id where t3.year = 2020 and t3.concert_name = "Chicago" order by t2.name, t2.is_male`

Is correct?: No 🔴

---

Question [hard]: Which singers participated in at least 3 rock concerts in Chicago in 2020, but never participated in pop concerts?

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select t2.name from singer_in_concert as t1 join singer as t2 on t1.singer_id = t2.singer_id join concert as t3 on t3.concert_id = t1.concert_id where t3.year = 2020 and t3.theme = "Rock" except select t2.name from singer_in_concert as t1 join concert as t2 on t1.concert2.concert3.concert1.singer_id = t2.singer_id join pop concert as t3 on t3.concert3.concert3.concert3.concert3.concert3.concert3.concert3.concert3.concert3.theme = "Pop"`

Is correct?: No 🔴

---

Question [hard]: Which singers participated in at least 3 rock concerts in Chicago in 2020, but never participated in pop concerts? Sort them by their total number of performances.

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select t2.name from singer_in_concert as t1 join singer as t2 on t1.singer_id = t2.singer_id join concert as t3 on t3.concert_id = t1.concert_id where t3.year = 2020 and t2.theme = "Rock" order by count(*)`

Is correct?: No 🔴

---

Question [hard]: Extract top-5 customers, who ordered at least two of the following items last year: "Lego technic kit 23422", "Ninja pocket knife pro", "Pearl necklace 342". Order them by their names.

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select t1.name from customers as t1 join sales as t2 on t1.customer_id = t2.customer_id join products as t3 on t2.product_id = t3.id where t3.name like "%lego technic kit 23422%" group by t1.customer_id having count(*) >= 5`

Is correct?: No 🔴

---

Question [hard]: Extract top-5 customers, who ordered at least two of the following items last year: "Lego technic kit 23422", "Ninja pocket knife pro", "Pearl necklace 342". Order them by their total spendings.

Schema: `| sales_data | sales: transaction_id, volume, product_id, product_price_at_the_moment_of_transaction_per_unit, datetime, customer_id | customers: customer_id, name, location | products: id, name, current_price, amount_in_stock`

Response: `sales_data | select t1.name from customers as t1 join sales as t2 on t1.customer_id = t2.customer_id join products as t3 on t2.product_id = t3.id where t3.name like "%lego technic kit 23422%" group by t1.customer_id order by sum(t2.spending)`

Is correct?: No 🔴

---

Question [hard]: Extract top-3 clients, whose packages are stored in violation of temperature conditions?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select t1.name from owners as t1 join packages as t2 on t1.id = t2.owner_id where t2.requires_temperature_control = 'No' group by t1.id order by count(*) desc limit 3`

Is correct?: No 🔴

---

Question [hard]: Extract top-3 clients, ordered by amount of their packages that are stored in violation of temperature conditions?

Schema: `| warehousing | warehouses : warehouse_id, location, max_storage_volume, has_temperature_control | packages : id, warehouse_id, package_volume, requires_temperature_control, stored_until_date, owner_id | owners : id, name`

Response: `warehousing | select t2.name from packages as t1 join owners as t2 on t1.owner_id = t2.id where t1.requires_temperature_control = 'No' group by t2.name order by sum(t1.package_volume)`

Is correct?:  No 🔴

---

# Column inserting

---

Question [medium]: Add new column to the table "concert", with the amount of singers performed at each concert

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select count(*), t1.concert_id from concert as t1 join singer_in_concert as t2 on t1.concert_id = t2.concert_id group by t1.concert_id`

Is correct?:  No 🔴

---

Question [easy]: Add new column to the table "stadium", equal to 2 * stadium.capacity

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select capacity from stadium`

Is correct?:  No 🔴

---

Question [easy]: Add new column to the table "stadium": double_capacity = 2 * stadium.capacity

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select double_capacity from stadium`

Is correct?:  No 🔴

---

Question [easy]: Add new column to the table "stadium": double_capacity = stadium.capacity / sum(stadium.capacity)

Schema: `| concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id`

Response: `concert_singer | select double_capacity from stadium`

Is correct?:  No 🔴

---

