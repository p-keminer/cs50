
-- *** The Lost Letter ***

    -- id of Anneke's apartment | Check syntax and whether a result is produced
SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%";

    -- check whether congratulatory letter was sent from Annekes appartment id
SELECT "id", "contents" FROM "packages" WHERE "from_address_id" =(
    SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
);

    -- check syntax and whether a result is produced
SELECT "id" FROM "packages" WHERE "from_address_id" AND "contents" LIKE "%congrat%" =(
    SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
);

    -- check syntax again and whether result is produced | check id is the same like congrat letter
SELECT "id" FROM "packages" WHERE "from_address_id" =(
    SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
) AND "contents" LIKE "%congrat%";


    -- check syntax and whether a id is produced | hoping for address id for 2 finnegan street
SELECT "address_id" FROM "scans" WHERE "package_id" =(
    SELECT "id" FROM "packages" WHERE "from_address_id" =(
        SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
    ) AND "contents" LIKE "%congrat%"
);

    --check syntax and whether i got the adress of the letter
SELECT "address" FROM "addresses" WHERE "id" =(
    SELECT "address_id" FROM "scans" WHERE "package_id" =(
        SELECT "id" FROM "packages" WHERE "from_address_id" =(
            SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
        ) AND "contents" LIKE "%congrat%"
    )
);
    --check whether the other id is right
SELECT "address" FROM "addresses" WHERE "id" = "854";

    -- check whether the package was dropped
SELECT "address" FROM "addresses" WHERE "id" =(
    SELECT "address_id" FROM "scans" WHERE "package_id" =(
        SELECT "id" FROM "packages" WHERE "from_address_id" =(
            SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
        ) AND "contents" LIKE "%congrat%"
    ) AND "action" LIKE "%drop%"
);
    -- check type of adress where the package was dropped
SELECT "address", "type" FROM "addresses" WHERE "id" =(
    SELECT "address_id" FROM "scans" WHERE "package_id" =(
        SELECT "id" FROM "packages" WHERE "from_address_id" =(
            SELECT "id" FROM "addresses" WHERE "address" LIKE "%900 Somerville Avenue%"
        ) AND "contents" LIKE "%congrat%"
    ) AND "action" LIKE "%drop%"
);

-- *** The Devious Delivery ***

    -- check which packages contain ducks
SELECT "id" FROM "packages" WHERE "contents" LIKE "%duck%";

    -- check which duck packages were dropped
SELECT * FROM "scans" WHERE "action" LIKE "%drop%" AND "package_id" IN (
    SELECT "id" FROM "packages" WHERE "contents" LIKE "%duck%"
);
    -- check which packages were dropped anywhere
SELECT * FROM "addresses" WHERE "id" IN (
    SELECT "address_id" FROM "scans" WHERE "action" LIKE "%drop%" AND "package_id" IN (
        SELECT "id" FROM "packages" WHERE "contents" LIKE "%duck%"
    ) ORDER BY "address_id"
);

    -- check whether anywhere a packet dropped with a duck without return address
SELECT "id" FROM "packages" WHERE "contents" LIKE "%duck%" AND "from_address_id" IS NULL

    -- check type and address of paket
SELECT * FROM "addresses" WHERE "id" IN (
    SELECT "address_id" FROM "scans" WHERE "action" LIKE "%drop%" AND "package_id" IN (
        SELECT "id" FROM "packages" WHERE "contents" LIKE "%duck%" AND "from_address_id" IS NULL
    ) ORDER BY "address_id"
);

    -- check content
SELECT "id", "contents" FROM "packages" WHERE "contents" LIKE "%duck%" AND "from_address_id" IS NULL;

-- *** The Forgotten Gift ***

-- check which id is associated with grandmas adress
SELECT "id" FROM "addresses" WHERE "address" LIKE "%109 TILESTON STR%";

-- check which id, content and to adress the package has
SELECT * FROM "packages" WHERE "from_address_id" = (
     SELECT "id" FROM "addresses" WHERE "address" LIKE "%109 TILESTON STR%"
);


-- check whether the package was sent to correct address
SELECT * FROM "addresses" WHERE "id" = (
    SELECT "to_address_id" FROM "packages" WHERE "from_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" LIKE "%109 TILESTON STR%"
    )
);

-- check whether the package was dropped anywhere
SELECT * FROM "scans" WHERE "package_id" =(
    SELECT "id" FROM "packages" WHERE "from_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" LIKE "%109 TILESTON STR%"
    )
);

-- check who the driver with id 17 is, which has picked up the package the latest
SELECT * FROM "drivers" WHERE "id" is 17;

