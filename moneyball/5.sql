SELECT "name"
FROM "teams"
WHERE "id" IN (
    SELECT "team_id"
    FROM "performances"
    WHERE "player_id" =(
        SELECT "id"
        FROM "players"
        WHERE "first_name" LIKE "%SATCHEL%"
        AND "last_name" LIKE "%PAIGE%"
    )GROUP BY "team_id"
);
