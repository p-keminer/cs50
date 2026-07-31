SELECT "year", "HR"
FROM "performances"
WHERE "player_id" =(
    SELECT "id"
    FROM "players"
    WHERE "first_name"
    LIKE "%KEN%" AND "last_name" LIKE "%GRIFFEY%" AND "birth_year" LIKE "%1969%"
) ORDER BY "year" DESC;
