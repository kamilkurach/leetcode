import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    data = courses.groupby(courses['class']).count().reset_index()
    return pd.DataFrame(data=data, columns=['class']).where(data['student'] >= 5).dropna()
