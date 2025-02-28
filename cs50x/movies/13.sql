 SELECT name FROM people WHERE name <> 'Kevin Bacon' AND people.id in
 (SELECT person_id FROM Stars WHERE movie_id in
 (SELECT movie_id FROM stars WHERE person_id =
 (SELECT people.id FROM people WHERE name = 'Kevin Bacon')));

 --write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
