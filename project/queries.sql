-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

PRAGMA foreign_keys = ON;
DELETE FROM "networks"
WHERE "id" = 99;


------------------------------------------#
------------------------------------------#
--         user interactions              #
------------------------------------------#
------------------------------------------#

--------------------
-- insert a network
--------------------
--EXPLAIN QUERY PLAN
INSERT INTO "networks" ("id","cidr_range", "networkname")
VALUES (99,'193.168.1.0/24', 'Demo Lab');

-------------------------
-- insert a network scan
-------------------------
--EXPLAIN QUERY PLAN
INSERT INTO "scans" ("id","host_id","network_id", "type", "scan_type", "tool")
VALUES (99,NULL,99,'network_scan','ping','demo local scanner');

----------------------
-- insert a host
----------------------
--EXPLAIN QUERY PLAN
INSERT INTO "host_findings" ("id","scan_id","network_id","ip_address", "host_name","name")
VALUES (99,99,99,'193.168.1.1','router.local','Raspberry Pi');

----------------------
-- insert a port scan
----------------------
--EXPLAIN QUERY PLAN
INSERT INTO "scans" ("id","host_id","network_id", "type", "scan_type", "tool")
VALUES (100,(SELECT "id" FROM "hosts" WHERE "network_id" = 99 AND "ip_address" = "193.168.1.1" ),99,'port_scan','tcp_connect','local scanner');

----------------------
-- insert a open port
----------------------
--EXPLAIN QUERY PLAN
INSERT INTO "ports" ("id","scan_id","host_id","network_id", "port_number", "protocol")
VALUES (99,100,(SELECT "id" FROM "hosts" WHERE "network_id" = 99 AND "ip_address" = "193.168.1.1" ),99,8080,'TCP');

----------------------
-- insert a service
----------------------
--EXPLAIN QUERY PLAN
INSERT INTO "services" ("id","port_id","port_number","name","version", "banner")
VALUES (99,99,8080, 'HTTP-alt', 'Demo Server', 'Server:demo');

----------------------
-- insert a header
----------------------
--EXPLAIN QUERY PLAN
INSERT INTO "headers" ("id","port_id","header")
VALUES (99,99,'Server: demo');




--------------------------
-- mark a scan as finished
---------------------------
--EXPLAIN QUERY PLAN
UPDATE "scans"
SET "finished_at" = CURRENT_TIMESTAMP
WHERE "id" = 99;


------------------------
-- rename a known device
-------------------------
--EXPLAIN QUERY PLAN
UPDATE "hosts"
SET "name" = "Rasberry Pi"
WHERE "ip_address" = "193.168.1.1";


------------------------------------------#
------------------------------------------#
--           port scan queries            #
------------------------------------------#
------------------------------------------#

-----------------------------
-- Complete port scan results
------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report";


--------------------------------------------------------------------------------------------------
-- Complete port scan results from the third scan, because the first scan will be a network scan
-- and a second one may be performed for verification purposes, and
--------------------------------------------------------------------------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "scan_id" = 3;


---------------------------------------------------------------
-- Complete port scan results from the first network scanned
---------------------------------------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "network_id" = 1;


-----------------------------------------------------------------------------
-- Complete port scan results from the first host found in the first network
-----------------------------------------------------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "host_id" = 1;


-----------------------------------------------------------------------------
-- Complete port scan results from the first host found in the first network
-----------------------------------------------------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "port_scan_report"
WHERE "ip_address" = "192.168.1.1";


-------------------------------------------------------------------------------------------------
-- Complete port scan results from the scan performed on a device using an example IP address
--------------------------------------------------------------------------------------------------
--EXPLAIN QUERY PLAN
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
--EXPLAIN QUERY PLAN
SELECT *
FROM "network_scan_report";


----------------------------------------------------------
-- Complete network scan results from the first network
-----------------------------------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "network_scan_report"
WHERE "scan_id" = 1;

----------------------------------------------------------
-- Complete network scan results from the second network
-----------------------------------------------------------
--EXPLAIN QUERY PLAN
SELECT *
FROM "network_scan_report"
WHERE "network_id" = 2;




------------------------------------------
-- Delete networks and all dependencies
------------------------------------------
--EXPLAIN QUERY PLAN
DELETE FROM "networks"
WHERE "id" = 99;
