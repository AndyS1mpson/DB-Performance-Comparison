# from typing import List, Tuple

# from mixer.backend.sqlalchemy import Mixer
# from sqlalchemy.orm import Session

# from api.deps import get_db_pg, get_local_pg
# from db import base as models
# import requests
# import time
# import random
# import string

# # def db_fixture(db: Session) -> List:
# #     """Generate data for test performance.
    
# #     Returns:
# #         List: ids of all created cities.
# #     """

# #     cities_ids = []
# #     mixer = Mixer(session=db)

# #     for i in range(100):
# #         country = mixer.blend(models.Country)
# #         city = mixer.blend(models.City, country=country.name)
# #         cities_ids.append(city.id)

# #     return cities_ids
# def get_random_string(length) -> str:
#     """Generate random string with fix length."""
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     print(result_str)


# def get_db_write_elapsed_times(db: Session, db_location: str) -> Tuple[List, List]:
#     """Get times of requests to database."""
#     times = []
#     ids = []
#     for _ in range(5):
#         country = {
#             "name": get_random_string(10)
#         }
#         start = time.time()
#         response = requests.post(f"http://0.0.0.0:8080/country/{db_location}", json=country)
#         times.append(time.time() - start)
#         country = response.json()
#         ids.append(country["id"])
#     return ids, times


# def get_db_read_elapsed_time(db: Session, ids: List, db_location: str) -> List:
#     """Get times of requests to database."""
#     times = []
#     ids = []
#     for id in ids:
#         start = time.time()
#         requests.get(f"http://0.0.0.0:8080/country/{db_location}/{id}")
#         times.append(time.time() - start)
#     return times


# def test_performance(db: Session, db_location: str) -> Tuple[List, List]:
#     """Test database performance.

#     Args:
#         db:
#             database session.
#         db_location:
#             db location: localperform/docker/remote. 

#     Returns:
#         Tuple[List, List]:
#             tuple of ids and elapsed times.
#     """
#     db = db
#     ids = db_fixture(db=db)
#     times = get_db_elapsed_times(
#         db=db,
#         ids=ids,
#         db_location=db_location
#     )
#     return ids, times

# def perform


# if __name__ == "__main__":
#     docker_session = next(get_db_pg())




#     print(times)
import psycopg2
conn = psycopg2.connect(
    host="127.0.0.1",
    database="local_app_db",
    user="app_user",
    password="postgres")

print(conn)