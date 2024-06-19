CREATE TABLE users (
  id bigserial PRIMARY KEY,
  name varchar NOT NULL,
  password_hash varchar NOT NULL,
  created_at timestamp NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX users_name_idx ON users(name);
