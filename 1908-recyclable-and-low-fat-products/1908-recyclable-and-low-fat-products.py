import pandas as pd

def find_products(p: pd.DataFrame) -> pd.DataFrame:
    r = p[(p['low_fats']=='Y') & (p['recyclable']=='Y')]
    return r[['product_id']]