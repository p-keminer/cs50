CREATE VIEW "by_district" AS
SELECT "district", SUM("families") AS "families" ,SUM("population") AS "population" ,SUM("male") AS "male" ,SUM("female") AS "female"
FROM "census"
GROUP BY "district";
