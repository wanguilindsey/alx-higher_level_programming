-- Task: Remove all records with a score <= 5 in the second_table.

USE hbtn_0c_0;

-- Delete records with a score <= 5
DELETE FROM second_table
WHERE score <= 5;
