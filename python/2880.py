import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.where(students['student_id'] == 101).filter(items=['name', 'age']).dropna()
