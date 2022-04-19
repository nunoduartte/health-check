import jaydebeapi


class DatabaseCheck:
    def __init__(self, host, port, database_name, user, password, statements, jtds_jar_path):
        self.driver_name = "net.sourceforge.jtds.jdbc.Driver"
        self.connection_url = "jdbc:jtds:sqlserver://"+host+":" + port + "/" + database_name
        self.connection_properties = {
            "user": user,
            "password": password,
        }
        self.statements = statements
        self.jtds_jar_path = jtds_jar_path

    def run(self):
        try:
            connection = jaydebeapi.connect(self.driver_name, self.connection_url, self.connection_properties, self.jtds_jar_path)
            cursor = connection.cursor()
            cursor.execute(self.statements[0])
            res = cursor.fetchall()
            if res:
                print(str(res))
            connection.close()
        except Exception as err:
            print(str(err))
