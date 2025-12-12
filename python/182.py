import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup = person.groupby(['email']).count().reset_index()
    return pd.DataFrame(data=dup, columns=['email']).where(dup['id'] > 1).dropna().rename(columns={'email': 'Email'})
