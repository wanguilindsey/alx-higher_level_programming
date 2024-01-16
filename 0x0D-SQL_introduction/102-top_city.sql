-- Task: Display the top 3 cities' temperature during July and August ordered by temperature (descending).

USE hbtn_0c_0;

-- Calculate the average temperature during July and August by city and order by temperature descending
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
