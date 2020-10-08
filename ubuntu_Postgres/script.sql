CREATE TABLE IF NOT EXISTS nomes (
    name_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL
);

INSERT INTO nomes(name_id,name) VALUES(1,'enio');
INSERT INTO nomes(name_id,name) VALUES(2,'allan');