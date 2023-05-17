-- a script that creates the DATABASE hbtn_0d_2 and the user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'LOCALHOST' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON  'hbtn_0d_2' TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES; 