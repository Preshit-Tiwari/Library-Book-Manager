SELECT name FROM people where people.id in
(SELECT person_id FROM directors WHERE movie_id in
(SELECT movie_id FROM ratings WHERE rating >= 9.0 ) );
--write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
