--- /* Augmented Query 0 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
ORDER BY channel, col_name, d_year, d_qoy, i_category
LIMIT 200;

--- /* Augmented Query 1 */
SELECT channel, col_name, d_year, d_qoy, d_month, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, d_month, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, d_month, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, d_month, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, d_month, i_category
ORDER BY channel, col_name, d_year, d_qoy, d_month, i_category;

--- /* Augmented Query 2 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL AND i_category = 'Electronics'
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL AND i_category = 'Electronics'
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL AND i_category = 'Electronics'
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
ORDER BY channel, col_name, d_year, d_qoy, i_category;

--- /* Augmented Query 3 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
ORDER BY channel, col_name, d_year, d_qoy, i_category;

--- /* Augmented Query 4 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, AVG(ext_sales_price) sales_amt_avg
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
ORDER BY channel, col_name, d_year, d_qoy, i_category;

--- /* Augmented Query 5 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
HAVING COUNT(*) > 50
ORDER BY channel, col_name, d_year, d_qoy, i_category;

--- /* Augmented Query 6 */
SELECT channel, d_year, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, d_year, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, d_year, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, d_year, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, d_year
ORDER BY channel, d_year;

--- /* Augmented Query 7 */
SELECT channel, col_name, d_year, d_qoy, i_category, c_customer_id, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price, ss_customer_sk
  FROM store_sales, item, date_dim, customer
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  AND ss_customer_sk=c_customer_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price, ws_bill_customer_sk
  FROM web_sales, item, date_dim, customer
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  AND ws_bill_customer_sk=c_customer_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price, cs_bill_customer_sk
  FROM catalog_sales, item, date_dim, customer
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
  AND cs_bill_customer_sk=c_customer_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category, c_customer_id
ORDER BY channel, col_name, d_year, d_qoy, i_category, c_customer_id;

--- /* Augmented Query 8 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
ORDER BY channel, col_name, d_year, d_qoy, i_category;

--- /* Augmented Query 9 */
SELECT channel, col_name, d_year, d_qoy, i_category, COUNT(*) sales_cnt, SUM(ext_sales_price) sales_amt
FROM (
  SELECT 'store' AS channel, 'ss_hdemo_sk' col_name, d_year, d_qoy, i_category, ss_ext_sales_price ext_sales_price
  FROM store_sales, item, date_dim
  WHERE ss_hdemo_sk IS NULL AND d_year = 2020
  AND ss_sold_date_sk=d_date_sk
  AND ss_item_sk=i_item_sk
  UNION ALL
  SELECT 'web' AS channel, 'ws_ship_mode_sk' col_name, d_year, d_qoy, i_category, ws_ext_sales_price ext_sales_price
  FROM web_sales, item, date_dim
  WHERE ws_ship_mode_sk IS NULL AND d_year = 2020
  AND ws_sold_date_sk=d_date_sk
  AND ws_item_sk=i_item_sk
  UNION ALL
  SELECT 'catalog' AS channel, 'cs_ship_customer_sk' col_name, d_year, d_qoy, i_category, cs_ext_sales_price ext_sales_price
  FROM catalog_sales, item, date_dim
  WHERE cs_ship_customer_sk IS NULL AND d_year = 2020
  AND cs_sold_date_sk=d_date_sk
  AND cs_item_sk=i_item_sk
) foo
GROUP BY channel, col_name, d_year, d_qoy, i_category
ORDER BY channel, col_name, d_year, d_qoy, i_category;

