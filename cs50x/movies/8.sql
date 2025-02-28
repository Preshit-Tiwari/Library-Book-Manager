SELECT name FROM people WHERE people.id in
(SELECT person_id FROM stars WHERE movie_id =
(SELECT movies.id FROM movies WHERE title like 'Toy Story'));
