CREATE TABLE "meteorites" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT,
    "class" TEXT,
    "mass" INTEGER,
    "discovery" TEXT CHECK("discovery" IN ('Fell','Found')),
    "year" INTEGER,
    "lat" FLOAT,
    "long" FLOAT
);

CREATE TABLE "meteorites_temp" (
    "name" TEXT,
    "id" INTEGER PRIMARY KEY,
    "nametype" TEXT,
    "class" TEXT,
    "mass" INTEGER,
    "discovery" TEXT CHECK("discovery" IN ('Fell','Found')),
    "year" INTEGER,
    "lat" FLOAT,
    "long" FLOAT
);

.import --csv --skip 1 meteorites.csv meteorites_temp

DELETE FROM "meteorites_temp" WHERE "nametype" = "Relict";

ALTER TABLE "meteorites_temp" DROP COLUMN "nametype";

UPDATE "meteorites_temp"
SET "mass" = NULL WHERE "mass" = '';
UPDATE "meteorites_temp"
SET "year" = NULL WHERE "year" = '';
UPDATE "meteorites_temp"
SET "lat" = NULL WHERE "lat" = '';
UPDATE "meteorites_temp"
SET "long" = NULL WHERE "long" = '';

UPDATE "meteorites_temp"
SET
    "mass" = ROUND("mass",2),
    "lat" = ROUND("lat",2),
    "long" = ROUND("long",2);

INSERT INTO "meteorites" ("name","class","mass","discovery","year","lat","long")
SELECT "name","class","mass","discovery","year","lat","long"
FROM "meteorites_temp"
ORDER BY "year", "name";


cat import.sql | sqlite3 meteorites.db
