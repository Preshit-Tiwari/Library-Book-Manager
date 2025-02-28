SELECT title FROM movies WHERE
(movies.id in
(SELECT movie_id FROM stars WHERE person_id =
(SELECT people.id FROM people WHERE name = 'Bradley Cooper'))
 AND movies.id in
(SELECT movie_id FROM stars WHERE person_id =
(SELECT people.id FROM people WHERE name = 'Jennifer Lawrence')));
--write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred
