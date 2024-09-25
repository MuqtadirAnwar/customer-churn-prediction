-- Identify customers at high risk of churn (low engagement and no recent purchases)
SELECT CustomerID, Age, Location, DaysSinceLastPurchase, LoginFrequency
FROM customers
WHERE LoginFrequency = 'Monthly'
  AND DaysSinceLastPurchase > 60
ORDER BY DaysSinceLastPurchase DESC;
