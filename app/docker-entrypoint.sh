#!/bin/bash

APP_UVICORN_OPTIONS="${APP_UVICORN_OPTIONS:---host 0.0.0.0 --port=8080}"

alembic -n postgres update head
uvicorn ${APP_UVICORN_OPTIONS} main:app
