from analysis.data_loader import load_data, correct_date_format
from analysis.promo_effect import apply_promotion_flags, calculate_promotion_effects
from analysis.clustering import cluster_items_stores
from analysis.visualizer import analyze_promotion_effects
from analysis.presentation import generate_presentation


def main():
    sales_df, promo_df = load_data("data/assignment4.1a.csv", "data/PromotionDates.csv")
    promo_df = correct_date_format(promo_df)

    max_date = promo_df[promo_df['Period'] == 'Promo4']['EndDate'].iloc[0]
    sales_df = sales_df[sales_df['Date'] <= max_date]
    sales_df = apply_promotion_flags(sales_df, promo_df, num_promos=4)

    non_promo_sales = sales_df[sales_df['IsPromotion'] == 0]
    item_info, store_info = cluster_items_stores(non_promo_sales)

    promo_effect = calculate_promotion_effects(sales_df, item_info, store_info)
    slide_images = analyze_promotion_effects(promo_effect)
    # generate_presentation(slide_images)


if __name__ == "__main__":
    main()
