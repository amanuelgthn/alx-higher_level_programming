-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_genres.name AS name FROM tv_genres
INNER JOIN tv_show_geners
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.genre_id
WHERE tv_shows.tile = 'Dexter'
ORDER BY tv_genres.name;
