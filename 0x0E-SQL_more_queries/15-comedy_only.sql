-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
USE hbtn_0d_tvshows;
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres
ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id ASC;
