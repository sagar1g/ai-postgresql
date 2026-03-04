import psycopg2
import pandas as pd
from datetime import datetime
import config
import os

report_dir="reports"

def connect_db():

    conn=psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        port=config.DB_PORT
    )

    return conn


def slow_queries(conn):

    query="""
    SELECT query,
           calls,
           total_exec_time,
           mean_exec_time
    FROM pg_stat_statements
    ORDER BY total_exec_time DESC
    LIMIT 20
    """

    df=pd.read_sql(query,conn)

    slow=df[df["mean_exec_time"]>config.SLOW_QUERY_THRESHOLD]

    return df,slow


def check_connections(conn):

    q="""
    SELECT count(*) FROM pg_stat_activity
    """

    cur=conn.cursor()
    cur.execute(q)

    result=cur.fetchone()[0]

    return result


def replication_lag(conn):

    q="""
    SELECT EXTRACT(EPOCH FROM now()-pg_last_xact_replay_timestamp())
    """

    cur=conn.cursor()

    try:
        cur.execute(q)
        lag=cur.fetchone()[0]
    except:
        lag="Primary Server"

    return lag


def recommend_index(query):

    if "WHERE" in query.upper():
        return "Create index on filter columns"

    return "Check query execution plan"


def generate_report(all_queries,slow_queries,connections,lag):

    file_name="reports/report_"+datetime.now().strftime("%Y%m%d_%H%M")+".txt"

    with open(file_name,"w") as f:

        f.write("AI PostgreSQL DBA Monitoring Report\n")
        f.write("===================================\n\n")

        f.write("Total Queries Analyzed: "+str(len(all_queries))+"\n")
        f.write("Slow Queries: "+str(len(slow_queries))+"\n\n")

        f.write("Active Connections: "+str(connections)+"\n")

        f.write("Replication Lag: "+str(lag)+"\n\n")

        f.write("Slow Query Details\n")
        f.write("------------------\n\n")

        for i,row in slow_queries.iterrows():

            f.write("Query:\n"+row["query"]+"\n")

            f.write("Calls:"+str(row["calls"])+"\n")

            f.write("Mean Execution Time:"+str(row["mean_exec_time"])+"\n")

            rec=recommend_index(row["query"])

            f.write("Recommendation:"+rec+"\n")

            f.write("\n-----------------------------\n\n")

    print("Report generated:",file_name)


def main():

    print("AI PostgreSQL DBA Monitoring System\n")

    conn=connect_db()

    all_queries,slow=slow_queries(conn)

    connections=check_connections(conn)

    lag=replication_lag(conn)

    generate_report(all_queries,slow,connections,lag)

    conn.close()

    print("Monitoring completed")


if __name__=="__main__":
    main()