--- /* Augmented Query 10 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 5
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 11 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price, date_dim.d_year
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax, date_dim.d_year
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city, date_dim.d_year
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number, date_dim.d_year
LIMIT 100;

--- /* Augmented Query 12 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 4 OR household_demographics.hd_vehicle_count= 4)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 13 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, avg_extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, avg(ss_ext_sales_price) avg_extended_price, sum(ss_ext_tax) extended_tax, sum(ss_ext_list_price) list_price
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 14 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Springfield','Shelbyville')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 15 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 50;

--- /* Augmented Query 16 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND household_demographics.hd_age BETWEEN 30 AND 40
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 17 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2001,2002,2003)
    AND store.s_city IN ('Walnut Grove','Enterprise')
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 18 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
    AND store.s_county = 'Springfield'
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 19 */
SELECT c_last_name, c_first_name, ca_city, bought_city, ss_ticket_number, extended_price, extended_tax, list_price
FROM (
  SELECT ss_ticket_number, ss_customer_sk, ca_city bought_city, sum(ss_ext_sales_price) extended_price, sum(ss_ext_list_price) list_price, sum(ss_ext_tax) extended_tax
  FROM store_sales, date_dim, store, household_demographics, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
    AND store_sales.ss_store_sk = store.s_store_sk
    AND store_sales.ss_hdemo_sk = household_demographics.hd_demo_sk
    AND store_sales.ss_addr_sk = customer_address.ca_address_sk
    AND date_dim.d_dom BETWEEN 1 AND 2
    AND (household_demographics.hd_dep_count = 3 OR household_demographics.hd_vehicle_count= 3)
    AND date_dim.d_year IN (2000,2001,2002)
    AND store.s_city IN ('Walnut Grove','Enterprise')
    AND store.s_gmt_offset = -8
  GROUP BY ss_ticket_number, ss_customer_sk, ss_addr_sk, ca_city
) dn, customer, customer_address current_addr
WHERE ss_customer_sk = c_customer_sk
  AND customer.c_current_addr_sk = current_addr.ca_address_sk
  AND current_addr.ca_city <> bought_city
ORDER BY c_last_name, ss_ticket_number
LIMIT 100;

--- /* Augmented Query 20 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 7
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'blue'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 21 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.1 * AVG(netpaid) FROM ssales)  -- Adjusted percentage
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 22 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, i_color, i_size, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name, i_color, i_size
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name, i_color, i_size;

--- /* Augmented Query 23 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime' AND i_size = 'M'  -- Filter for medium size
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 24 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales
  JOIN store_returns ON ss_ticket_number = sr_ticket_number AND ss_item_sk = sr_item_sk
  JOIN store ON ss_store_sk = s_store_sk
  JOIN item ON ss_item_sk = i_item_sk
  JOIN customer ON ss_customer_sk = c_customer_sk
  JOIN customer_address ON c_current_addr_sk = ca_address_sk
  JOIN date_dim ON store_sales.ss_sold_date_sk = date_dim.d_date_sk AND d_year = 2020  -- Joined with date_dim for a specific year
  WHERE c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 25 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 26 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
    AND i_manager_id = 5
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 27 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
    AND i_manager_id = 5  -- Filter for a specific manager
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 28 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY s_store_name, c_last_name, c_first_name;

--- /* Augmented  -- Changed order priority Query 29 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
    AND c_birth_year > 1980  -- Filter for customers born after 1980
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 30 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'lime'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 31 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 5
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'navy'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 32 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.1 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 33 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, i_size, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name, i_size
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name, i_size;

--- /* Augmented Query 34 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
    AND i_current_price BETWEEN 50 AND 100
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 35 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_state = 'TX'
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)
SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 36 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
    AND ca_state = s_state
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 37 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
    AND i_manager_id = 10
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 38 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY SUM(netpaid) DESC;

--- /* Augmented Query 39 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> UPPER(ca_country)
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk' OR i_color = 'azure'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 40 */
WITH ssales AS (
  SELECT c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size, SUM(ss_net_paid_inc_tax) netpaid
  FROM store_sales, store_returns, store, item, customer, customer_address
  WHERE ss_ticket_number = sr_ticket_number
    AND ss_item_sk = sr_item_sk
    AND ss_customer_sk = c_customer_sk
    AND ss_item_sk = i_item_sk
    AND ss_store_sk = s_store_sk
    AND c_current_addr_sk = ca_address_sk
    AND c_birth_country <> 'USA'
    AND s_zip = ca_zip
    AND s_market_id = 8
  GROUP BY c_last_name, c_first_name, s_store_name, ca_state, s_state, i_color, i_current_price, i_manager_id, i_units, i_size
)

SELECT c_last_name, c_first_name, s_store_name, SUM(netpaid) paid
FROM ssales
WHERE i_color = 'cornsilk'
GROUP BY c_last_name, c_first_name, s_store_name
HAVING SUM(netpaid) > (SELECT 0.05 * AVG(netpaid) FROM ssales)
ORDER BY c_last_name, c_first_name, s_store_name;

