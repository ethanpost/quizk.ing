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

A) Green environment

B) Blue environment

C) Staging environment

D) Test environment

---

B

///

## How long does a blue/green deployment switchover typically take?

A) Less than one minute

B) 5-10 minutes

C) 30-60 minutes

D) Several hours

---

A

///

## Which of the following database engines are supported for Amazon RDS Blue/Green Deployments?

A) RDS for Oracle, RDS for SQL Server, and RDS for DB2

B) RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL

C) Aurora MySQL, Aurora PostgreSQL, and RDS for Oracle

D) RDS for SQL Server, RDS for MySQL, and RDS for MariaDB

---

B

///

## What is a switchover guardrail?

A) A physical barrier that prevents unauthorized access to the database

B) A check that prevents switchover if environments aren't ready to avoid downtime and data loss

C) A backup system that activates if the switchover fails

D) A monitoring tool that tracks database performance during switchover

---

B

///

## Which permission is required to switch over a blue/green deployment?

A) rds:CreateBlueGreenDeployment

B) rds:DeleteBlueGreenDeployment

C) rds:SwitchoverBlueGreenDeployment

D) rds:ModifyBlueGreenDeployment

---

C

///

## What happens to database connections during a blue/green deployment switchover?

A) Connections remain active throughout the process

B) Only read connections remain active, write connections are dropped

C) Connections are dropped and new connections aren't allowed temporarily

D) Connections are automatically redirected to the green environment

---

C

///

## What is lazy loading in the context of blue/green deployments?

A) A method to reduce database workload during peak hours

B) A process where data blocks are loaded only as applications request them

C) A technique to optimize database query performance

D) The automatic scaling of database resources based on demand

---

B

///

## What happens to the blue environment after a switchover?

A) It is automatically deleted

B) It becomes the new staging environment

C) It is retained and renamed with "-oldn" suffix

D) It is immediately upgraded to match the green environment

---

C

///

## Which of the following is NOT a benefit of using blue/green deployments?

A) Reducing database storage costs

B) Testing database changes safely without affecting production

C) Implementing and testing newer database features

D) Minimizing downtime during database updates

---

A

///

## When does Amazon RDS use logical replication instead of physical replication for PostgreSQL blue/green deployments?

A) When the source instance has read replicas

B) When requesting a major version upgrade on supported PostgreSQL versions

C) When the source instance uses Multi-AZ deployment

D) When the green environment has different storage settings

---

B

///

## What condition must be met before switching over a blue/green deployment?

A) The green environment must have more storage capacity than the blue environment

B) Replica lag should be close to zero

C) All applications must be reconfigured to point to the green environment

D) The blue environment must be at least 24 hours old

---

B

///

## What happens to external replicas after switching over an RDS for MySQL blue/green deployment?

A) They are automatically updated to point to the new production environment

B) They are deleted and must be recreated

C) They continue replicating from the old blue environment

D) They must have their parent node manually updated to maintain replication

---

D

///

## Which statement about deleting a blue/green deployment is TRUE?

A) Deleting a blue/green deployment always deletes both blue and green environments

B) The blue environment is not affected when deleting a blue/green deployment

C) You cannot delete a blue/green deployment after switchover

D) Deleting a blue/green deployment automatically creates a snapshot of both environments

---

B

///

## What is a limitation of RDS for PostgreSQL blue/green deployments that use logical replication?

A) They cannot be used for major version upgrades

B) Tables must have a primary key for UPDATE and DELETE operations

C) They require manual intervention every hour to maintain synchronization

D) They can only be used with instances smaller than 8xlarge

---

B

///

## What action does Amazon RDS take during switchover to ensure application compatibility?

A) Automatically updates application connection strings

B) Creates a copy of all application code with updated database references

C) Renames the green environment endpoints to match the corresponding blue environment endpoints

D) Temporarily duplicates all write operations to both environments

---

C

///

## Which CloudWatch metric should you check before switching over a blue/green deployment?

A) CPUUtilization

B) DatabaseConnections

C) FreeStorageSpace

D) ReadIOPS

---

B

///

## What is the default timeout period for a blue/green deployment switchover?

A) 30 seconds

B) 120 seconds

C) 300 seconds

D) 3600 seconds

---

C

///

## What happens if you make DDL changes in the blue environment of a PostgreSQL blue/green deployment using logical replication?

A) The changes are automatically applied to the green environment

B) The deployment enters a state of "Replication degraded"

C) The switchover is automatically triggered

D) The changes are queued and applied after switchover

---

B

///

## What is the purpose of storage initialization in a blue/green deployment?

A) To encrypt data stored in the green environment

B) To proactively download all blocks from S3 for maximum volume performance

C) To minimize the storage footprint of the green environment

D) To create an automated backup before switchover

---

B
