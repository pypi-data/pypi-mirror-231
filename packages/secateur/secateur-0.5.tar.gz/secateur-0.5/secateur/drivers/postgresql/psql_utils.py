from prettytable import PrettyTable
from ...connector import BaseConnector

class PSQLUtilities(BaseConnector):
    """
    Doc-string for Utilities class.
    """
    def db_size(self, database=None) -> str:
        """
        Doc-string for db_size() method.
        """
        return self.execute(
            f"SELECT pg_size_pretty(pg_database_size('{self.engine.url.database if database == None else database}'))"
        )[0][0]

    def schema_size(self, schema: str) -> str:
        """
        Doc-string for schema_size() method.
        """
        return self.execute(
f"""SELECT pg_size_pretty(sum(table_size)::bigint)
FROM (SELECT pg_catalog.pg_namespace.nspname           AS schema_name,
                pg_relation_size(pg_catalog.pg_class.oid) AS table_size
        FROM pg_catalog.pg_class
        JOIN pg_catalog.pg_namespace ON relnamespace = pg_catalog.pg_namespace.oid
        WHERE pg_catalog.pg_namespace.nspname = '{schema}') t
GROUP BY schema_name"""
            )[0][0]

    def table_size(self, table: str) -> str:
        """
        Doc-string for table_size() method.
        """
        return self.execute(f"SELECT pg_size_pretty(pg_total_relation_size('{table}'))")[0][0]

    def get_count(self, table: str, condition="") -> int:
        """
        Doc-string for get_count() method.
        """
        return self.execute(f"SELECT COUNT(*) FROM {table} {condition}")[0][0]

    def get_dtype(self, table: str, column: str) -> str:
        """
        Doc-string for get_dtype() method.
        """
        try:
            return self.execute(
f"""SELECT data_type FROM information_schema.columns
WHERE table_schema = '{table.split('.')[0]}'
AND table_name = '{table.split('.')[1]}'
AND column_name = '{column}'""")[0][0]
        except IndexError:
            raise ValueError("Format of the table entry: schema_name.table_name")

    def get_schema_tables(self, schema: str) -> list:
        """
        Doc-string for get_schema_tables() method.
        """
        return [
                item[0]
                for item in self.execute(
f"""SELECT table_schema || '.' || table_name FROM information_schema.tables
WHERE table_schema = '{schema}'"""
                )
            ]

    def get_table_columns(self, table: str) -> list:
        """
        Doc-string for get_table_columns() method.
        """
        try:
            return [
                    item[0]
                    for item in self.execute(
f"""SELECT column_name FROM information_schema.columns
WHERE table_schema = '{table.split('.')[0]}'
AND table_name = '{table.split('.')[1]}'""")
                ]
        except IndexError:
            raise ValueError("Format of the table entry: schema_name.table_name")

    def get_dependencies(self) -> list:
        """
        Doc-string for get_dependencies() method.
        """
        self.dependencies = self.execute(
f"""SELECT tc.constraint_type,
    tc.constraint_name,
    tc.table_schema,
    tc.table_name,
    kcu.column_name,
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name   AS foreign_table_name,
    ccu.column_name  AS foreign_column_name
FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
            ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type IN ('FOREIGN KEY', 'PRIMARY KEY')
AND tc.table_schema <> 'pg_catalog'
ORDER BY constraint_type DESC""")
        self.__dependencies = PrettyTable()
        self.__dependencies.field_names = ["constraint_type", "constraint_name", "table_schema", "table_name",
                                "column_name", "foreign_table_schema", "foreign_table_name", "foreign_column_name"]
        self.__dependencies.add_rows([list(item) for item in self.dependencies])
        return self.dependencies

    def show_dependencies(self) -> None:
        print(self.__dependencies)