import pandas as pd
from utils.helpers import parse_date


def load_data(sales_path, promo_path):
    sales_df = pd.read_csv(sales_path)
    promo_df = pd.read_csv(promo_path)
    sales_df['Date'] = pd.to_datetime(sales_df['Date'])
    promo_df['StartDate'] = promo_df['StartDate'].apply(parse_date)
    promo_df['EndDate'] = promo_df['EndDate'].apply(parse_date)
    return sales_df, promo_df


def correct_date_format(promo_df):
    if 'Promo5' in promo_df['Period'].values:
        idx = promo_df[promo_df['Period'] == 'Promo5'].index[0]
        for col in ['StartDate', 'EndDate']:
            promo_df.at[idx, col] = promo_df.at[idx, col].strftime('%d/%m/%Y')
    return promo_df
