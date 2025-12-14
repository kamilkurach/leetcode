import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema.where((cinema["id"] % 2 != 0) & (cinema["description"] != "boring")).dropna().sort_values(by="rating", ascending=False)
