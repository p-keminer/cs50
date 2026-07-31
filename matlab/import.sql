PRAGMA foreign_keys = ON;

.mode csv
.import --skip 1 movies.csv movies
.import --skip 1 links.csv links
.import --skip 1 ratings.csv ratings
.import --skip 1 tags.csv tags
