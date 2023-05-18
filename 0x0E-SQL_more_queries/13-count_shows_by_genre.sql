-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked

USE hbtn_0d_tvshows;
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
INNER JOIN TV_SHOW_
ON tv_genres.ID =tv_genres
ORDER BY number_of_shows
