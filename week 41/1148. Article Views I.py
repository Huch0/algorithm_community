import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = (
        views[views['viewer_id'] == views['author_id']]
        .drop_duplicates(subset=['author_id'])
        .rename(columns={'author_id': 'id'})
        .sort_values(by='id')
        .reset_index(drop=True)
    )
    return df[['id']]