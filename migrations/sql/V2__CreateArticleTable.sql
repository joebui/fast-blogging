CREATE TABLE articles (
  id bigserial PRIMARY KEY,
  title varchar(255) NOT NULL,
  description text,
  owner_id bigint NOT NULL,
  content text,
  created_at timestamp NOT NULL DEFAULT now()
);

ALTER TABLE
  articles
ADD
  CONSTRAINT articles_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES users(id);
