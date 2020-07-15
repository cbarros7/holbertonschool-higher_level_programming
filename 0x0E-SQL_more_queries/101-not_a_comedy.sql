-- Only comedy
SELECT tv_shows.title title
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
JOIN tv_genres 
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name NOT LIKE '%Comedy%'
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;

