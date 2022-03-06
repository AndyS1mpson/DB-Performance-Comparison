from cProfile import label
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from utils.generate_data import generate_city, generate_country
import matplotlib.pyplot as plt
import schemas, services
from api.deps import get_db_pg, get_local_pg, get_remote_pg
import utils
import time

router = APIRouter()


@router.post(
    "/country/{amount}",
    status_code=status.HTTP_201_CREATED,
    summary="Sends queries to local, dockerized and remote databases. \
             Saves a graph of the time spent on each request"
)
def check_performance_with_country_model(amount: int):
    docker_db_session: Session = next(get_db_pg())
    local_db_session: Session = next(get_local_pg())
    remote_db_session: Session = next(get_remote_pg())

    dc_times = []
    loc_times = []
    remote_times = []

    x = list(range(amount))

    for _ in x:
        # generate country data
        country = generate_country()
        # check elapsed time for docker database
        start = time.time()
        services.create_country(db=docker_db_session, country=country)
        dc_times.append(time.time() - start)
        # check elapsed time for local database
        start = time.time()
        services.create_country(db=local_db_session, country=country)
        loc_times.append(time.time() - start)
        start = time.time()
        services.create_country(db=remote_db_session, country=country)
        remote_times.append(time.time() - start)       



    plt.plot(x, dc_times, 'r', label="dockerized database")
    plt.plot(x, loc_times, 'g', label="local database")
    plt.plot(x, remote_times, 'b', label="remote database")
    plt.legend()
    plt.savefig('performance.png')

