-- Task: List the number of records with the same score in the second_table.

USE hbtn_0c_0;

-- List the score and the number of records for each score
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
