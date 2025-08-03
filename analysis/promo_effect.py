import pandas as pd
import numpy as np

def apply_promotion_flags(sales_df, promo_df, num_promos=4):
    sales_df['IsPromotion'] = 0
    for i in range(num_promos):
        start, end = promo_df.loc[i, 'StartDate'], promo_df.loc[i, 'EndDate']
        sales_df.loc[(sales_df['Date'] >= start) & (sales_df['Date'] <= end), 'IsPromotion'] = 1
    return sales_df

def calculate_promotion_effects(sales_df, item_info, store_info):
    df = sales_df.merge(item_info[['ProductCode', 'ItemCategory']], on='ProductCode')
    df = df.merge(store_info[['StoreCode', 'StoreCategory']], on='StoreCode')
    grouped = df.groupby(['ProductCode', 'StoreCode', 'ItemCategory', 'StoreCategory', 'IsPromotion'])['SalesQuantity'].mean().reset_index()
    grouped.rename(columns={'SalesQuantity': 'AvgDailySale'}, inplace=True)

    pivot = grouped.pivot_table(index=['ProductCode', 'StoreCode', 'ItemCategory', 'StoreCategory'],
                                 columns='IsPromotion', values='AvgDailySale').reset_index()
    pivot.columns = ['ProductCode', 'StoreCode', 'ItemCategory', 'StoreCategory', 'AvgDailySale_NonPromo', 'AvgDailySale_Promo']
    pivot['SalesIncrease'] = pivot['AvgDailySale_Promo'] - pivot['AvgDailySale_NonPromo']
    pivot['SalesIncrease_Percentage'] = (pivot['SalesIncrease'] / pivot['AvgDailySale_NonPromo']) * 100
    pivot.replace([np.inf, -np.inf], 0, inplace=True)
    pivot.fillna(0, inplace=True)
    return pivot
