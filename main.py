
import os
from prometheus_client import start_http_server, Gauge
from database.database_check import DatabaseCheck
from network.network_check import NetworkCheck
import time

DATABASE_CONNECTION_CHECK = Gauge('database_connection_check', "Time of database connection")

if __name__ == '__main__':
    start_http_server(8000)

    statements = ['STATEMENTS']
    host = os.environ['HOST']
    port = os.environ['PORT']
    database_name = os.environ['DATABASE_NAME']
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    jar_path = os.environ['JAR_PATH']
    databaseCheck = DatabaseCheck(host, port, database_name, user, password, statements, jar_path)

    while True:
        start = time.time()
        databaseCheck.run()
        now = time.time()
        time_database_check_result = (now - start)
        DATABASE_CONNECTION_CHECK.set(time_database_check_result)
        print("TIME: " + str(time_database_check_result))
        time.sleep(30)



