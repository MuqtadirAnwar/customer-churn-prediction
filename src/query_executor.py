import pandas as pd
import sqlite3

# Project Structure Paths (Adjust if needed)
DATA_PROCESSED_DIR = "../data/processed/"
SQL_DIR = "../sql/"

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
            if result_df.empty:
                print("No results found for this query.")
            else:
                print(result_df.to_string(index=False))
            # Further processing can be added here (e.g., save to file)
        except pd.io.sql.DatabaseError as e:
            print(f"Error executing query: {query}\n{e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Close the connection
conn.close()

"""

Results for query:
-- Identify customers at high risk of churn (low engagement and no recent purchases)
SELECT CustomerID, Age, DaysSinceLastPurchase, LoginFrequency
FROM customers
WHERE LoginFrequency = 'Monthly'  -- Changed from LoginFrequencyNumeric
  AND DaysSinceLastPurchase > 60
ORDER BY DaysSinceLastPurchase DESC

 CustomerID  Age  DaysSinceLastPurchase LoginFrequency
       1027   43                    458        Monthly
       1057   41                    458        Monthly
       1081   42                    458        Monthly
       1015   58                    453        Monthly
       1045   42                    453        Monthly
       1069   40                    453        Monthly
       1039   57                    448        Monthly
       1021   40                    443        Monthly
       1075   45                    443        Monthly
       1051   44                    438        Monthly
       1087   44                    438        Monthly
       1033   41                    433        Monthly
       1063   43                    433        Monthly
       1009   42                    302        Monthly
       1004   55                    300        Monthly

Results for query:
-- Calculate average order value by age group
SELECT
  CASE
    WHEN Age BETWEEN 18 AND 25 THEN '18-25'
    WHEN Age BETWEEN 26 AND 35 THEN '26-35'
    WHEN Age BETWEEN 36 AND 45 THEN '36-45'
    WHEN Age BETWEEN 46 AND 55 THEN '46-55'
    ELSE '55+'
  END AS AgeGroup,
  AVG(AvgOrderValue) AS AvgOrderValue
FROM customers
GROUP BY AgeGroup
ORDER BY AvgOrderValue DESC

AgeGroup  AvgOrderValue
     55+     105.775000
   46-55      90.236842
   36-45      89.481481
   26-35      52.008621
   18-25      40.500000

Results for query:
-- Identify top customers by total purchases and loyalty score
SELECT CustomerID, TotalPurchases, LoyaltyScore
FROM customers
ORDER BY TotalPurchases DESC, LoyaltyScore DESC
LIMIT 10

 CustomerID  TotalPurchases  LoyaltyScore
       1005              30      7.239726
       1028              29      7.215068
       1052              29      7.215068
       1076              29      7.215068
       1010              28      7.190938
       1040              28      7.190411
       1070              28      7.190411
       1088              28      7.190411
       1016              27      7.165753
       1034              27      7.165753

Results for query:
-- Calculate churn rate by location (modified for one-hot encoded locations)
-- Example for 'Location_New York' - repeat for other locations as needed
SELECT
       COUNT(*) AS TotalCustomers,
       SUM(CASE WHEN Churn = 'Yes' AND "Location_New York" = 1 THEN 1 ELSE 0 END) AS ChurnedCustomers,
       CAST(SUM(CASE WHEN Churn = 'Yes' AND "Location_New York" = 1 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS ChurnRate
FROM customers

 TotalCustomers  ChurnedCustomers  ChurnRate
             88                 0        0.0

Results for query:
-- Analyze the relationship between support interactions and churn
SELECT
  CASE
    WHEN SupportInteractions = 0 THEN 'No Interactions'
    WHEN SupportInteractions BETWEEN 1 AND 2 THEN '1-2 Interactions'
    WHEN SupportInteractions BETWEEN 3 AND 5 THEN '3-5 Interactions'
    ELSE '6+ Interactions'
  END AS InteractionGroup,
  COUNT(*) AS TotalCustomers,
  SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
  CAST(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS ChurnRate
FROM customers
GROUP BY InteractionGroup
ORDER BY ChurnRate DESC

InteractionGroup  TotalCustomers  ChurnedCustomers  ChurnRate
3-5 Interactions              15                 8   0.533333
1-2 Interactions              51                16   0.313725
No Interactions              22                 6   0.272727

 """
