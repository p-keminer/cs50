CREATE VIEW "june_vacancies" AS
SELECT "listings"."id", "listings"."property_type", "listings"."host_name", COUNT("reviews"."id") AS "reviews"
FROM "listings"
JOIN "reviews"
ON "listings"."id" == "reviews"."listing_id"
GROUP BY "listings"."id","listings"."property_type", "listings"."host_name"
ORDER BY "reviews" DESC,"listings"."property_type", "listings"."host_name"
LIMIT 100;
