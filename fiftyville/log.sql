-- Keep a log of any SQL queries you execute as you solve the mystery.

-- getting starting information

SELECT * FROM "crime_scene_reports"
WHERE "year" = 2025
AND "month" = 07
AND "day" = 28
AND "street" LIKE "%HUMPHREY STREET%";

-- getting interview information

SELECT * FROM "interviews"
WHERE "year" = 2025
AND "month" = 07
AND "day" = 28;

-- getting bakery information

SELECT * FROM "bakery_security_logs"
WHERE "year" = 2025
AND "month" = 07
AND "day" = 28
AND "hour" = 10
AND "minute" < 25;

-- getting transaction information

SELECT * FROM "atm_transactions"
WHERE "year" = 2025
AND "month" = 07
AND "day" = 28
AND "atm_location" LIKE "%LEGGETT STREET%";

-- getting phone information

SELECT * FROM "phone_calls"
WHERE "year" = 2025
AND "month" = 07
AND "day" = 28
AND "duration" < 60;

-- getting full joined information

SELECT "people"."name", "people"."phone_number", "people"."passport_number", "people"."license_plate",
       "bakery_security_logs"."minute", "bakery_security_logs"."activity",
       "phone_calls"."duration","phone_calls"."caller","phone_calls"."receiver",
       "bank_accounts"."person_id",
       "atm_transactions"."account_number", "atm_transactions"."atm_location", "atm_transactions"."transaction_type",  "atm_transactions"."amount"
FROM "people"
JOIN "bakery_security_logs" ON "people"."license_plate" = "bakery_security_logs"."license_plate"
JOIN "phone_calls" ON "people"."phone_number" = "phone_calls"."caller"
JOIN "bank_accounts" ON "people"."id" = "bank_accounts"."person_id"
JOIN "atm_transactions" ON "bank_accounts"."account_number" = "atm_transactions"."account_number"
WHERE "bakery_security_logs"."year" = 2025
AND "bakery_security_logs"."month" = 07
AND "bakery_security_logs"."day" = 28
AND "bakery_security_logs"."hour" = 10
AND "bakery_security_logs"."minute" < 25
AND "phone_calls"."duration" < 60
AND "atm_transactions"."atm_location" = "Leggett Street"
AND "atm_transactions"."transaction_type" = "withdraw"
AND "phone_calls"."year" = 2025
AND "phone_calls"."month" = 7
AND "phone_calls"."day" = 28
AND "atm_transactions"."year" = 2025
AND "atm_transactions"."month" = 7
AND "atm_transactions"."day" = 28

-- Check whether and when Bruce flew

SELECT * FROM "flights" WHERE "id" IN (
    SELECT "flight_id" FROM "passengers" WHERE "passport_number" = 5773159633
);

-- Check if the flight was the first one the next day

SELECT * FROM "flights" WHERE "day" = 29 AND "month" = 7 AND "year" = 2025 ORDER BY "hour" , "min";

-- Check where Bruce flew to

SELECT * FROM "airports" WHERE "id" = 4;

-- Find out who Bruce was calling

SELECT * FROM "people" WHERE "phone_number" = "(375) 555-8161";







