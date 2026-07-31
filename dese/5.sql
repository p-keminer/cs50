SELECT "city", COUNT("type")
FROM "schools"
WHERE "type" LIKE "%PUBLIC SCHOOL%"
GROUP BY "city"
HAVING COUNT("type") <= 3
ORDER BY COUNT("type") DESC, "city" ;
