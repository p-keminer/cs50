CREATE TABLE "ingredients" (
        "id" INTEGER PRIMARY KEY,
        "type" TEXT UNIQUE NOT NULL CHECK("type" in ('floor','yeast','oil','sugar_brown','sugar_white','butter','kakao')),
        "price_cents" INTEGER NOT NULL,
        "overall" INTEGER,
        "unit" TEXT NOT NULL
);

CREATE TABLE "recipes" (
        "id" INTEGER PRIMARY KEY,
        "donut_id" INTEGER NOT NULL UNIQUE,
        "floor" INTEGER,
        "yeast" INTEGER,
        "oil" INTEGER,
        "sugar_brown" INTEGER,
        "sugar_white" INTEGER,
        "butter" INTEGER,
        "kakao" INTEGER,
        "buttermilk" INTEGER,
        "sprinkles" INTEGER,
        FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);

CREATE TABLE "donuts" (
        "id" INTEGER PRIMARY KEY,
        "name" TEXT NOT NULL UNIQUE,
        "free" TEXT NOT NULL CHECK("free" in ('yes','no')),
        "price" INTEGER NOT NULL

);


CREATE TABLE "orders" (
        "id" INTEGER NOT NULL,
        "donut_type" TEXT NOT NULL,
        "number" INTEGER NOT NULL,
        "customer_id" INTEGER NOT NULL,
        FOREIGN KEY("customer_id") REFERENCES "customers"("id"),
        FOREIGN KEY("donut_type") REFERENCES "donuts"("name")
);

CREATE TABLE "customers" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "first_name" TEXT NOT NULL,
        "last_name" TEXT NOT NULL,
        "order_id" INTEGER NOT NULL,
        FOREIGN KEY("order_id") REFERENCES "orders"("customer_id")

);

