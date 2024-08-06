from dataclasses import dataclass
import sqlite3 
import array
import csv


@dataclass
class DBMeta:
    table_name: str
    csv_name: str
    columns: list[str]


class Import_data:
    def create_table(self):
        self.cursor.execute(f'''
            create table if not exists {self.table_name} ({','.join(str(x) for x in self.columns)})
                   ''')
        
    def insert_data(self):
        with open('doc/'+self.csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_file,None)

            for row in csv_reader:
                    self.cursor.execute(f'INSERT INTO {self.table_name} ({','.join(str(x) for x in self.columns)}) VALUES ({','.join('?' for _ in range(len(self.columns)))})', row)

            self.conn.commit()    


    def __init__(self,dbmeta) -> None:
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.table_name = dbmeta.table_name
        self.csv_name = dbmeta.csv_name
        self.columns = dbmeta.columns

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close_connection()

if __name__ == "__main__":
    dbmeta = DBMeta('test_import','nulls.csv',["col1","col2"])
    import_data = Import_data(dbmeta)
    import_data.create_table()
    import_data.insert_data()