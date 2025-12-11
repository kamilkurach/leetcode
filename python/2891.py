import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals.where(animals['weight'] > 100).sort_values(by='weight', ascending=False).dropna()
    return pd.DataFrame(data=df['name'])
