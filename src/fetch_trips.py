from urllib.error import HTTPError, URLError

import pandas as pd
from prefect import task

TLC_TRIP_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
REQUIRED_COLUMNS = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "duration",
    "month",
    "year",
]


@task(name="fetch_trips", retries=3, log_prints=True)
def fetch_trips(color: str, year: int, month: int) -> pd.DataFrame:
    url = f"{TLC_TRIP_DATA_URL}{color}_tripdata_{year}-{month:>02}.parquet"
    try:
        print(f"Fetching {color} trips in {year}/{month}.")
        trips = pd.read_parquet(url)
        trips["month"] = month
        trips["year"] = year

        return process_trips(trips)
    except (HTTPError, URLError):
        print(f"Failed to fetch {color} trip in {year}/{month}.")


def process_trips(trips: pd.DataFrame) -> pd.DataFrame:
    trips = trips.copy()

    trips["tpep_pickup_datetime"] = pd.to_datetime(trips.tpep_pickup_datetime)
    trips["tpep_dropoff_datetime"] = pd.to_datetime(trips.tpep_dropoff_datetime)
    trips["duration"] = (
        trips.tpep_dropoff_datetime - trips.tpep_pickup_datetime
    ).dt.total_seconds() / 60

    trips["duration"] = trips["duration"].round(2)

    return trips[REQUIRED_COLUMNS]
