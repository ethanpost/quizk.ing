## Amazon RDS Blue/Green Deployments

### Overview
- A mechanism for making and testing database changes before implementing in production
- Blue environment is the current production environment
- Green environment is the staging environment that copies and stays in sync with production
- Changes can be made to RDS DB instances in green environment without affecting production
- Switchover transitions green environment to become the new production environment
- Typically takes under one minute with no data loss and no application changes needed

### Supported Database Engines
- RDS for MariaDB
- RDS for MySQL
- RDS for PostgreSQL
- Not currently supported for Amazon RDS Proxy, cascading read replicas, cross-Region read replicas, AWS CloudFormation, and Multi-AZ DB cluster deployments

### Benefits
- Create production-ready staging environments easily
- Automatically replicate database changes from production to staging
- Test changes safely without affecting production
- Stay current with patches and system updates
- Implement and test new database features
- Switch over without application changes
- Built-in switchover guardrails for safety
- No data loss during switchover
- Fast switchover (typically under one minute)

### Permissions and Authorization
- IAM policies required for creating, switching, and deleting deployments
- Creating deployments requires permissions for:
  - rds:CreateBlueGreenDeployment
  - rds:AddTagsToResource
  - rds:CreateDBInstanceReadReplica
- Switching over requires permissions for:
  - rds:SwitchoverBlueGreenDeployment
  - rds:ModifyDBInstance
  - rds:PromoteReadReplica
- Deleting deployments requires permissions for:
  - rds:DeleteBlueGreenDeployment
  - rds:DeleteDBInstance

### Creating Blue/Green Deployments
- Specify source DB instance to copy (production instance becomes blue environment)
- Prepare the DB instance with required configuration
- Optionally specify changes for green environment:
  - Higher engine version
  - Different DB parameter group
  - Storage and performance settings
  - Enable RDS Optimized Writes
  - Storage configuration upgrades

### Replication Methods
- RDS for PostgreSQL uses different replication methods based on circumstances:
  - Physical replication for minor version upgrades or same version
  - Logical replication for major version upgrades (on supported versions)

### Limitations
- General limitations:
  - No support for AWS Secrets Manager for master user passwords
  - Cannot change encryption status (encrypted to unencrypted or vice versa)
  - Resources must be in same AWS account
  - Specific features not supported (RDS Proxy, cascading read replicas, etc.)
- MySQL-specific limitations:
  - Blue DB instance can't be an external binlog replica
  - Custom option groups restrict major version upgrades
  - No support for AWS JDBC Driver for MySQL
- PostgreSQL-specific limitations for physical replication:
  - No manual major version upgrades after green environment creation
  - Schema changes not supported in green environment
  - Blue DB instance can't be a logical source or replica
- PostgreSQL-specific limitations for logical replication:
  - Unlogged tables not replicated
  - Resource overhead increases with number of databases
  - Single-threaded replication apply process
  - Limitations with certain extensions (pg_partman, pg_cron, pglogical, pgactive)
  - DDL statements not replicated
  - Large objects not replicated
  - Tables must have primary keys

### Best Practices
- General best practices:
  - Test green environment thoroughly before switchover
  - Keep green environment read-only
  - Make only replication-compatible schema changes
  - Handle lazy loading before switchover
  - Follow switchover best practices
- MySQL-specific best practices:
  - Avoid non-transactional storage engines
  - Optimize binary log replication
  - Address replica lag before switchover
- PostgreSQL-specific best practices:
  - Update extensions to latest versions
  - Manage long-running transactions
  - Optimize vacuum operations
  - Adjust replication timeout parameters
  - Ensure adequate storage for WAL segments

### Switchover Process
- Switchover timeout period configurable (30-3600 seconds, default 300 seconds)
- Guardrail checks before switchover:
  - Replication health and lag
  - Active writes in green environment
  - External replication, long-running writes, DDL statements in blue environment
- Switchover actions:
  - Stop new write operations
  - Drop connections and prevent new ones
  - Wait for replication to catch up
  - Rename DB instances in both environments
  - Allow connections to databases
  - Allow write operations in new production environment

### Post-Switchover Steps
- Previous blue environment resources are retained (with standard costs)
- Replication between environments stops
- DB instances in old blue environment are read-only until configured otherwise
- For external replicas, update parent node to maintain replication

### Deleting Blue/Green Deployments
- Can delete before or after switchover
- Option to delete or retain green environment DB instances
- Blue environment not affected by deletion

### Terms
- Blue environment - The current production environment in a blue/green deployment.
- Green environment - The staging environment that copies the production environment in a blue/green deployment.
- Switchover - The process of transitioning the green environment to be the new production environment.
- Switchover guardrails - Checks that prevent switchover if environments aren't ready, avoiding downtime and data loss.
- Replica lag - The measure of how far behind a replica is from its source database.
- Physical replication - A replication method that copies the entire database at the storage level.
- Logical replication - A replication method that replicates data changes at the logical level through SQL statements.
- Lazy loading - The process where data blocks are loaded as applications request them rather than all at once.
- Storage initialization - The process of proactively downloading all blocks from Amazon S3 to provide maximum volume performance.

///

## Which environment represents the current production database in a blue/green deployment?

---

A) Blue environment

B) Green environment

C) Staging environment

D) Test environment

---

Blue environment

///

## How long does a blue/green deployment switchover typically take?

