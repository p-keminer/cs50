SELECT "year" , "salary"
FROM "salaries"
WHERE "player_id" = (
    SELECT "id"
    FROM "players"
    WHERE "first_name"
    LIKE "%CAL%" AND "last_name" LIKE "%RIPKEN%"
)
ORDER BY "year" DESC;
