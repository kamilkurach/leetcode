import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    students = pd.DataFrame(data=student_data, columns=['student_id', 'age'])
    return students
