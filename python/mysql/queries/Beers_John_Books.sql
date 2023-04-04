INSERT INTO users (name)
VALUES ("Jane Amsden");

INSERT INTO users (name)
VALUES ("Emily Dixon");

INSERT INTO users (name)
VALUES ("Theodore Dostoevsky");

INSERT INTO users (name)
VALUES ("William Shapiro");

INSERT INTO users (name)
VALUES ("Lao Xiu");

INSERT INTO books (title)
VALUES ("C Sharp");

INSERT INTO books (title)
VALUES ("Java");

INSERT INTO books (title)
VALUES ("Python");

INSERT INTO books (title)
VALUES ("PHP");

INSERT INTO books (title)
VALUES ("Ruby");

UPDATE books
SET title = "C#"
WHERE id = 1;

UPDATE users
SET name = "Bill"
WHERE id = 4;

INSERT INTO favorites (user_id, book_id)
VALUES (1, 1);

INSERT INTO favorites (user_id, book_id)
VALUES (1, 2);

INSERT INTO favorites (user_id, book_id)
VALUES (2, 1);

INSERT INTO favorites (user_id, book_id)
VALUES (2, 2);

INSERT INTO favorites (user_id, book_id)
VALUES (2, 3);

INSERT INTO favorites (user_id, book_id)
VALUES (3, 1);

INSERT INTO favorites (user_id, book_id)
VALUES (3, 2);

INSERT INTO favorites (user_id, book_id)
VALUES (3, 3);

INSERT INTO favorites (user_id, book_id)
VALUES (3, 4);

INSERT INTO favorites (user_id, book_id)
VALUES (4, 1);

INSERT INTO favorites (user_id, book_id)
VALUES (4, 2);

INSERT INTO favorites (user_id, book_id)
VALUES (4, 3);

INSERT INTO favorites (user_id, book_id)
VALUES (4, 4);

INSERT INTO favorites (user_id, book_id)
VALUES (4, 5);

SELECT * FROM users
JOIN favorites ON users.id = favorites.user_id
WHERE book_id = 3;

DELETE FROM favorites
WHERE book_id = 3
LIMIT 1;

INSERT INTO favorites (user_id, book_id)
VALUES (5, 2);

SELECT * FROM books
JOIN favorites ON books.id = favorites.user_id
WHERE favorites.user_id = 3;

SELECT * FROM books
JOIN favorites ON books.id = favorites.user_id
WHERE favorites.book_id = 5;