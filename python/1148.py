import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.where(views['author_id'] == views['viewer_id']).rename(columns={'viewer_id': 'id'}).dropna().filter(items=['id']).drop_duplicates().sort_values(by='id')
