#2885. Rename Columns
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students.values,
    columns=(
        'student_id',
        'first_name',
        'last_name',
        'age_in_years'))
