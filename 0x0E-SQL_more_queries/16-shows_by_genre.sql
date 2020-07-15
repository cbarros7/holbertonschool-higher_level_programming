-- Only comedy
SELECT tv_shows.title title, tv_genres.name name
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
LEFT OUTER JOIN tv_genres 
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;

