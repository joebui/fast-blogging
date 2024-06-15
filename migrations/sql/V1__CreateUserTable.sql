CREATE TABLE users (
  id bigserial PRIMARY KEY,
  name varchar NOT NULL,
  password_hash varchar NOT NULL,
  password_salt varchar NOT NULL
);

CREATE UNIQUE INDEX users_name_idx ON users(name);
