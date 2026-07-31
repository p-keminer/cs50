CREATE TABLE IF NOT EXISTS "movies" (
    "movieId" INTEGER PRIMARY KEY,
    "title" TEXT,
    "genres" TEXT
);

CREATE TABLE IF NOT EXISTS "ratings"(
    "userId" INT ,
    "movieId" INT,
    "rating" REAL DEFAULT NULL,
    "timestamp" INT ,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

CREATE TABLE IF NOT EXISTS "links" (
    "movieId" INTEGER PRIMARY KEY,
    "imdbId" INTEGER ,
    "tmdbId" INTEGER ,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);



CREATE TABLE IF NOT EXISTS "tags" (
    "userId" INTEGER ,
    "movieId" INTEGER ,
    "tag" TEXT ,
    "timestamp" INTEGER,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

DROP VIEW IF EXISTS rating_overview;

CREATE VIEW rating_overview AS
SELECT
    ratings.userId,
    ratings.movieId,
    movies.title,
    movies.genres,
    ratings.rating,
    ratings.timestamp,
    links.imdbId,
    links.tmdbId
FROM ratings
JOIN movies
    ON ratings.movieId = movies.movieId
LEFT JOIN links
    ON ratings.movieId = links.movieId;



