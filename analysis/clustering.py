from sklearn.cluster import KMeans
import pandas as pd


def cluster_items_stores(non_promo_sales):
    avg_sales = non_promo_sales.groupby(['ProductCode', 'StoreCode'])['SalesQuantity'].mean().reset_index()
    avg_sales['AvgWeeklySale'] = avg_sales['SalesQuantity'] * 7

    item_avg = avg_sales.groupby('ProductCode')['AvgWeeklySale'].mean().reset_index()
    item_avg.columns = ['ProductCode', 'AvgWeeklySalePerStore']
    item_avg['ItemCluster'] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(
        item_avg[['AvgWeeklySalePerStore']])
    item_avg = map_cluster_to_category(item_avg, 'ItemCluster', 'AvgWeeklySalePerStore', 'ItemCategory')

    store_avg = avg_sales.groupby('StoreCode')['AvgWeeklySale'].mean().reset_index()
    store_avg.columns = ['StoreCode', 'AvgWeeklySalePerItem']
    store_avg['StoreCluster'] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(
        store_avg[['AvgWeeklySalePerItem']])
    store_avg = map_cluster_to_category(store_avg, 'StoreCluster', 'AvgWeeklySalePerItem', 'StoreCategory')

    return item_avg, store_avg


def map_cluster_to_category(df, cluster_col, value_col, new_col):
    cluster_map = df.groupby(cluster_col)[value_col].mean().sort_values().index.tolist()
    mapping = {v: k for k, v in enumerate(cluster_map)}
    df[new_col] = df[cluster_col].map(mapping).map({0: 'Slow', 1: 'Medium', 2: 'Fast'})
    return df
