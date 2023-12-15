# Overview

 Oracle Database connector enables FortiSOAR to run SQL query on Oracle Database 12c+

# Oracle Database


Use this connector to connect to an Oracle database to run queries and retrieve data. You can connect to multiple databases by setting up multiple configurations. 

### Version information

- Connector Version: 1.0.0
- Authored By: Fortinet CSE.
- Certified: No

### Release Notes for version 1.0.0

- Tested on 
    - FortiSOAR 7.3.0
    - Oracle Database XE 21c

### Installation

- Download and **install Oracle Instant Client:**
    - On RHEL, CentOS or Rocky linux install the required package using the command line below

```bash
yum install https://download.oracle.com/otn_software/linux/instantclient/218000/oracle-instantclient-basic-21.8.0.0.0-1.el8.x86_64.rpm
```

- Browse to **Content Hub** within FortiSOAR UI (7.2+) or the **Connector Store** if you have an older version and search for **Oracle Database* connector. Open it and click **Install**


### Configuration parameters

In FortiSOAR™, on the **Content Hub** (or Connector Store) page, click the **Manage** tab, and then click the **Oracle Database** connector card. On the connector page pops up. Select the  **Configurations** tab to enter the required configuration details.


|Parameter | Description | 
|----------|-------------|
| Host | Specify the Hostname of the oracle database server to which you will connect and perform the automated operations.|
|Port| Specify the Port number used for connecting to the database server, it is 1521 by default|
|Database|Specify the name of the database to which you will connect and perform automated operations.|
|Username|Specify the username to access the oracle database to which you will connect and perform automated operations. The user must have the required privileges on the above database|
|Password| Specify the password to access the database to which you will connect and perform automated operations.|

### Actions supported by the connector

The following automated operations can be included in playbooks:

| Function | Description |
|----------|-------------|
| Query DB| Performs a query on the configured database based on the query string you have specified. the semicolon is not needed at the end of the sql statement|

### operation: Query DB

#### Input parameters

|Parameter|Description|
|----------|-------------|
| Query String | Specify the PL*SQL query that you want to run on the configured database |
