import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from pptx.util import Inches

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_plot(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
    return path

def analyze_promotion_effects(promo_effect):
    slide_images = []

    def add_bar_plot(data, x, y, title, fname, palette):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x=data[x], y=data[y], palette=palette, ax=ax)
        ax.set_title(title)
        return save_plot(fig, fname)

    def add_box_plot(df, x, y, title, fname, palette):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x=x, y=y, palette=palette, ax=ax)
        ax.set_title(title)
        return save_plot(fig, fname)

    cat_sales = promo_effect.groupby('ItemCategory')['SalesIncrease'].mean().reset_index()
    slide_images.append(("Item Category Impact", add_bar_plot(cat_sales, 'ItemCategory', 'SalesIncrease', 'Item Category', 'item_cat.png', 'Blues')))

    top_items = promo_effect.sort_values(by='SalesIncrease', ascending=False).head(10)
    slide_images.append(("Top 10 Items", add_bar_plot(top_items, 'ProductCode', 'SalesIncrease', 'Top Items', 'top_items.png', 'Greens')))

    cat_stores = promo_effect.groupby('StoreCategory')['SalesIncrease'].mean().reset_index()
    slide_images.append(("Store Category Impact", add_bar_plot(cat_stores, 'StoreCategory', 'SalesIncrease', 'Store Category', 'store_cat.png', 'Oranges')))

    top_stores = promo_effect.groupby('StoreCode')['SalesIncrease'].mean().sort_values(ascending=False).head(10).reset_index()
    slide_images.append(("Top 10 Stores", add_bar_plot(top_stores, 'StoreCode', 'SalesIncrease', 'Top Stores', 'top_stores.png', 'Purples')))

    # Statistical test plots
    for category, label in [('ItemCategory', 'Items'), ('StoreCategory', 'Stores')]:
        fast = promo_effect[promo_effect[category] == 'Fast']['SalesIncrease']
        slow = promo_effect[promo_effect[category] == 'Slow']['SalesIncrease']
        if not fast.empty and not slow.empty:
            t_stat, p_val = ttest_ind(fast, slow, nan_policy='omit')
            print(f"{label} Fast vs Slow: T-stat={t_stat:.3f}, P={p_val:.3f}")
            subset = promo_effect[promo_effect[category].isin(['Fast', 'Slow'])]
            slide_images.append((f"Fast vs Slow {label}", add_box_plot(subset, category, 'SalesIncrease', f"Fast vs Slow {label}", f"{label.lower()}_box.png", 'Set2')))

    return slide_images
