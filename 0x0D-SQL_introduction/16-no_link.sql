-- list all records with names
SELECT score, name FROM second_table
WHERE name <> NULL
ORDER BY score DESC;
