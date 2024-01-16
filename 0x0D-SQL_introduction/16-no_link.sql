-- Task: List all records of the second_table with scores and names, excluding rows without a name value.

USE hbtn_0c_0;

-- List records with scores and names, excluding rows without a name value
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
