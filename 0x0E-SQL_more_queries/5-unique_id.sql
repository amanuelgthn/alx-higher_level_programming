-- script that creates unique_id on MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1 ,
    name VARCHAR(256)
);