-- Create and use hbtn_0c_0 database
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;

-- Grant privileges to root user
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

-- Write a script that creates a table called first_table in the current database

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
