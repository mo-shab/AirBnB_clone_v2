-- prepares a MySQL server for the project
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the user if it doesn't exit
CREATE USER IF NOT EXISTS 'hbnb_dev_1'@'localhost' IDENTIFIED BY 'hbnb_Dev_pwd1';
-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev_1'@'localhost';
-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema . * TO 'hbnb_dev_1'@'localhost';
