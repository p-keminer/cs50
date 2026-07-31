
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
