CREATE TABLE "passengers" (
        "id" INTEGER NOT NULL,
        "first_name" TEXT NOT NULL,
        "last_name" TEXT NOT NULL,
        "age" INTEGER NOT NULL,
        PRIMARY KEY("id")
);

CREATE TABLE "check_ins" (
        "day" INTEGER NOT NULL,
        "month" INTEGER NOT NULL,
        "year" INTEGER NOT NULL,
        "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "flight_id" INTEGER NOT NULL,
        "passenger_id" INTEGER,
        FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
        FOREIGN KEY("flight_id") REFERENCES "flights"("id")
);

CREATE TABLE "airlines" (
        "name" TEXT NOT NULL,
        "coucourses" TEXT NOT NULL,
        PRIMARY KEY("name")
);

CREATE TABLE "flights" (
        "id" INTEGER NOT NULL,
        "name_airline" TEXT NOT NULL,
        "flight_from" TEXT NOT NULL,
        "day_from" INTEGER NOT NULL,
        "month_from" INTEGER NOT NULL,
        "year_from" INTEGER NOT NULL,
        "datetime_from" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "flight_to" TEXT NOT NULL,
        "day_to" INTEGER NOT NULL,
        "month_to" INTEGER NOT NULL,
        "year_to" INTEGER NOT NULL,
        "hour_to" INTEGER NOT NULL,
        "datetime_to" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY("id"),
        FOREIGN KEY("name_airline") REFERENCES "airlines"("name")
);
