## [RDS Multi-AZ Deployments Overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

### Types of Multi-AZ Deployments
- Multi-AZ DB instance deployment (one standby DB instance)
  - Has one standby DB instance providing failover support
  - Standby doesn't serve read traffic
  - Uses synchronous replication across availability zones
- Multi-AZ DB cluster deployment (two standby DB instances)
  - Has two standby DB instances providing failover support
  - Standby instances can serve read traffic
  - Provides higher availability and read scaling

### Identifying Deployment Types in Console
- Multi-AZ DB instance deployment characteristics:
  - Single row for the DB instance
  - Role value shows "Instance" or "Primary"
  - Multi-AZ value shows "Yes"
- Multi-AZ DB cluster deployment characteristics:
  - Cluster-level row with three DB instance rows beneath
  - Cluster-level row has "Multi-AZ DB cluster" role
  - Instance rows show "Writer instance" or "Reader instance" roles
  - Instance rows show "3 Zones" for Multi-AZ value

### Multi-AZ DB Instance Deployments
- Technologies used:
  - Amazon failover technology (for MariaDB, MySQL, Oracle, PostgreSQL, RDS Custom for SQL Server)
  - SQL Server Database Mirroring or Always On Availability Groups (for Microsoft SQL Server)
- Benefits:
  - Data redundancy
  - Minimized latency during backups
  - Enhanced availability during maintenance
  - Protection against DB instance failure
  - Protection against Availability Zone disruption

### Converting to Multi-AZ
- Process:
  1. Amazon RDS takes a snapshot of primary DB's EBS volumes
  2. Creates new volumes for standby replica from snapshot
  3. Initiates synchronous block-level replication between primary and standby
- Performance considerations:
  - Process can impact performance during conversion
  - Synchronous replication may increase I/O latency
  - Best practice: Avoid converting production DB instances directly
- Conversion methods:
  - Through RDS console (Apply immediately or during maintenance window)
  - Using AWS CLI with modify-db-instance command
  - Using RDS API with ModifyDBInstance operation

### Failover Process
- Automatic process that takes 60-120 seconds typically
- Can take longer with large transactions or lengthy recovery
- Failover triggers:
  - OS patching during maintenance window
  - Unhealthy primary host
  - Network connectivity loss
  - Customer-initiated DB instance modification
  - Unresponsive primary instance
  - Storage volume failure
  - Manual failover request
- Monitoring failover:
  - Set up DB event subscriptions for notifications
  - View DB events in RDS console or API
  - Check current state in RDS console or API

### DNS Management for Failover
- Failover mechanism changes DNS record to point to standby
- JVM environments require special considerations
- Best practice: Configure JVM with TTL value of 60 seconds or less
- Methods to modify JVM's TTL:
  - Global setting in java.security file
  - Local setting in application initialization code

### Terms
- Multi-AZ - A deployment strategy where database instances are maintained in multiple availability zones for high availability and failover support.
- Standby replica - A backup database instance that maintains a synchronized copy of the primary database for failover purposes.
- Synchronous replication - A process where data is simultaneously written to both primary and standby instances before transactions are considered complete.
- Availability Zone - A distinct location within an AWS Region designed to be isolated from failures in other Availability Zones.
- Failover - The process of automatically switching from the primary database to a standby replica when the primary becomes unavailable.
- EBS volumes - Amazon Elastic Block Store volumes that provide persistent block-level storage for Amazon RDS instances.
- DNS record - Domain Name System record that maps a domain name to the IP address of the active database instance.
- TTL (Time-to-Live) - A value that determines how long DNS information is cached before being refreshed.
- JVM (Java Virtual Machine) - The runtime environment for Java applications that may need configuration for proper failover handling.
- RDS console - The web interface used to manage Amazon RDS resources.

///

## Which of the following describes a Multi-AZ DB instance deployment?

---

A) It has one standby DB instance that provides failover support, but doesn't serve read traffic

B) It has two standby DB instances that provide failover support and can serve read traffic

C) It's a single DB instance replicated across multiple regions

D) It has three DB instances that all serve both read and write traffic

---

It has one standby DB instance that provides failover support, but doesn't serve read traffic

///

