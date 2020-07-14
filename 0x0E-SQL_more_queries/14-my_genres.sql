-- My genres
SELECT tv_genres.name name
FROM tv_genres
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id 
WHERE tv_shows.title LIKE '%Dexter%'
-- GROUP BY tv_genres.name, tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;

