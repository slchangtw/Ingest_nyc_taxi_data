# Ingest NYC Taxi Data

This project's objective is to retrieve [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) on a scheduled basis using Prefect. The collected data is then processed and stored in a PostgreSQL database. The orchestration of these services is managed through Docker Compose.

## Start the services

Start the services by running the commands within the root directory.

```bash
docker-compose build
docker-compose up -d
```

## Check the schedules in Prefect Server

Proceed to [http://localhost:4200](http://localhost:4200) and select the "Deployment" section. You'll find a scheduled task configured to run every two months on the first day of each month. This schedule aligns with the update frequency of the website. The task is designed to fetch data from the past two months. It's worth noting that, at present, the task retrieves data from the same month in the previous year since data for the current year is not yet available.

<img src="./images/schedule.png" alt="schedule" height="210" width="500"/></p>

To manually execute the task, select *Run* followed by *Quick Run* in the upper-right corner of the task. After the task is complete, you can review the results and access the logs for further information.

<img src="./images/task_result.png" alt="task_result" height="210" width="500"/></p>

## Check the data in PostgresSQL

To access the PostgreSQL data, navigate to [pgAdmin](http://localhost:8080). You can log in with the username `admin@admin.com` and the password `admin`. To register the server, please enter the information as indicated in the figures. Ensure that the server name matches the configuration provided in `docker-compose.yml`.

<img src="./images/pgadmin1.png" alt="pdadmin1" height="350" width="350"/></p>
<img src="./images/pgadmin2.png" alt="pgadmin2" height="350" width="350"/></p>

Once the server is registered, you can execute queries to verify that the data has been successfully stored in the database.

<img src="./images/query1.png" alt="query1" height="350" width="300"/></p>
<img src="./images/query2.png" alt="query2" height="350" width="550"/></p>

## Clean up

To stop the services, execute the following command in the root directory:

```bash
docker compose down --rmi all
```

This will stop and remove the images and containers defined in the Docker Compose configuration.
