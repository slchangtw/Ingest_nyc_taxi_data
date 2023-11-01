from datetime import date
from typing import Generator

from dateutil.relativedelta import relativedelta
from prefect import flow

from src.fetch_trips import fetch_trips
from src.ingest_trips import ingest_trips_to_pg


def get_last_two_months() -> Generator[tuple[int, int], None, None]:
    today = date.today()
    for _ in range(2):
        today = today - relativedelta(months=1)
        # The -1 is because the data after 2023/7 is not available yet.
        yield today.year - 1, today.month


@flow
def ingest_yellow_taxi_trips() -> None:
    color = "yellow"

    for year, month in get_last_two_months():
        trips = fetch_trips(color=color, year=year, month=month)
        ingest_trips_to_pg(color=color, trips=trips)


if __name__ == "__main__":
    ingest_yellow_taxi_trips.serve(
        name="ingest-yellow-taxi-trips",
        cron="0 0 1 */2 *",
        description="Ingest yellow taxi trips every two months.",
    )
