-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

---------------------------------------
-- Data table for scanned network data
---------------------------------------

CREATE TABLE "networks" (
    "id" INTEGER PRIMARY KEY,
    "cidr_range" TEXT NOT NULL UNIQUE,
    "networkname" TEXT
);


-----------------------------------------------
-- Data table for hosts in the scanned networks
-----------------------------------------------

CREATE TABLE "hosts" (
    "id" INTEGER PRIMARY KEY,
    "network_id" INTEGER NOT NULL,
    "ip_address" TEXT NOT NULL,
    "host_name" TEXT,
    "name" TEXT,
    "mac_address" TEXT,
    "vendor" TEXT,
    "first_seen" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "last_seen" DATETIME ,
    UNIQUE("network_id", "ip_address"),
    FOREIGN KEY ("network_id") REFERENCES "networks"("id") ON DELETE CASCADE

);


---------------------------------------
-- Data table for the individual scans
---------------------------------------

CREATE TABLE "scans" (
    "id" INTEGER PRIMARY KEY,
    "host_id" INTEGER,
    "network_id" INTEGER NOT NULL,
    "type" TEXT CHECK("type" IN("network_scan","port_scan")),
    "scan_type" TEXT,
    "tool" TEXT NOT NULL,
    "started_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "finished_at" DATETIME ,
    "note" TEXT,
    FOREIGN KEY ("network_id") REFERENCES "networks"("id") ON DELETE CASCADE,
    FOREIGN KEY ("host_id") REFERENCES "hosts"("id") ON DELETE CASCADE
);

--------------------------------------------
-- Data table for the individual ports found
---------------------------------------------

CREATE TABLE "ports" (
    "id" INTEGER PRIMARY KEY,
    "scan_id" INTEGER NOT NULL,
    "host_id" INTEGER NOT NULL,
    "network_id" INTEGER NOT NULL,
    "port_number" INTEGER,
    "protocol" TEXT,
    FOREIGN KEY ("network_id") REFERENCES "networks"("id") ON DELETE CASCADE,
    FOREIGN KEY ("scan_id") REFERENCES "scans"("id") ON DELETE CASCADE,
    FOREIGN KEY ("host_id") REFERENCES "hosts"("id") ON DELETE CASCADE
);

-----------------------------------------------
-- Data table for the individual services found
-----------------------------------------------

CREATE TABLE "services" (
    "id" INTEGER PRIMARY KEY,
    "port_id" INTEGER NOT NULL UNIQUE,
    "port_number" INTEGER,
    "name" TEXT ,
    "version" TEXT,
    "banner" TEXT,
    FOREIGN KEY ("port_id") REFERENCES "ports"("id") ON DELETE CASCADE
);


----------------------------------------------------------------------------
-- a single header table, because formatting would destroy the header tables
----------------------------------------------------------------------------

CREATE TABLE "headers" (
    "id" INTEGER PRIMARY KEY,
    "port_id" INTEGER NOT NULL,
    "header" TEXT,
    FOREIGN KEY ("port_id") REFERENCES "ports"("id") ON DELETE CASCADE
);


-------------------------------------------------------------
-- linking tables for individual data entries in the tables
-------------------------------------------------------------

CREATE TABLE "network_scan_results" (
    "id" INTEGER PRIMARY KEY,
    "scan_id" INTEGER NOT NULL,
    "host_id" INTEGER NOT NULL,
    "network_id" INTEGER  NOT NULL,
    "date" DATE DEFAULT CURRENT_DATE,
    UNIQUE("scan_id","host_id"),
    FOREIGN KEY ("network_id") REFERENCES "networks"("id") ON DELETE CASCADE,
    FOREIGN KEY ("scan_id") REFERENCES "scans"("id") ON DELETE CASCADE,
    FOREIGN KEY ("host_id") REFERENCES "hosts"("id") ON DELETE CASCADE

);

CREATE TABLE "port_scan_results" (
    "id" INTEGER PRIMARY KEY,
    "port_id" INTEGER,
    "scan_id" INTEGER NOT NULL,
    "host_id" INTEGER NOT NULL,
    "network_id" INTEGER NOT NULL,
    "service_id" INTEGER,
    "date" DATE DEFAULT CURRENT_DATE,
    "header_id" INTEGER,
    FOREIGN KEY ("network_id") REFERENCES "networks"("id") ON DELETE CASCADE,
    FOREIGN KEY ("host_id") REFERENCES "hosts"("id") ON DELETE CASCADE,
    FOREIGN KEY ("scan_id") REFERENCES "scans"("id") ON DELETE CASCADE,
    FOREIGN KEY ("port_id") REFERENCES "ports"("id") ON DELETE CASCADE,
    FOREIGN KEY ("service_id") REFERENCES "services"("id") ON DELETE SET NULL,
    FOREIGN KEY ("header_id") REFERENCES "headers"("id") ON DELETE SET NULL
);

CREATE TABLE "host_findings" (
    "id" INTEGER PRIMARY KEY,
    "scan_id" INTEGER NOT NULL,
    "network_id" INTEGER NOT NULL,
    "ip_address" TEXT NOT NULL,
    "host_name" TEXT,
    "name" TEXT,
    "mac_address" TEXT,
    "vendor" TEXT,
    "found_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY ("scan_id") REFERENCES "scans"("id") ON DELETE CASCADE,
     FOREIGN KEY ("network_id") REFERENCES "networks"("id") ON DELETE CASCADE
);
-------------------------------------------------------------------------------------
-- Creating port scan report view for csv export per python and simple sql querries
--------------------------------------------------------------------------------------

CREATE VIEW "port_scan_report" AS
SELECT "networks"."id" AS "network_id", "networks"."networkname", "networks"."cidr_range",
       "scans"."id" AS "scan_id", "scans"."scan_type", "scans"."tool" , "scans"."started_at", "scans"."finished_at", "scans"."note",
       "hosts"."id" AS "host_id", "hosts"."ip_address", "hosts"."host_name", "hosts"."name" AS "device_name", "hosts"."mac_address", "hosts"."vendor",
       "ports"."id" AS "port_id",  "ports"."port_number",  "ports"."protocol",
       "services"."id" AS "service_id", "services"."name" AS "service_name", "services"."version", "services"."banner",
       "port_scan_results"."date",
       "headers"."id" AS "header_id", "headers"."header"
FROM "port_scan_results"
JOIN "networks" ON "port_scan_results"."network_id" = "networks"."id"
JOIN "scans" ON "port_scan_results"."scan_id" = "scans"."id"
JOIN "hosts" ON "port_scan_results"."host_id" = "hosts"."id"
LEFT JOIN "ports" ON "port_scan_results"."port_id" = "ports"."id"
LEFT JOIN "services" ON "port_scan_results"."service_id" = "services"."id"
LEFT JOIN "headers" ON "port_scan_results"."header_id" = "headers"."id";

---------------------------------------------------------------------------------------
-- Creating network scan report view for csv export per python and simple sql querries
---------------------------------------------------------------------------------------

CREATE VIEW "network_scan_report" AS
SELECT "networks"."id" AS "network_id", "networks"."networkname", "networks"."cidr_range",
       "scans"."id" AS "scan_id", "scans"."scan_type", "scans"."tool" , "scans"."started_at", "scans"."finished_at", "scans"."note",
       "hosts"."id" AS "host_id", "hosts"."ip_address", "hosts"."host_name", "hosts"."name" AS "device_name", "hosts"."mac_address", "hosts"."vendor",
       "network_scan_results"."date"
FROM "network_scan_results"
JOIN "networks" ON "network_scan_results"."network_id" = "networks"."id"
JOIN "scans" ON "network_scan_results"."scan_id" = "scans"."id"
JOIN "hosts" ON "network_scan_results"."host_id" = "hosts"."id";



------------------------------------
-- Trigger for automated databases
------------------------------------

----------------------------------------------------------------
-- Updates the “last_seen” status of a host after a network scan
----------------------------------------------------------------

CREATE TRIGGER "update_last_seen_after_net"
AFTER INSERT ON "network_scan_results"
FOR EACH ROW
BEGIN
    UPDATE "hosts"
    SET "last_seen" = CURRENT_TIMESTAMP
    WHERE "id" = NEW."host_id";
END;


----------------------------------------------------------------
-- Updates the “last_seen” status of a host after a port scan
----------------------------------------------------------------

CREATE TRIGGER "update_last_seen_after_port"
AFTER INSERT ON "port_scan_results"
FOR EACH ROW
BEGIN
    UPDATE "hosts"
    SET "last_seen" = CURRENT_TIMESTAMP
    WHERE "id" = NEW."host_id";
END;


-----------------------------------------
-- generates the port scan result record
-----------------------------------------

CREATE TRIGGER "generate_port_scan_result"
AFTER INSERT ON "ports"
FOR EACH ROW
BEGIN
    INSERT INTO "port_scan_results"(
        "port_id",
        "scan_id",
        "host_id",
        "network_id"
    )VALUES(
        NEW."id",
        NEW."scan_id",
        NEW."host_id",
        NEW."network_id"
    );
END;

------------------------------------------------------------
-- links the service detection with the port scan results
------------------------------------------------------------

CREATE TRIGGER "generate_services_results"
AFTER INSERT ON "services"
FOR EACH ROW
BEGIN
    UPDATE "port_scan_results"
    SET "service_id" = NEW."id"
    WHERE "port_id" = NEW."port_id"
    AND "service_id" IS NULL;
END;


------------------------------------------------------------
-- links the header detection with the port scan results
------------------------------------------------------------

CREATE TRIGGER "generate_header_results"
AFTER INSERT ON "headers"
FOR EACH ROW
BEGIN
    UPDATE "port_scan_results"
    SET "header_id" = NEW."id"
    WHERE "port_id" = NEW."port_id"
    AND "header_id" IS NULL;
END;


------------------------------------------------------------
-- adds a host for each host found and generates a scan result
------------------------------------------------------------

CREATE TRIGGER "process_host_finding"
AFTER INSERT ON "host_findings"
FOR EACH ROW
BEGIN
    INSERT INTO "hosts" (
        "network_id" ,
        "ip_address" ,
        "host_name" ,
        "name" ,
        "mac_address" ,
        "vendor"
    )VALUES(
        NEW."network_id" ,
        NEW."ip_address" ,
        NEW."host_name" ,
        NEW."name" ,
        NEW."mac_address" ,
        NEW."vendor"
    );
    INSERT INTO "network_scan_results" (
        "scan_id",
        "host_id",
        "network_id"
    )SELECT
        NEW."scan_id",
        "hosts"."id",
        NEW."network_id"
    FROM "hosts"
    WHERE "hosts"."network_id" = NEW."network_id"
    AND "hosts"."ip_address" = NEW."ip_address";
END;

----------------------------------------------..
-- Lookup Indexes for scans, hosts and networks
------------------------------------------------


CREATE INDEX "network_cidr_range"
ON "networks" ("cidr_range");

CREATE INDEX "network_name"
ON "networks" ("networkname");



CREATE INDEX "host_network_id"
ON "hosts" ("network_id");

CREATE INDEX "host_ip"
ON "hosts" ("ip_address");



CREATE INDEX "scan_network_id"
ON "scans" ("network_id");

CREATE INDEX "scan_host_id"
ON "scans" ("host_id");

CREATE INDEX "scan_type"
ON "scans" ("type");



CREATE INDEX "port_scan_id"
ON "ports" ("scan_id");

CREATE INDEX "port_host_id"
ON "ports" ("host_id");

CREATE INDEX "port_network_id"
ON "ports" ("network_id");


CREATE INDEX "header_port_id"
ON "headers"("port_id");


-------------------------
-- Indexes for Trigger
-------------------------

CREATE INDEX "port_scan_port_service"
ON "port_scan_results"("port_id","service_id");


CREATE INDEX "port_scan_port_header"
ON "port_scan_results"("port_id","header_id");


-------------------------
-- Indexes for Views
-------------------------

CREATE INDEX "port_scan_scan_id"
ON "port_scan_results"("scan_id");

CREATE INDEX "port_scan_host_id"
ON "port_scan_results"("host_id");

CREATE INDEX "port_scan_network_id"
ON "port_scan_results"("network_id");

CREATE INDEX "port_scan_port_id"
ON "port_scan_results"("port_id");


CREATE INDEX "net_scan_scan_id"
ON "network_scan_results"("scan_id");

CREATE INDEX "net_scan_host_id"
ON "network_scan_results"("host_id");

CREATE INDEX "net_scan_net_id"
ON "network_scan_results"("network_id");
