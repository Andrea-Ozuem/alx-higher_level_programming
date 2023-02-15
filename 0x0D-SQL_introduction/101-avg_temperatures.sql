-- Import in hbtn_0c_0 database a table
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
IMPORT TABLE FROM "temperatures.sql";
UNLOCK TABLES;
SELECT city, AVG(value) AS "avg_temp" ORDER BY `avg_temp` DESC;
