import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(employees, salaries, how='outer', on='employee_id')
    return data.where(data['name'].isnull() | data['salary'].isnull()).filter(items=['employee_id']).dropna()
