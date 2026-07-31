SELECT COUNT(*)
FROM "schools"
JOIN "districts"
ON "schools"."district_id" = "districts"."id"
