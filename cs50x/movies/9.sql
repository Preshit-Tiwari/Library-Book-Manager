SELECT name FROM people WHERE people.id in
(SELECT person_id FROM stars WHERE movie_id in
(SELECT movies.id FROM movies WHERE year = 2004)) ORDER BY birth;
--write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year
