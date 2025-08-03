# Sales Promotion Analysis

This project analyzes the impact of promotions on item and store-level sales using clustering, statistical testing, and visualization. It generates plots and a PowerPoint report summarizing the results.

## Features

- Loads and preprocesses sales and promotion data
- Flags sales records during promotion periods
- Clusters items and stores by average weekly sales
- Calculates sales increase due to promotions
- Visualizes results with bar and box plots
- Performs statistical tests (t-test) on sales increases
- Generates a PowerPoint presentation of findings

## Project Structure

- `analysis/visualizer.py`: Generates plots and statistical analyses for promotion effects.
- `parse_date.py`: Utility for robust date parsing.
- `data/assignment4.1a.csv`: Sales data (example path).
- `data/PromotionDates.csv`: Promotion periods (example path).
- `outputs/`: Directory for generated plot images.
- `Promotion_Analysis_Report.pptx`: Generated PowerPoint report.

## Setup

1. Clone the repository.
2. Install dependencies:
