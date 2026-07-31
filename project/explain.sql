-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

PRAGMA foreign_keys = ON;

------------------------------------------#
------------------------------------------#
--         user interactions              #
------------------------------------------#
------------------------------------------#

--------------------
-- insert a network
--------------------
EXPLAIN QUERY PLAN
INSERT INTO "networks" ("cidr_range", "networkname")
VALUES ('192.168.1.0/24', 'Home Lab');

-------------------------
-- insert a network scan
-------------------------
EXPLAIN QUERY PLAN
INSERT INTO "scans" ("host_id","network_id", "type", "scan_type", "tool")
VALUES (NULL,1,'network_scan','ping','local scanner');

----------------------
-- insert a host
----------------------
EXPLAIN QUERY PLAN
INSERT INTO "host_findings" ("scan_id","network_id","ip_address", "host_name","name")
VALUES (1,1,'192.168.1.1','router.local','Router');

----------------------
-- insert a port scan
----------------------
EXPLAIN QUERY PLAN
INSERT INTO "scans" ("host_id","network_id", "type", "scan_type", "tool")
VALUES (1,1,'port_scan','tcp_connect','local scanner');

----------------------
-- insert a open port
----------------------
EXPLAIN QUERY PLAN
INSERT INTO "ports" ("scan_id","host_id","network_id", "port_number", "protocol")
VALUES (1,1,1,22,'TCP');

----------------------
-- insert a service
----------------------
EXPLAIN QUERY PLAN
INSERT INTO "services" ("port_id","port_number","name","version", "banner")
VALUES (1,22,'SSH', 'OpenSSH', 'OpenSSH banner');

----------------------
-- insert a header
----------------------
EXPLAIN QUERY PLAN
INSERT INTO "headers" ("port_id","header")
VALUES (1,'Server: nginx');




--------------------------
-- mark a scan as finished
---------------------------
EXPLAIN QUERY PLAN
UPDATE "scans"
SET "finished_at" = CURRENT_TIMESTAMP
WHERE "id" = 3;


------------------------
-- rename a known device
-------------------------
EXPLAIN QUERY PLAN
UPDATE "hosts"
SET "name" = "Rasberry PI"
WHERE "ip_address" = "192.168.1.1";


------------------------------------------#
------------------------------------------#
--           port scan queries            #
------------------------------------------#
------------------------------------------#

-----------------------------
-- Complete port scan results
------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report";


--------------------------------------------------------------------------------------------------
-- Complete port scan results from the third scan, because the first scan will be a network scan
-- and a second one may be performed for verification purposes, and
--------------------------------------------------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "scan_id" = 3;


---------------------------------------------------------------
-- Complete port scan results from the first network scanned
---------------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "network_id" = 1;


-----------------------------------------------------------------------------
-- Complete port scan results from the first host found in the first network
-----------------------------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "host_id" = 1;


-----------------------------------------------------------------------------
-- Complete port scan results from the first host found in the first network
-----------------------------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "ip_address" = "192.168.1.1";


-------------------------------------------------------------------------------------------------
-- Complete port scan results from the scan performed on a device using an example IP address
--------------------------------------------------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "scan_id" = 1
AND "banner" IS NOT NULL;



------------------------------------------#
------------------------------------------#
--         network scan queries           #
------------------------------------------#
------------------------------------------#

--------------------------------
-- Complete network scan results
---------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "network_scan_report";


----------------------------------------------------------
-- Complete network scan results from the first network
-----------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "network_scan_report"
WHERE "scan_id" = 1;

----------------------------------------------------------
-- Complete network scan results from the second network
-----------------------------------------------------------
EXPLAIN QUERY PLAN
SELECT *
FROM "network_scan_report"
WHERE "network_id" = 2;




--------------------------------------
-- Delete network and all dependencies
--------------------------------------
EXPLAIN QUERY PLAN
DELETE FROM "networks"
WHERE "id" = 1;
