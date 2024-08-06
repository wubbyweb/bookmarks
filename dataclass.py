from dataclasses import dataclass
import numpy as np

@dataclass
class sqlite():
    sqlite_tablename: str
    csv_filename: str
    columns: list[str]


sq=sqlite('tblnme','flenme',['test1','test2'])

print(sq.columns)

