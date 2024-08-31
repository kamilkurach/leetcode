#2879. Display the First Three Rows
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    
    #2 less pandas way but also works
    #return employees[:3]
