-- einzelnen Matricwert kontrollieren
SELECT rating FROM rating_overview WHERE movieId = 5 AND userId = 10;

--durchschnittbewertung mit über 173 bewertungen kontrollieren
SELECT
    movieId,
    title,
    COUNT(*) AS count_rating,
    ROUND(AVG(rating), 4) AS avg_rating
FROM rating_overview
GROUP BY movieId, title
HAVING COUNT(*) > 173
ORDER BY avg_rating DESC;

-- top 6 Filme kontrollieren
SELECT
    movieId,
    title,
    COUNT(*) AS rating_count,
    ROUND(AVG(rating), 4) AS avg_rating
FROM rating_overview
GROUP BY movieId, title
HAVING COUNT(*) > 173
ORDER BY AVG(rating) DESC
LIMIT 6;


-- histogramm kontrolieren
SELECT rating
FROM rating_overview
WHERE movieId = (
    SELECT movieId
    FROM rating_overview
    GROUP BY movieId
    HAVING COUNT(*) > 173
    ORDER BY AVG(rating) DESC
    LIMIT 1 OFFSET 2
)
ORDER BY rating;




