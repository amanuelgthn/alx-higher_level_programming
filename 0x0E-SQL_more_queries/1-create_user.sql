-- script that creates the MYSQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'LOCALHOST' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;