SELECT
    transaction_date,
    COALESCE(SUM(CASE WHEN amount % 2 = 1 THEN amount END), 0) AS odd_sum,
    COALESCE(SUM(CASE WHEN amount % 2 = 0 THEN amount END), 0) AS even_sum
FROM Transactions
GROUP BY transaction_date
ORDER BY transaction_date;