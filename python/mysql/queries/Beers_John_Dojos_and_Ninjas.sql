INSERT INTO dojos (name)
VALUES ('Cobra Kai');

INSERT INTO dojos (name)
VALUES ('Miyagi Do');

INSERT INTO dojos (name)
VALUES ('Eagle Fang');

DELETE FROM dojos WHERE id <= 3;

INSERT INTO dojos (name)
VALUES ('Alpha');

INSERT INTO dojos (name)
VALUES ('Beta');

INSERT INTO dojos (name)
VALUES ('Omega');

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('John', 'Doe', 21, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jane', 'Smith', 23, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Bill', 'Smith', 25, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Daniel', 'Laruso', 17, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jason', 'Vorhees', 99, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Michael', 'Myers', 30, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Betty', 'Crocker', 23, 6);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Mr', 'Peanut', 19, 6);

SELECT * FROM ninjas
WHERE dojo_id = 4;

SELECT * FROM ninjas
WHERE dojo_id = 6; 

SELECT dojo_id FROM ninjas
ORDER BY created_at DESC
LIMIT 1;