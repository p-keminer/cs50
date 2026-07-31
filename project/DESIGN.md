# Design Document

Network Scanning Ecosystem - By Philip Keminer

Video overview: https://youtu.be/JgdM4IAWQg4

## Scope

This database is intended to serve as a hub for storing and processing results from local network and port scans in a structured manner. In addition, it should be capable of generating detailed reports with minimal effort and be easy to maintain. Its purpose is limited solely to local and authorized targets within the organization’s own network.

The database consists of individual tables, as shown in the diagram below, e.g., networks, found hosts, individual scans, open ports found, detected services, and banner or header information. Additionally, two “on command” report views are implemented to make exports and report generation as simple as possible using higher-level programming languages such as Python.

- Networks themselves are represented by their CIDR range ‘xxx.xxx.x.x/y’.
- Individual devices are stored as hosts within a single network.
- Scans are assigned a type identification that currently includes either network scan or port scan
- Ports store the ports found during a host scan
- Services indicate which services were detected on the respective port
- Header stores simple text information such as headers or banners
- Host findings serve as a trigger and insertion table to populate information in the database
- Port scan results and Network scan results serve as lookup tables for subsequent views and simplified queries


Specific attack vectors, CVE matches, exploit attempts, and anything falling under “red teaming” are outside the scope of this database; the database
is intentionally intended solely as a reconnaissance tool.


## Functional Requirements

The database should be capable of creating networks, performing network and port scans, storing host findings and port information along with service and header details, querying this data, and presenting it clearly in comprehensive reports.
This data should answer typical questions about a network: Which hosts and what information are publicly accessible? Which scans fail, when, and why? Which hosts are consistently detectable on a network?

All of this should be generated as simply as possible and automatically by the database; therefore, there are input tables, such as `host_findings` for discovered hosts.
A higher-level programming language or application need only write to this table, and the database propagates this data via a trigger to `hosts` and
`network_scan_results`.

Another input table, `ports`, generates an automatic entry in `port_scan_results` in a somewhat simpler manner; if associated headers or services are subsequently entered, they also automatically expand the port scan result record.

For the demo video, mri created a small seed dataset using CSV files and automatically loaded it into the database via a file named `import.sql`. The ‘querries.sql’ file remains unaffected in this process, as it merely displays this information, creates an additional record, and deletes it again at the end.

The database is not intended to be used to carry out automated attacks or scans; it is intended solely for documentation purposes.


## Representation

### Entities

The database contains the entities that are representative of a typical scan workflow: `networks`, `hosts`, `scans`, `host_findings`, `ports`, `services`, `headers`, `network_scan_results`. This allows you to first define a network, scan it, and then, based on that, scan the hosts within the network, after which a detailed report of both scans is generated

The `networks` table represents scanned networks and, like any other table, contains a unique `id` as the primary key, as well as the unique `cidr_range` and, optionally, `networkname`. The CIDR range is stored as `TEXT` since it does not need to be processed as a number; however, it has a unique constraint to ensure that the same network range remains unique.

The `hosts` table represents known devices within a previously defined network (`network_id`). The combination of `network_id` and `ip_address` is defined as unique to prevent a host from being created multiple times. Attributes such as `host_name`, `name`, `mac_address`, and `vendor` are treated as text, as they do not need to be processed as numbers or similar data types. `first_seen` and `last_seen` are typical date/time values and are therefore defined as DATETIME.

The `scans` table stores individual scan operations and is always associated with a network. `host_id` can be empty, since network scans do not have a host ID.
For port scans, `host_id` refers to the host that was scanned. The `type` field is also a text field that is restricted to `network_scan` or `port_scan` via a `CHECK`, as this was a deliberate design decision but can be expanded later as an option when the database is extended. `scan_type` describes the specific method, e.g., `ping` or `tcp_connect`.

The `host_findings` table is the input table for discovered hosts. It stores in which scan and network an IP address was found. The `process_host_finding` trigger handles the actual assignment to `hosts` and `network_scan_results`. This approach was chosen to simplify automation and data entry via higher-level programming languages or applications.

The `ports` table stores open ports that have been found; each port belongs to a port scan, a host, and a network, so it also contains their corresponding IDs. `port_number` is an integer, as it is a numerical value and allows for simple comparisons. `protocol` was defined as text, as it is intended to store values such as `TCP`.

The `services` table stores detected services associated with a port. It contains related information such as `name`, `version`, and `banner` as text fields for the most part, since these can have different structures and are optional. A conscious decision was made to ensure that `port_id` is uniquely defined, as only one primary detected service should be stored per port.

The `headers` table stores header or banner information as a simple text block and extends the `ports` table. This table is intentionally kept simple and separate because a readable report output is more important than breaking down individual header fields, but it can be expanded later. However, it also contains a unique identifier `id` and `port_id`.

The `network_scan_results` and `port_scan_results` tables are result and relationship tables. `network_scan_results` links network scan, host, and network; `port_scan_results` links port scan, host, network, port, service, and header, and is defined exactly as these data types are in the other tables.

---

### Relationships

<img src="diagram.png" alt="Entity Relationship Diagram" width="800">

- A network can contain many hosts and many scans
- A host can appear in multiple scans
- A network scan can generate multiple host detections
- A host detection results in a host and a network scan result
- A port scan belongs to a host
- A port belongs to a port scan, a host, and a network
- A service and a header each belong to a port

Simplified, the data flow looks like this:

```text
networks
  -> scans(type = network_scan)
  -> host_findings
  -> hosts
  -> network_scan_results

hosts
  -> scans(type = port_scan)
  -> ports
  -> services/headers
  -> port_scan_results
```

Here, the views `network_scan_report` and `port_scan_report` combine these tables back into readable result lists.

## Optimizations

As mentioned several times, views were used to optimize the retrieval of reports, making the process more structured and streamlined and eliminating the need to write endless `JOIN` queries.

### Indexes

Indexes were created on all typical query columns (`network_id`, `host_id`, `scan_id`, `port_id`, and `ip_address`). Even though this incurs storage costs and requires maintenance with every extension, this approach was deliberately chosen to cover all typical queries and, in particular, to speed up cascading operations.

The indexes on `port_scan_results` and `network_scan_results` are particularly important for this, because the report views are based on these tables. Furthermore, indexes on `host_findings` are useful because this table is linked to other tables via `network_id`, `scan_id`, and IP address.

### Triggers

In this design, triggers automate highly repetitive tasks and reduce both insertions and queries on the database. `process_host_finding` generates the host and the network scan result from a host finding. `generate_port_scan_result` generates a port scan result from an inserted port, and other triggers link services and headers to this result. The `last_seen` triggers update hosts when new result data becomes available.

Foreign keys with `ON DELETE CASCADE` ensure that dependent result data is removed as soon as a network, host, scan, or port is deleted. For `service_id` and `header_id` in `port_scan_results`, `ON DELETE SET NULL` is used because a port scan result can remain even if the additional service or header information has been removed or updated.

## Limitations

The database is intentionally kept small and is suitable for local test data, simple reports, and clear documentation, but not for large enterprise environments and complex systems. It lacks user roles, detailed audit logs, rights management, etc. Additionally, the database does not recognize services, banners, headers, or similar items on its own; it only stores what a scanner or another program returns as a result.

Furthermore, incorrect results cannot be detected in real time, or only to a limited extent.
Headers are stored solely as plain text; by separating header names and header values, this limitation could be overcome.

The automations require that data be entered in the logically correct order. First, a network must exist, then a network scan, followed by host detections, then port scans, ports, services, and headers.
