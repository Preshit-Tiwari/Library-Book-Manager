SELECT title, rating FROM
ratings JOIN movies WHERE ratings.movie_id = movies.id AND year = 2010 ORDER BY rating DESC,title;
