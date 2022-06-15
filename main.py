
import os
from prometheus_client import start_http_server, Gauge
from database.database_check import DatabaseCheck
from network.network_check import NetworkCheck
import time

DATABASE_CONNECTION_CHECK = Gauge('database_connection_check', "Time of database connection")
MIN_NETWORK_CONNECTION_TIME = Gauge('min_network_connection_time', "Min server ping time")
MAX_NETWORK_CONNECTION_TIME = Gauge('max_network_connection_time', "Max server ping time")
AVERAGE_NETWORK_CONNECTION_TIME = Gauge('average_network_connection_time', "Average server ping time")

if __name__ == '__main__':
    start_http_server(8000)

    statements = ['STATEMENTS']
    host = os.environ['HOST']
    port = os.environ['PORT']
    database_name = os.environ['DATABASE_NAME']
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    jar_path = os.environ['JAR_PATH']
    database_check = DatabaseCheck(host, port, database_name, user, password, statements, jar_path)
    network_check = NetworkCheck(host)


    while True:
        start = time.time()
        database_check.run()
        now = time.time()
        time_database_check_result = (now - start)
        DATABASE_CONNECTION_CHECK.set(time_database_check_result)

        min_time, max_time, average_time = network_check.run()
        MIN_NETWORK_CONNECTION_TIME.set(min_time)
        MAX_NETWORK_CONNECTION_TIME.set(max_time)
        AVERAGE_NETWORK_CONNECTION_TIME.set(average_time)

        print("database_query_time: " + str(time_database_check_result))
        print("min_ping_time: " + str(min_time))
        print("max_ping_time: " + str(max_time))
        print("average_ping_time: " + str(average_time))
        time.sleep(30)



