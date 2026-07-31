PRAGMA foreign_keys = ON;

.mode csv
.import --skip 1 csvs/networks.csv networks

INSERT INTO "scans" (
    "id",
    "host_id",
    "network_id",
    "type",
    "scan_type",
    "tool",
    "started_at",
    "finished_at",
    "note"
)
VALUES
(1,NULL,1,'network_scan','ping','local scanner','2026-06-09 10:05:00','2026-06-09 10:05:04','Home network discovery'),
(4,NULL,2,'network_scan','ping','local scanner','2026-06-09 10:25:00','2026-06-09 10:25:03','VM network discovery');

.import --skip 1 csvs/host_findings.csv host_findings
.import --skip 1 csvs/port_scans.csv scans
.import --skip 1 csvs/ports.csv ports
.import --skip 1 csvs/services.csv services
.import --skip 1 csvs/headers.csv headers
