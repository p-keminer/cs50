SELECT"teams"."name", SUM("performances"."H") AS "total hits"
FROM "teams"
JOIN "performances"
ON "teams"."id" = "performances"."team_id"
WHERE "performances"."year" LIKE "2001"
GROUP BY "performances"."team_id"
ORDER BY "total hits" DESC
LIMIT 5;
