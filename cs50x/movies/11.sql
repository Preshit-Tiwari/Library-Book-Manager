SELECT title FROM movies JOIN ratings WHERE movies.id = ratings.movie_id AND movies.id in
(SELECT stars.movie_id FROM stars WHERE stars.person_id = (SELECT people.id FROM people WHERE name = 'Chadwick Boseman')) ORDER BY rating DESC LIMIT 5;
--write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
