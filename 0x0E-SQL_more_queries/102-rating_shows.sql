-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- I can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title,
SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC,
title DESC;
