SELECT "first_name" , "last_name"
FROM "players" WHERE "id" = (
    SELECT "player_id" FROM "salaries"
    GROUP BY "player_id", "year"
    HAVING MAX("salary")
    ORDER BY "salary" DESC
    LIMIT 1
);
