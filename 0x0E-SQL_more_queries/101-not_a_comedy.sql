-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- I can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command.
SELECT title FROM tv_shows
WHERE title NOT IN (
	SELECT title FROM tv_shows
	JOIN tv_show_genres
	JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id AND 
	tv_shows.id = tv_show_genres.show_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC
