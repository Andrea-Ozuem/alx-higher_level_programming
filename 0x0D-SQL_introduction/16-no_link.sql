--  lists all records of the table second_table
-- Don't list rows without a name value
-- Results should display the score and the name in descending score
SELECT score, name FROM second_table WHERE name is NOT NULL ORDER BY score DESC;
