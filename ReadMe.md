# ClickHouse Traffic Data API

This repository contains a Flask application for managing traffic data stored in ClickHouse.

## Requirements
- Docker
- Docker Compose
- env file

## ENV File
create a .env file and the values:
- DEBUG=True | for select application debug mode. default is "False"
- CLICKHOUSE_DB="default" | default clickhouse database for connection
- CLICKHOUSE_USER="snappcab" | clickhouse username. default is "default"
- CLICKHOUSE_PASSWORD="snappcap" | clickhouse user password. default is ""
- CLICKHOUSE_HOST="clickhouse" | clickhouse database host. default is "localhost"
- WORKING_DB="snapp" | Name of the database that application creates


## Database
the application using sqlalchemy and clickhouse for database, for running on localhost:
1. sudo apt-get install apt-transport-https ca-certificates dirmngr
2. sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4
3. echo "deb https://repo.clickhouse.tech/deb/stable/ main/" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list
4. sudo apt-get update
5. sudo apt-get install -y clickhouse-server clickhouse-client
6. sudo service clickhouse-server start


## Running the Application With Docker
1. Navigate to the cloned directory.
2. Run `docker-compose up -d` to build and start the application containers.
3. The Flask application will be available at http://localhost:5000.


## UnitTest

for running unit test script: Run `python -m unittest`


## Endpoints

The file postman-api-document.json is a postman export with examples for all endpoints document

### Create Traffic Data
- Method: POST
- URL: /api/v1/traffic
- Content-Type: application/json
- Request Body Schema:
  ```json
  {
    "user_id": int,
    "created_at": "datetime with format %Y-%m-%d %H:%M:%S",
    "page_url": "string"
  }

### Update Traffic Data
- Method: PUT
- URL: /api/v1/traffic/{request_id}
- Content-Type: application/json
- Request Body Schema:
  ```json
  {
    "user_id": int,
    "created_at": "datetime with format %Y-%m-%d %H:%M:%S",
    "page_url": "string"
  }
  
### Read Traffic Data
- Method: GET
- URL: /api/v1/traffic/daily/{user_id}
- Content-Type: application/json
