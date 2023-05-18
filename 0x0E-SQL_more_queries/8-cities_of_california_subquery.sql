-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
SELECT FROM cities WHERE state_id = 1 ORDER BY cities.id ASC;
