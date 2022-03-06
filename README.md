# DB-Performance-Comparison
Databases performance comparison study project

## Разработка

## Структура проекта

```
-> *app*
   -> *alembic* — папка с миграциями
   -> *api* — слой с логикой обработки запросов через api
   -> *config* — глобальные для проекта вещи, вроде настроек (`config.py`)
   -> *db* — инициализация базы и сессии (скорее всего в процессе работы над проектом изменяться не будет)
   -> *models* — модели в терминологии SQLAlchemy (не путать с *schemas* в pydantic и бизнес-моделями)
   -> *schemas* — схемы для валидации/сериализации объектов запроса/ответа (они же модели в терминологии pydantic)
   -> *services* — сервисный слой, здесь размещается вся бизнес-логика.
-> *.env* — файл для перечисления всех используемых внутри сервиса переменных среды
```

* Создайте виртуальную среду:
~~~console
python -m venv venv
~~~

* В виртуальном окружении установите зависимости:
~~~console
pip install -r app/requirements.txt
~~~

* В корневой папке создайте файл .env со следующими переменными:
~~~console
APP_UVICORN_OPTIONS  

# Dockerized database parameters.
DOCKER_POSTGRES_USER  
DOCKER_POSTGRES_PASSWORD  
DOCKER_POSTGRES_DB  
DOCKER_POSTGRES_HOST  
DOCKER_POSTGRES_PORT  
PGDATA  
DOCKER_POSTGRES_URL  

# Local database parameters.  
LOCAL_POSTGRES_USER  
LOCAL_POSTGRES_PASSWORD  
LOCAL_POSTGRES_DB  
LOCAL_POSTGRES_HOST  
LOCAL_POSTGRES_PORT  
LOCAL_POSTGRES_URL  

# Remote database parameters.
REMOTE_POSTGRES_USER  
REMOTE_POSTGRES_PASSWORD  
REMOTE_POSTGRES_DB  
REMOTE_POSTGRES_HOST  
REMOTE_POSTGRES_URL  
~~~

* Экспортируйте переменные в окружающую среду:
~~~console
source app/scripts/export_env.sh
~~~

* Запустите контейнер с базой данных следующей командой:
~~~console
docker-compose up --build
~~~

* В отдельном терминале запустите сервис следующей командой:
~~~console
uvicorn app.main:app --reload
~~~

Документацию API можно посмотреть по следующему URL: http://0.0.0.0:8000/docs
