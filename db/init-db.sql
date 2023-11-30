-- Change DB_USER, DB_USER and DB_PASSWORD to the same environment variables
-- that is used with docker build --build-args

CREATE DATABASE IF NOT EXISTS DB_NAME;
USE DB_NAME;

CREATE USER {DB_USER}@'%' IDENTIFIED BY {DB_PASSWORD};
GRANT ALL PRIVILEGES ON DB_NAME.* TO {DB_USER}@'%';
FLUSH PRIVILEGES;
