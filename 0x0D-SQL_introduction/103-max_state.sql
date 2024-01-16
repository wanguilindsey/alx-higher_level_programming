-- Task: Display the top 3 cities' temperatures during July and August ordered by temperature (descending).

USE hbtn_0c_0;

-- Calculate the average temperature for July and August by city and order by temperature descending
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
