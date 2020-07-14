-- My genres
SELECT tv_genres.name name
FROM tv_genres
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id 
WHERE tv_show_genres.show_id = 8
GROUP BY tv_genres.name, tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;

