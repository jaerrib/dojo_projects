INSERT INTO users (first_name, last_name)
VALUES ('Amy', 'Giver');

INSERT INTO users (first_name, last_name)
VALUES ('Eli', 'Byers');

INSERT INTO users (first_name, last_name)
VALUES ('Marky', 'Mark');

INSERT INTO users (first_name, last_name)
VALUES ('Big', 'Bird');

INSERT INTO users (first_name, last_name)
VALUES ('Kermit', 'The Frog');

INSERT INTO users (first_name, last_name)
VALUES ('Oscar', 'The Grouch');

INSERT INTO friendships (user_id, friend_id)
VALUES (1, 2);

INSERT INTO friendships (user_id, friend_id)
VALUES (1, 4);

INSERT INTO friendships (user_id, friend_id)
VALUES (1, 6);

INSERT INTO friendships (user_id, friend_id)
VALUES (2, 1);

INSERT INTO friendships (user_id, friend_id)
VALUES (2, 3);

INSERT INTO friendships (user_id, friend_id)
VALUES (2, 5);

INSERT INTO friendships (user_id, friend_id)
VALUES (3, 2);

INSERT INTO friendships (user_id, friend_id)
VALUES (3, 5);

INSERT INTO friendships (user_id, friend_id)
VALUES (4, 3);

INSERT INTO friendships (user_id, friend_id)
VALUES (5, 1);

INSERT INTO friendships (user_id, friend_id)
VALUES (5, 6);

INSERT INTO friendships (user_id, friend_id)
VALUES (6, 2);

INSERT INTO friendships (user_id, friend_id)
VALUES (6, 3);

SELECT users.first_name as first_name, users.last_name as last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users 
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id;

SELECT users.first_name as first_name, users.last_name as last_name FROM users 
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id
WHERE friendships.friend_id = 1;
