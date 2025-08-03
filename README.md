# 📊 Sales Promotion Analysis

This project evaluates the impact of promotional events on product and store-level sales using clustering, statistical testing, and visual reporting. The workflow includes preprocessing, analysis, visualization, and generation of a comprehensive PowerPoint report.

---

## ✨ Features

- ✅ Load and preprocess sales and promotion datasets
- 📅 Identify and flag promotion periods
- 📊 Cluster items and stores using K-Means based on sales performance
- 📈 Measure sales uplift during promotions
- 📉 Generate bar charts and boxplots for deeper insights
- 📐 Perform statistical t-tests to compare category-wise effects
- 🖼️ Automatically generate a PowerPoint report with visuals and analysis

---

## 📁 Project Structure

```bash
sales_promotion_analysis/
├── data/                  # Input CSV files
├── outputs/               # Generated plots and PPT report
├── analysis/              # Core logic for analysis
│   ├── data_loader.py         # Load & preprocess sales and promo data
│   ├── clustering.py          # Cluster items and stores
│   ├── promo_effect.py        # Compute promo impact
│   ├── visualizer.py          # Plot and summarize results
│   └── presentation.py        # Generate PowerPoint slides
├── utils/
│   └── helpers.py             # Utility functions (e.g., date parsing)
├── main.py                    # Entry point for analysis
└── requirements.txt           # Required Python packages

```

- `analysis/data_loader.py`: load the data.
- `analysis/clustering.py`: Perform the clustering.
- `analysis/promo_effect.py`: Compute promo impact.
- `analysis/visualizer.py`: Generates plots and statistical analyses for promotion effects.
- `utils/helpers.py`: Utility for robust date parsing.
- `data/assignment4.1a.csv`: Sales data (example path).
- `data/PromotionDates.csv`: Promotion periods (example path).
- `outputs/`: Directory for generated plot images.
- `Promotion_Analysis_Report.pptx`: Generated PowerPoint report.

## Setup

1. Clone the repository.
2. Install dependencies: using requirement.txt
      pip install -r requirements.txt
4. unzip the data.zip folder.
5. run the main.py file on command promot using 'python main.py'
     python main.py

📤 Output

    Plots saved in the outputs/ directory
