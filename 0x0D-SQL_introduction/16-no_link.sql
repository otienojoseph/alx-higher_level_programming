-- List all records of the table second_table
-- Dont list rows without a name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
