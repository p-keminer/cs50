CREATE TABLE "users" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "first_name" TEXT NOT NULL,
        "last_name" TEXT NOT NULL,
        "username" TEXT NOT NULL,
        "password" TEXT NOT NULL

);

CREATE TABLE "schools" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "name" TEXT NOT NULL,
        "kind" TEXT NOT NULL CHECK("kind" in ('elementary','middle','high','lower','upper','college','university')),
        "city" TEXT,
        "year" TEXT
);

CREATE TABLE "companys" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "name" TEXT NOT NULL,
        "branche" TEXT CHECK("branche" in('education','technology','finance','etc.')),
        "city" TEXT

);

CREATE TABLE "connections_users" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "user_id1" INTEGER NOT NULL,
        "user_id2"INTEGER NOT NULL,
        "type" TEXT NOT NULL CHECK("type" in('follow','connection')),
        FOREIGN KEY("user_id1") REFERENCES "users"("id"),
        FOREIGN KEY("user_id2") REFERENCES "users"("id")
);

CREATE TABLE "connections_schools" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "user_id" INTEGER NOT NULL,
        "school_id" INTEGER NOT NULL,
        "studied_from" NUMERIC ,
        "graduation" TEXT,
        "studied_to" NUMERIC DEFAULT CURRENT_TIMESTAMP,
        "worked_from" NUMERIC,
        "worked_to" NUMERIC DEFAULT CURRENT_TIMESTAMP,
        "type" TEXT NOT NULL CHECK("type" in('follow','working','studied')),
        FOREIGN KEY("user_id") REFERENCES "users"("id"),
        FOREIGN KEY("school_id") REFERENCES "schools"("id")
);

CREATE TABLE "connections_companys" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "user_id" INTEGER NOT NULL,
        "company_id" INTEGER NOT NULL,
        "position" TEXT,
        "experience" TEXT,
        "worked_from" NUMERIC ,
        "worked_to" NUMERIC DEFAULT CURRENT_TIMESTAMP,
        "type" TEXT NOT NULL CHECK("type" in('follow','working')),
        FOREIGN KEY("user_id") REFERENCES "users"("id"),
        FOREIGN KEY("company_id") REFERENCES "companys"("id")
);
