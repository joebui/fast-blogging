#!/bin/sh

NETWORK='fastapi_default'
DOCKER_IMG='flyway/flyway:10'
POSTGRES_URL='jdbc:postgresql://postgres:5432/blog?user=postgres&password=root'

docker run --rm -v $PWD/migrations/sql:/flyway/sql \
  --network $NETWORK $DOCKER_IMG \
  -url=$POSTGRES_URL \
  -connectRetries=60 \
  -baselineOnMigrate=true \
  -validateMigrationNaming=true \
  migrate