--- /* Augmented Query 41 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 42 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Electronics') AND
    i_class IN ('portable','reference') AND
    i_brand IN ('scholaramalgamalg #14','exportiunivamalg #9'))
    OR (i_category IN ('Women','Men') AND
    i_class IN ('accessories','fragrances') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 43 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END < 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 44 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 50;

--- /* Augmented  -- Adjusted limit Query 45 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand NOT IN ('scholaramalgamalg #14'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand NOT IN ('edu packscholar #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 46 */
SELECT * FROM (
  SELECT i_manufact_id,
    AVG(ss_sales_price) avg_sales,
    AVG(AVG(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(avg_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, avg_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 47 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics', 'Home & Garden') AND
    i_class IN ('personal','portable','reference','self-help', 'gardening') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men', 'Sports') AND
    i_class IN ('accessories','classical','fragrances','pants', 'athletic') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 48 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 49 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('scholaramalgamalg #14','scholaramalgamalg #7',
    'exportiunivamalg #9','scholaramalgamalg #9'))
    OR (i_category IN ('Women','Music','Men') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('amalgimporto #1','edu packscholar #1','exportiimporto #1',
    'importoamalg #1')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY i_manufact_id, avg_quarterly_sales, sum_sales
LIMIT 100;

--- /* Augmented Query 50 */
SELECT * FROM (
  SELECT i_manufact_id,
    SUM(ss_sales_price) sum_sales,
    AVG(SUM(ss_sales_price)) OVER (PARTITION BY i_manufact_id) avg_quarterly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
    ss_sold_date_sk = d_date_sk AND
    ss_store_sk = s_store_sk AND
    d_month_seq IN (1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224)
    AND ((i_category IN ('Books','Children','Electronics', 'Toys', 'Fashion') AND
    i_class IN ('personal','portable','reference','self-help') AND
    i_brand IN ('brand #1', 'brand #2'))
    OR (i_category IN ('Women','Music','Men', 'Sports', 'Outdoor') AND
    i_class IN ('accessories','classical','fragrances','pants') AND
    i_brand IN ('brand #3', 'brand #4')))
  GROUP BY i_manufact_id, d_qoy
) tmp1
WHERE CASE WHEN avg_quarterly_sales > 0
  THEN ABS(sum_sales - avg_quarterly_sales) / avg_quarterly_sales
  ELSE NULL END > 0.1
ORDER BY avg_quarterly_sales, sum_sales, i_manufact_id
LIMIT 100;

--- /* Augmented Query 51 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 85
  AND d_moy = 11
  AND d_year = 2003
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 52 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 6
  AND d_year = 2002
  AND d_day_of_week = 'Monday'
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 53 */
SELECT i_category category,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year = 2002
GROUP BY i_category
ORDER BY ext_price DESC
LIMIT 100;

--- /* Augmented Query 54 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year = 2002
GROUP BY i_brand, i_brand_id
ORDER BY i_brand, ext_price DESC
LIMIT 100;

--- /* Augmented Query 55 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year = 2002
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 50;

--- /* Augmented Query 56 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year = 2002
  AND i_color = 'red'
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 57 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year BETWEEN 2000 AND 2002
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 58 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year = 2002
  AND i_brand NOT IN ('Brand#123', 'Brand#456')
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 59 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 96
  AND d_moy = 12
  AND d_year = 2002
  AND i_class = 'luxury'
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 60 */
SELECT i_brand_id brand_id, i_brand brand,
  SUM(ss_ext_sales_price) ext_price
FROM date_dim, store_sales, item
WHERE d_date_sk = ss_sold_date_sk
  AND ss_item_sk = i_item_sk
  AND i_manager_id = 88
  AND d_moy = 12
  AND d_year = 2002
  AND i_category = 'Electronics'
GROUP BY i_brand, i_brand_id
ORDER BY ext_price DESC, i_brand_id
LIMIT 100;

--- /* Augmented Query 61 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2002
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'CA'
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 62 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.5
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 63 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state IN ('TX', 'CA', 'NY')
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 64 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY ctr_total_return DESC
LIMIT 50;

--- /* Augmented Query 65 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return < (SELECT AVG(ctr_total_return)*0.8
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 66 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
  AND c_birth_year <> 1980
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 67 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY ctr_total_return ASC, c_customer_id
LIMIT 100;

--- /* Augmented Query 68 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
  AND c_preferred_cust_flag = 'Y'
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 69 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2001
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state = 'MI'
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 200;

--- /* Augmented Query 70 */
WITH customer_total_return AS (
  SELECT wr_returning_customer_sk AS ctr_customer_sk,
  ca_state AS ctr_state,
  SUM(wr_return_amt) AS ctr_total_return
  FROM web_returns, date_dim, customer_address
  WHERE wr_returned_date_sk = d_date_sk
  AND d_year = 2003
  AND wr_returning_addr_sk = ca_address_sk
  GROUP BY wr_returning_customer_sk, ca_state
)

SELECT c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
FROM customer_total_return ctr1, customer_address, customer
WHERE ctr1.ctr_total_return > (SELECT AVG(ctr_total_return)*1.2
  FROM customer_total_return ctr2
  WHERE ctr1.ctr_state = ctr2.ctr_state)
  AND ca_address_sk = c_current_addr_sk
  AND ca_state NOT IN ('MI', 'CA')
  AND ctr1.ctr_customer_sk = c_customer_sk
ORDER BY c_customer_id, c_salutation, c_first_name, c_last_name, c_preferred_cust_flag,
  c_birth_day, c_birth_month, c_birth_year, c_birth_country, c_login, c_email_address,
  c_last_review_date, ctr_total_return
LIMIT 100;

--- /* Augmented Query 71 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Women', 'Sports', 'Books')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-05-01' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-05-01'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 72 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category = 'Electronics'
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 15, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 73 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Jewelry', 'Home & Garden', 'Tools')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 200;

--- /* Augmented Query 74 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Men', 'Electronics', 'Music')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY itemrevenue DESC
LIMIT 100;

--- /* Augmented Query 75 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_category) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Men', 'Electronics', 'Music')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 76 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Men', 'Electronics', 'Music')
  AND i_class NOT IN ('portable', 'classical')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 77 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Men', 'Electronics', 'Music')
  AND i_current_price > 100
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 78 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Men', 'Electronics', 'Music')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN DATEADD(day, -15, TO_DATE('2001-03-09'))
  AND DATEADD(day, 15, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 79 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY i_category
  ,i_class
  ,i_item_id
  ,i_item_desc
  ,revenueratio
LIMIT 100;

--- /* Augmented Query 80 */
SELECT i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
  ,SUM(cs_ext_sales_price) AS itemrevenue
  ,SUM(cs_ext_sales_price)*100/SUM(SUM(cs_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM catalog_sales
  ,item
  ,date_dim
WHERE cs_item_sk = i_item_sk
  AND i_category IN ('Men', 'Electronics', 'Music')
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2001-03-09' AS DATE)
  AND DATEADD(day, 30, TO_DATE('2001-03-09'))
GROUP BY i_item_id
  ,i_item_desc
  ,i_category
  ,i_class
  ,i_current_price
ORDER BY revenueratio, i_category
LIMIT 100;

--- /* Augmented Query 81 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Books', 'Sports', 'Home')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(month,1,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 82 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category = 'Electronics'
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,15,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 83 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_category) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 84 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND i_class NOT IN ('casual', 'portable')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 85 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND i_current_price > 100
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 86 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY itemrevenue DESC
LIMIT 50;

--- /* Augmented Query 87 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/(SELECT SUM(ws_ext_sales_price) FROM web_sales) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 88 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Books', 'Home', 'Garden')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 89 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND ws_sold_date_sk = d_date_sk
  AND d_date BETWEEN CAST('2002-04-12' AS DATE)
  AND DATEADD(day,30,TO_DATE('2002-04-12'))
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY revenueratio, i_category
LIMIT 100;

--- /* Augmented Query 90 */
SELECT i_item_id, i_item_desc, i_category, i_class, i_current_price,
  SUM(ws_ext_sales_price) AS itemrevenue,
  SUM(ws_ext_sales_price)*100/SUM(SUM(ws_ext_sales_price)) OVER
  (PARTITION BY i_class) AS revenueratio
FROM web_sales, item, date_dim
WHERE ws_item_sk = i_item_sk
  AND i_category IN ('Shoes', 'Children', 'Electronics')
  AND ws_sold_date_sk = d_date_sk
  AND d_year = 2002
GROUP BY i_item_id, i_item_desc, i_category, i_class, i_current_price
ORDER BY i_category, i_class, i_item_id, i_item_desc, revenueratio
LIMIT 100;

--- /* Augmented Query 91 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2003
     AND d_moy = 8)
  AND i.i_current_price > 1.1 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 5
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 92 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND i.i_category = 'Electronics'
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 5
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 93 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND i.i_category = 'Electronics'
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 5
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 94 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 100
GROUP BY a.ca_state
HAVING COUNT(*) >= 10
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 95 */
SELECT a.ca_state state, SUM(s.ss_quantity) AS total_quantity
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING SUM(s.ss_quantity) > 100
ORDER BY total_quantity DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 96 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND i.i_category NOT IN ('Furniture', 'Home Appliances')
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 10
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 97 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 50
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 98 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND a.ca_state IN ('CA', 'NY', 'TX')
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 10
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 99 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2003
     AND d_moy = 12)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 10
ORDER BY cnt DESC, a.ca_state
LIMIT 100;

--- /* Augmented Query 100 */
SELECT a.ca_state state, COUNT(*) cnt
FROM customer_address a, customer c, store_sales s, date_dim d, item i
WHERE a.ca_address_sk = c.c_current_addr_sk
  AND c.c_customer_sk = s.ss_customer_sk
  AND s.ss_sold_date_sk = d.d_date_sk
  AND s.ss_item_sk = i.i_item_sk
  AND d.d_month_seq =
    (SELECT DISTINCT (d_month_seq)
     FROM date_dim
     WHERE d_year = 2002
     AND d_moy = 7)
  AND i.i_current_price > 1.2 *
    (SELECT AVG(j.i_current_price)
     FROM item j
     WHERE j.i_category = i.i_category)
GROUP BY a.ca_state
HAVING COUNT(*) >= 10
ORDER BY a.ca_state, cnt DESC
LIMIT 100;

--- /* Augmented Query 101 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (SUBSTR(ca_zip,1,5) IN ('12345', '67890', '54321', '98765', '24680',
  '13579', '19283', '37465', '92837')
  OR ca_state IN ('NY', 'NJ', 'PA', 'CT')
  OR cs_sales_price > 500)
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 2 AND d_year = 2000
GROUP BY ca_zip
ORDER BY ca_zip
LIMIT 100;

--- /* Augmented Query 102 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (SUBSTR(ca_zip,1,5) IN ('85669', '86197', '88274', '83405', '86475')
  OR ca_state IN ('CA', 'WA', 'GA')
  OR cs_sales_price > 1000)
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 1 AND d_year = 2001
GROUP BY ca_zip
ORDER BY ca_zip
LIMIT 100;

--- /* Augmented Query 103 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (SUBSTR(ca_zip,1,5) NOT IN ('99999', '00000')
  OR ca_state IN ('TX', 'FL', 'IL')
  OR cs_sales_price > 250)
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 4 AND d_year = 2000
GROUP BY ca_zip
ORDER BY ca_zip
LIMIT 100;

--- /* Augmented Query 104 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (SUBSTR(ca_zip,1,5) IN ('12345', '54321', '67890', '09876', '56789')
  OR ca_state IN ('OR', 'MT', 'ID')
  OR cs_sales_price BETWEEN 100 AND 500)
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 3 AND d_year = 2000
GROUP BY ca_zip
ORDER BY ca_zip
LIMIT 100;

--- /* Augmented Query 105 */
SELECT YEAR(d_date) as sale_year, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (SUBSTR(ca_zip,1,5) IN ('11111', '22222', '33333')
  OR ca_state IN ('MI', 'OH', 'IN')
  OR cs_sales_price > 750)
  AND cs_sold_date_sk = d_date_sk
  AND d_year BETWEEN 1999 AND 2001
GROUP BY YEAR(d_date)
ORDER BY sale_year
LIMIT 100;

--- /* Augmented Query 106 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (ca_state NOT IN ('NV', 'UT', 'AZ')
  OR cs_sales_price > 1500)
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 1 AND d_year = 2000
GROUP BY ca_zip
ORDER BY ca_zip
LIMIT 100;

--- /* Augmented Query 107 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND cs_sales_price > 2000
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 2 AND d_year = 2000
GROUP BY ca_zip
ORDER BY ca_zip
LIMIT 100;

--- /* Augmented Query 108 */
SELECT ca_zip, SUM(cs_sales_price) AS total_sales
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND (SUBSTR(ca_zip,1,5) IN ('10101', '20202', '30303')
  OR ca_state IN ('NY', 'MA', 'CT')
  OR cs_sales_price > 300)
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 2 AND d_year = 2000
GROUP BY ca_zip
ORDER BY total_sales DESC, ca_zip
LIMIT 100;

--- /* Augmented Query 109 */
SELECT ca_zip, COUNT(*) AS num_sales
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND cs_sold_date_sk = d_date_sk
  AND d_qoy = 2 AND d_year = 2000
GROUP BY ca_zip
HAVING COUNT(*) > 20
ORDER BY num_sales DESC, ca_zip
LIMIT 100;

--- /* Augmented Query 110 */
SELECT ca_zip, SUM(cs_sales_price)
FROM catalog_sales, customer, customer_address, date_dim
WHERE cs_bill_customer_sk = c_customer_sk
  AND c_current_addr_sk = ca_address_sk
  AND d_date BETWEEN '2000-04-01' AND '2000-04-07'
  AND cs_sold_date_sk = d_date_sk
GROUP BY ca_zip
ORDER BY SUM(cs_sales_price) DESC, ca_zip
LIMIT 100;

--- /* Augmented Query 111 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_brand, s_store_name, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year IN (2001) AND
  ((i_category IN ('Books','Men','Children') AND
  i_class IN ('novels','pants','toys'))
  OR (i_category IN ('Music','Accessories','Health') AND
  i_class IN ('pop','watches','supplements')))
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.1
ORDER BY sum_sales - avg_monthly_sales, s_store_name
LIMIT 100;

--- /* Augmented Query 112 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_brand, s_store_name, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year BETWEEN 2000 AND 2002 AND
  i_brand IN ('Brand#123', 'Brand#456', 'Brand#789')
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.2  -- Adjusted threshold
ORDER BY sum_sales - avg_monthly_sales DESC, s_store_name  -- Changed order direction
LIMIT 100;

--- /* Augmented Query 113 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_brand, s_store_name, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year IN (2000)
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END <= 0.1  -- Focused on lower variance
ORDER BY avg_monthly_sales DESC, s_store_name
LIMIT 100;

--- /* Augmented Query 114 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_brand, s_store_name, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_moy = 12 AND
  d_year IN (2000) AND
  i_category NOT IN ('Electronics', 'Women')
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.1
ORDER BY sum_sales DESC, s_store_name
LIMIT 100;

--- /* Augmented Query 115 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_brand, s_store_name, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year IN (2000) AND
  ss_sales_price > 200
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.1
ORDER BY sum_sales DESC, s_store_name
LIMIT 100;

--- /* Augmented Query 116 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_brand, s_store_name, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year IN (2000)
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.5  -- Increased threshold for variance
ORDER BY sum_sales DESC, s_store_name
LIMIT 100;

--- /* Augmented Query 117 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, i_class, s_store_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  i_brand = 'Brand#123'
  AND d_year IN (2000)
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.1
ORDER BY sum_sales DESC, s_store_name
LIMIT 100;

--- /* Augmented Query 118 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, s_company_name, d_moy)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_moy = 6 AND
  d_year BETWEEN 1999 AND 2001
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.1
ORDER BY sum_sales DESC, s_store_name
LIMIT 100;

--- /* Augmented Query 119 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY s_store_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year IN (2000)
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.2
ORDER BY avg_monthly_sales, s_store_name
LIMIT 100;

--- /* Augmented Query 120 */
SELECT *
FROM (
  SELECT i_category, i_class, i_brand,
  s_store_name, s_company_name,
  d_moy,
  SUM(ss_sales_price) sum_sales,
  AVG(SUM(ss_sales_price)) OVER
  (PARTITION BY i_category, s_company_name)
  avg_monthly_sales
  FROM item, store_sales, date_dim, store
  WHERE ss_item_sk = i_item_sk AND
  ss_sold_date_sk = d_date_sk AND
  ss_store_sk = s_store_sk AND
  d_year IN (2000)
  GROUP BY i_category, i_class, i_brand,
  s_store_name, s_company_name, d_moy
) tmp1
WHERE CASE WHEN (avg_monthly_sales <> 0) THEN (ABS(sum_sales - avg_monthly_sales) / avg_monthly_sales) ELSE NULL END > 0.1
ORDER BY ABS(sum_sales - avg_monthly_sales) DESC, i_category
LIMIT 100;

--- /* Augmented Query 121 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name, d_date
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND d_month_seq BETWEEN 1200 AND 1200 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name, d_date
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND d_month_seq BETWEEN 1200 AND 1200 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name, d_date
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND d_month_seq BETWEEN 1200 AND 1200 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 122 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name, d_date
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND d_month_seq = 1176
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name, d_date
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND d_month_seq = 1176
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name, d_date
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND d_month_seq = 1176
) hot_cust
LIMIT 100;

--- /* Augmented Query 123 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND ss_sales_price > 500
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND cs_sales_price > 500
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND ws_sales_price > 500
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 124 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales JOIN date_dim ON store_sales.ss_sold_date_sk = date_dim.d_date_sk
  JOIN customer ON store_sales.ss_customer_sk = customer.c_customer_sk
  JOIN item ON store_sales.ss_item_sk = item.i_item_sk
  WHERE i_category NOT IN ('Electronics', 'Clothing')
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales JOIN date_dim ON catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  JOIN customer ON catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  JOIN item ON catalog_sales.cs_item_sk = item.i_item_sk
  WHERE i_category NOT IN ('Electronics', 'Clothing')
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales JOIN date_dim ON web_sales.ws_sold_date_sk = date_dim.d_date_sk
  JOIN customer ON web_sales.ws_bill_customer_sk = customer.c_customer_sk
  JOIN item ON web_sales.ws_item_sk = item.i_item_sk
  WHERE i_category NOT IN ('Electronics', 'Clothing')
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 125 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND c_preferred_cust_flag = 'Y'
  AND d_month_seq BETWEEN 1300 AND 1300 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND c_preferred_cust_flag = 'Y'
  AND d_month_seq BETWEEN 1300 AND 1300 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND c_preferred_cust_flag = 'Y'
  AND d_month_seq BETWEEN 1300 AND 1300 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 126 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND d_date = CAST(c_birth_year || '-' || c_birth_month || '-' || c_birth_day AS DATE)
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND d_date = CAST(c_birth_year || '-' || c_birth_month || '-' || c_birth_day AS DATE)
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND d_date = CAST(c_birth_year || '-' || c_birth_month || '-' || c_birth_day AS DATE)
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 127 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND d_year = 2000
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND d_year = 2001
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND d_year = 2002
) hot_cust
LIMIT 100;

--- /* Augmented Query 128 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales JOIN date_dim ON store_sales.ss_sold_date_sk = date_dim.d_date_sk
  JOIN customer ON store_sales.ss_customer_sk = customer.c_customer_sk
  WHERE ss_net_profit > 1000
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales JOIN date_dim ON catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  JOIN customer ON catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  WHERE cs_net_profit > 1000
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales JOIN date_dim ON web_sales.ws_sold_date_sk = date_dim.d_date_sk
  JOIN customer ON web_sales.ws_bill_customer_sk = customer.c_customer_sk
  WHERE ws_net_profit > 1000
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 129 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales, date_dim, customer, customer_address
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND customer.c_current_addr_sk = customer_address.ca_address_sk
  AND ca_state IN ('CA', 'TX', 'NY')
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales, date_dim, customer, customer_address
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND customer.c_current_addr_sk = customer_address.ca_address_sk
  AND ca_state IN ('CA', 'TX', 'NY')
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales, date_dim, customer, customer_address
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND customer.c_current_addr_sk = customer_address.ca_address_sk
  AND ca_state IN ('CA', 'TX', 'NY')
  AND d_month_seq BETWEEN 1176 AND 1176 + 11
) hot_cust
LIMIT 100;

--- /* Augmented Query 130 */
SELECT COUNT(*) FROM (
  SELECT DISTINCT c_last_name, c_first_name
  FROM store_sales, date_dim, customer
  WHERE store_sales.ss_sold_date_sk = date_dim.d_date_sk
  AND store_sales.ss_customer_sk = customer.c_customer_sk
  AND d_date = '2000-11-24'
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM catalog_sales, date_dim, customer
  WHERE catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
  AND catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
  AND d_date = '2000-11-24'
  INTERSECT
  SELECT DISTINCT c_last_name, c_first_name
  FROM web_sales, date_dim, customer
  WHERE web_sales.ws_sold_date_sk = date_dim.d_date_sk
  AND web_sales.ws_bill_customer_sk = customer.c_customer_sk
  AND d_date = '2000-11-24'
) hot_cust
LIMIT 100;
