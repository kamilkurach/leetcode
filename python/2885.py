#2885. Rename Columns
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students.values,
    columns=(
        'student_id',
        'first_name',
        'last_name',
        'age_in_years'))

#2 according to leetcode scoring solution #2 is slower
'''
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={
        'id':'student_id',
        'first':'first_name',
        'last':'last_name',
        'age':'age_in_years'})
'''
