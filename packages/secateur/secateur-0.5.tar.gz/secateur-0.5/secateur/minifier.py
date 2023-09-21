from sqlalchemy import *
from drivers.postgresql.psql_secateur import PSQLSecateur
# from drivers.mysql.mysql_secateur import MySQLSecateur
# from drivers.oracle.oracle_secateur import OracleSecateur
# from drivers.mssql.mssql_secateur import MSSQLSecateur
# from drivers.sqlite.sqlite_secateur import SqliteSecateur

class Secateur:
    """
    Doc-string for main Secateur class.
    """
    def __init__(
        self,
        url=None,
        engine=None,
        connection=None,
        already_exist=False,
        debug_mode=True,
        verbose=True,
        log=True
    ):
        try:
            if already_exist:
                self.engine = engine
                self.connection = connection
            else:
                self.engine = create_engine(url)
                self.connection = self.engine.connect()
            if self.engine.driver in ["psycopg2", "pg8000"]:
                return PSQLSecateur(url, engine, connection, already_exist, debug_mode, verbose, log)
            elif self.engine.driver in ["mysqldb", "pymysql"]:
                pass
            elif self.engine.driver in ["cx_oracle"]:
                pass
            elif self.engine.driver in ["pyodbc", "pymssql"]:
                pass
            elif self.engine.driver in ["pysqlite"]:
                pass
            else:
                raise ValueError(
                    "Unsupported driver! Please create an issue on https://github.com/darentydarenty/secateur"
                )
        except Exception as Error:
            raise ValueError(
                "Failed to connect to the database. Please try again."
            )
        finally:
            self.connection.close()
            self.engine.dispose()
