INSERT INTO users (first_name, last_name, email) 
VALUES('John', 'Doe', 'johndoe@somemail.com');

INSERT INTO users (first_name, last_name, email) 
VALUES('Jane', 'Smith', 'smith.jane@somemail.com');

INSERT INTO users (first_name, last_name, email) 
VALUES('Bill', 'Smith', 'bsmith@esomemail.com');

SELECT * FROM users; 

SELECT email FROM users
WHERE id = 1;

SELECT id, created_at FROM users
ORDER BY created_at DESC
LIMIT 1;

UPDATE users
SET last_name = "Pancakes"
WHERE id = 3;

DELETE FROM users WHERE ID = 2;

SELECT * FROM users
ORDER BY first_name; 

SELECT * FROM users
ORDER BY first_name DESC; 