-- Genre ID by show
SELECT s.title, g.genre_id
FROM tv_shows s
JOIN tv_show_genres g 
ON s.id = g.genre_id 
ORDER BY s.title ASC, g.genre_id ASC;
 
