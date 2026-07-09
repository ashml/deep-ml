-- your query
SELECT *
FROM (SELECT department, name, salary, DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rnk
      FROM employees) r
WHERE rnk <= 3