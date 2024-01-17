-- a script that creates a table called first_table in the current database
-- in your MySQL server.
-- first_table description: id INT, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command.
-- If the table first_table already exists, your script should not fail.
-- I'm not allowed to use the SELECT or SHOW statements.
CREATE TABLE IF NOT EXISTS second_table(
	id int DEFAULT NULL,
	name VARCHAR(256) DEFAULT NULL,
	score int DEFAULT NULL);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14),
(4, 'George', 8);
