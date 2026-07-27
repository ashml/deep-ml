-- your query
SELECT user_id, MAX(streak_length) AS longest_streak
FROM (
  SELECT user_id, COUNT(*) AS streak_length
  FROM (
    SELECT user_id, visit_date,
           ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY visit_date) AS rn,
           visit_date - INTERVAL '1 day' * (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY visit_date) - 1) AS date_group
    FROM visits
    WHERE visit_date < CURRENT_DATE
  ) t
  GROUP BY user_id, date_group
)
GROUP BY user_id
ORDER BY longest_streak DESC, user_id ASC
LIMIT 100;