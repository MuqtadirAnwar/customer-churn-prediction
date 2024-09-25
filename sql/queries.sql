-- Identify customers at high risk of churn (low engagement and no recent purchases)
SELECT CustomerID, Age, Location, DaysSinceLastPurchase, LoginFrequency
FROM customers
WHERE LoginFrequency = 'Monthly'
  AND DaysSinceLastPurchase > 60
ORDER BY DaysSinceLastPurchase DESC;

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
ORDER BY AvgOrderValue DESC;

-- Identify top customers by total purchases and loyalty score
SELECT CustomerID, TotalPurchases, LoyaltyScore
FROM customers
ORDER BY TotalPurchases DESC, LoyaltyScore DESC
LIMIT 10;


-- Calculate churn rate by location
SELECT Location,
       COUNT(*) AS TotalCustomers,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
       CAST(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS ChurnRate
FROM customers
GROUP BY Location
ORDER BY ChurnRate DESC;

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
ORDER BY ChurnRate DESC;
