SELECT "salary"
FROM "salaries"
WHERE "player_id" =(
    SELECT "player_id"
    FROM "performances"
    WHERE "year" = "2001"
    GROUP BY "player_id"
    ORDER BY "HR" DESC
    LIMIT 1
)
AND "year" = "2001";
