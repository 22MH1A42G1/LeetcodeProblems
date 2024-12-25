import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    a = views[views['author_id'] == views['viewer_id']]
    u = a['author_id'].unique()
    u = sorted(u)
    return pd.DataFrame({'id': u})