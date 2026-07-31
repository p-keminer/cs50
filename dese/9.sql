SELECT "name"
FROM "districts"
WHERE "id" IN (
    SELECT "district_id"
    FROM "expenditures"
    ORDER BY "pupils"
    LIMIT 1
);

