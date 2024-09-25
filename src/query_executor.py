import pandas as pd
import sqlite3

# Project Structure Paths (Adjust if needed)
DATA_PROCESSED_DIR = "customer_churn_prediction/data/processed/"
SQL_DIR = "customer_churn_prediction/sql/"

# 1. Read CSV
csv_file_path = DATA_PROCESSED_DIR + "processed_customer_data.csv"
df = pd.read_csv(csv_file_path)

# 2. Create SQLite Database
conn = sqlite3.connect(':memory:')  # In-memory database

# 3. Load DataFrame into Database
table_name = "customers"
df.to_sql(table_name, conn, if_exists='replace', index=False)

# 4. Read SQL Queries
sql_file_path = SQL_DIR + "queries.sql"
with open(sql_file_path, 'r') as file:
    sql_queries = file.read()

# 5. Execute Queries & Process Results
for query in sql_queries.split(';'):
    query = query.strip()
    if query:
        try:
            result_df = pd.read_sql_query(query, conn)
            print(f"\nResults for query:\n{query}\n")
            print(result_df.to_string(index=False))
            # Further processing can be added here (e.g., save to file)
        except pd.io.sql.DatabaseError as e:
            print(f"Error executing query: {query}\n{e}")

# Close the connection
conn.close()