---

A) Several hours

B) 30-60 minutes

C) Less than one minute

D) 5-10 minutes

---

Less than one minute

///

## Which of the following database engines are supported for Amazon RDS Blue/Green Deployments?

---

A) Aurora MySQL, Aurora PostgreSQL, and RDS for Oracle

B) RDS for SQL Server, RDS for MySQL, and RDS for MariaDB

C) RDS for Oracle, RDS for SQL Server, and RDS for DB2

D) RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL

---

RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL

///

## What is a switchover guardrail?

---

A) A monitoring tool that tracks database performance during switchover

B) A physical barrier that prevents unauthorized access to the database

C) A backup system that activates if the switchover fails

D) A check that prevents switchover if environments aren't ready to avoid downtime and data loss

---

A check that prevents switchover if environments aren't ready to avoid downtime and data loss

///

## Which permission is required to switch over a blue/green deployment?

---

A) rds:ModifyBlueGreenDeployment

B) rds:DeleteBlueGreenDeployment

C) rds:CreateBlueGreenDeployment

D) rds:SwitchoverBlueGreenDeployment

---

rds:SwitchoverBlueGreenDeployment

///

## What happens to database connections during a blue/green deployment switchover?

---

A) Only read connections remain active, write connections are dropped

B) Connections are automatically redirected to the green environment

C) Connections remain active throughout the process

D) Connections are dropped and new connections aren't allowed temporarily

---

Connections are dropped and new connections aren't allowed temporarily

///

## What is lazy loading in the context of blue/green deployments?

---

A) The automatic scaling of database resources based on demand

B) A technique to optimize database query performance

C) A method to reduce database workload during peak hours

D) A process where data blocks are loaded only as applications request them

---

A process where data blocks are loaded only as applications request them

///

## What happens to the blue environment after a switchover?

---

A) It becomes the new staging environment

B) It is immediately upgraded to match the green environment

C) It is automatically deleted

D) It is retained and renamed with "-oldn" suffix

---

It is retained and renamed with "-oldn" suffix

///

## Which of the following is NOT a benefit of using blue/green deployments?

---

A) Testing database changes safely without affecting production

B) Minimizing downtime during database updates

C) Reducing database storage costs

D) Implementing and testing newer database features

---

Reducing database storage costs

///

## When does Amazon RDS use logical replication instead of physical replication for PostgreSQL blue/green deployments?

---

A) When the source instance uses Multi-AZ deployment

B) When the source instance has read replicas

C) When the green environment has different storage settings

D) When requesting a major version upgrade on supported PostgreSQL versions

---

When requesting a major version upgrade on supported PostgreSQL versions

///

## What condition must be met before switching over a blue/green deployment?

---

A) The blue environment must be at least 24 hours old

B) All applications must be reconfigured to point to the green environment

C) The green environment must have more storage capacity than the blue environment

D) Replica lag should be close to zero

---

Replica lag should be close to zero

///

## What happens to external replicas after switching over an RDS for MySQL blue/green deployment?

---

A) They continue replicating from the old blue environment

B) They are automatically updated to point to the new production environment

C) They are deleted and must be recreated

D) They must have their parent node manually updated to maintain replication

---

They must have their parent node manually updated to maintain replication

///

## Which statement about deleting a blue/green deployment is TRUE?

---

A) You cannot delete a blue/green deployment after switchover

B) Deleting a blue/green deployment automatically creates a snapshot of both environments

C) The blue environment is not affected when deleting a blue/green deployment

D) Deleting a blue/green deployment always deletes both blue and green environments

---

The blue environment is not affected when deleting a blue/green deployment

///

## What is a limitation of RDS for PostgreSQL blue/green deployments that use logical replication?

---

A) They can only be used with instances smaller than 8xlarge

B) They cannot be used for major version upgrades

C) They require manual intervention every hour to maintain synchronization

D) Tables must have a primary key for UPDATE and DELETE operations

---

Tables must have a primary key for UPDATE and DELETE operations

///

## What action does Amazon RDS take during switchover to ensure application compatibility?

---

A) Creates a copy of all application code with updated database references

B) Temporarily duplicates all write operations to both environments

C) Automatically updates application connection strings

D) Renames the green environment endpoints to match the corresponding blue environment endpoints

---

Renames the green environment endpoints to match the corresponding blue environment endpoints

///

## Which CloudWatch metric should you check before switching over a blue/green deployment?

---

A) ReadIOPS

B) FreeStorageSpace

C) CPUUtilization

D) DatabaseConnections

---

DatabaseConnections

///

## What is the default timeout period for a blue/green deployment switchover?

---

A) 120 seconds

B) 3600 seconds

C) 30 seconds

D) 300 seconds

---

300 seconds

///

## What happens if you make DDL changes in the blue environment of a PostgreSQL blue/green deployment using logical replication?

---

A) The changes are queued and applied after switchover

B) The changes are automatically applied to the green environment

C) The switchover is automatically triggered

D) The deployment enters a state of "Replication degraded"

---

The deployment enters a state of "Replication degraded"

///

## What is the purpose of storage initialization in a blue/green deployment?

---

A) To minimize the storage footprint of the green environment

B) To create an automated backup before switchover

C) To encrypt data stored in the green environment

D) To proactively download all blocks from S3 for maximum volume performance

---

To proactively download all blocks from S3 for maximum volume performance
