import pandas as pd
from prefect import task

from src.postgres import create_pg_engine


@task(name="ingest_trips", retries=3, log_prints=True)
def ingest_trips_to_pg(trips: pd.DataFrame, color: str) -> None:
    table_name = f"nyc_taxi_trip_{color}"
    pg_engine = create_pg_engine()

    print(f"Writing {len(trips)} trips to {table_name}.")
    trips.to_sql(name=table_name, con=pg_engine, if_exists="append")
