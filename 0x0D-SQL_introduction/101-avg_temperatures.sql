-- List all tables in the hbtn_0c_0 database
SHOW TABLES;

-- Update the script with the correct table name
USE hbtn_0c_0;

-- Calculate the average temperature by city and order by temperature descending
SELECT city, AVG(temperature) AS avg_temp
FROM correct_table_name  -- Replace with the correct table name
GROUP BY city
ORDER BY avg_temp DESC;
