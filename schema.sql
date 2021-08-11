
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id INT  NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	created_at DATE NOT NULL,
	updated_at DATE NOT NULL
);



CREATE TABLE books (
	id INT NOT NULL PRIMARY KEY,
	user_id INT REFERENCES users (id) ON DELETE CASCADE,
	name VARCHAR(50) NOT NULL,
	pages INT NOT NULL,
	created_at DATE NOT NULL,
	updated_at DATE NOT NULL
);







