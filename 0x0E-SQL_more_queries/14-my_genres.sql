-- lists all genres of the show Dexter. Each record should display: tv_genres.name
-- must be sorted in ascending order by the genre name
SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_shows.title = "Dexter"
    AND tv_shows.id = tv_show_genres.show_id
    AND tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;
