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
