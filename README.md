# AI PostgreSQL DBA Monitoring System

AI PostgreSQL DBA is a Python-based monitoring tool designed to help PostgreSQL DBAs automatically analyze database performance and detect issues such as slow queries.

The tool collects database statistics and generates reports that help DBAs quickly identify problems and take corrective actions.



# AI PostgreSQL DBA

## Project Structure

Create a project folder.

```bash
mkdir ai_postgresql_dba
cd ai_postgresql_dba
```

Folder structure:

```
ai_postgresql_dba
│
├── ai_postgres_monitor.py
├── config.py
├── requirements.txt
└── reports/
```

Create reports directory:

```bash
mkdir reports
```


# Prerequisites

Before running this project make sure you have:

```
Python 3.8+

PostgreSQL database

Required Python libraries

```

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-postgresql.git
cd ai-postgresql

````

# Install required dependencies:

```
pip install -r requirements.txt

```

# Configuration

Edit the config.py file and update your PostgreSQL connection details.

```
Example:

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "password"

```

# Usage

Run the monitoring script:

```
python3 ai_postgres_monitor.py

```

The script will analyze the database and generate reports inside the reports/ directory.

```
Example Output

The tool can detect:

Slow queries

Long running queries

Database health indicators

Performance metrics

```

# Run Monitoring

```
python3 ai_postgres_monitor.py

```

# Output:

AI PostgreSQL DBA Monitoring System

Report generated: reports/report_20260304_1010.txt

Monitoring completed

 
 # Example Report

Example output file:

```

AI PostgreSQL DBA Monitoring Report

Total Queries Analyzed: 20
Slow Queries: 3

Active Connections: 25
Replication Lag: 0

Slow Query Details

Query:
SELECT * FROM orders WHERE customer_id=10

Mean Execution Time: 3450 ms

Recommendation:
Create index on filter columns

```

# Automate Monitoring

Edit cron.

```
crontab -e

```

Add:

```
*/30 * * * * python3 /home/postgres/ai_postgresql_dba/ai_postgres_monitor.py

```
Now monitoring runs every 30 minutes.

Reports will be saved in the reports/ folder.