## What technology does Amazon RDS use for Multi-AZ deployments with MariaDB, MySQL, Oracle, PostgreSQL, and RDS Custom for SQL Server?

---

D) SQL Server Database Mirroring

A) Always On Availability Groups

B) Amazon failover technology

C) Oracle Data Guard

---

Amazon failover technology

///

## In the RDS console, how can you identify a Multi-AZ DB instance deployment?

---

D) The value of Role is "Multi-AZ DB cluster"

A) The value of Multi-AZ is "3 Zones"

B) There is only one row for the DB instance and the value of Multi-AZ is "Yes"

C) The value of Role is "Reader instance"

---

There is only one row for the DB instance and the value of Multi-AZ is "Yes"

///

## What is the typical failover time for a Multi-AZ DB instance?

---

C) 15-30 seconds

D) 60-120 seconds

A) 5-10 minutes

B) 30-60 minutes

---

60-120 seconds

///

## What is the first step Amazon RDS performs when converting a Single-AZ deployment to a Multi-AZ DB instance deployment?

---

C) Initializes synchronous block-level replication

B) Takes a snapshot of the primary DB instance's EBS volumes

A) Creates a new primary DB instance in a different Availability Zone

D) Shuts down the current DB instance

---

Takes a snapshot of the primary DB instance's EBS volumes

///

## What is a potential impact of converting a production DB instance directly to Multi-AZ?

---

D) No performance impact as the process is done during maintenance windows

B) Increased I/O latency due to synchronous replication

C) Complete database downtime during the conversion

A) Loss of all existing connections permanently

---

Increased I/O latency due to synchronous replication

///

## What does the failover mechanism automatically change during a failover event?

---

C) The IP address of the standby database

A) The DNS record of the DB instance

D) The security groups attached to the DB instance

B) The database engine version

---

The DNS record of the DB instance

///

## What is the recommended TTL value for JVM environments working with AWS resources?

---

B) No more than 60 seconds

C) At least 300 seconds

D) Default JVM setting (usually 24 hours)

A) 0 seconds (no caching)

---

No more than 60 seconds

///

## Which of the following is NOT a trigger for an automatic failover in a Multi-AZ DB instance?

---

B) The primary host is unhealthy

D) Network connectivity loss to the primary

A) Read traffic exceeds database capacity

C) Storage volume failure on the primary host

---

Read traffic exceeds database capacity

///

## What is synchronous replication in the context of Multi-AZ deployments?

---

C) A process where backups are created at regular intervals

A) A process where data is simultaneously written to both primary and standby instances

D) A process where multiple users can read from the database at the same time

B) A process where database schema changes are deployed to all instances

---

A process where data is simultaneously written to both primary and standby instances

///

## Which of the following is TRUE about standby replicas in a Multi-AZ DB instance deployment?

---

B) They can be used for read scaling to offload queries from the primary

D) They are located in a different AWS Region from the primary

A) They cannot be accessed directly by applications

C) They use a different storage type than the primary instance

---

They cannot be accessed directly by applications

///

## What is the best practice recommended instead of directly converting a production DB instance to Multi-AZ?

---

D) Take the production database offline during non-business hours for conversion

A) Create a read replica, enable backups on it, convert it to Multi-AZ, and promote it

B) Create a completely new Multi-AZ instance and migrate data manually

C) Wait for the next maintenance window to perform the conversion

---

Create a read replica, enable backups on it, convert it to Multi-AZ, and promote it

///

## What happens to existing database connections during a Multi-AZ failover?

---

C) They continue to function without interruption

A) They are terminated and need to be re-established

D) They are paused and automatically resumed after failover

B) They are redirected to a read replica until failover completes

---

They are terminated and need to be re-established

///

## Which command is used to convert a DB instance to Multi-AZ using the AWS CLI?

---

B) create-multi-az-instance

D) convert-to-multi-az

A) modify-db-instance (with --multi-az option)

C) update-db-instance-deployment

---

modify-db-instance (with --multi-az option)

///

## What is the purpose of Multi-AZ DB cluster deployments?

---

C) To span database instances across multiple AWS Regions

D) To provide both failover support and serve read traffic from standby instances

A) To reduce costs by sharing resources across instances

B) To support different database engines in the same deployment

---

To provide both failover support and serve read traffic from standby instances
