# Persona Analysis with Python

The initial project of the Miuul Data Science Bootcamp. This project performs a comprehensive analysis on customer data from a `persona.csv` dataset, showcasing how to segment customers based on various attributes like `COUNTRY`, `SOURCE`, `SEX`, and `AGE`. The project utilizes the `pandas` library for data manipulation and analysis.

## Project Overview

The goal of this analysis is to understand customer behavior and revenue by applying various grouping, aggregating, and segmentation techniques. This helps in identifying different customer personas and predicting potential revenue based on their characteristics.

## Dataset

The dataset used in this project is `persona.csv`, which contains the following key columns:
- `COUNTRY`: Country from which the sale was made.
- `SOURCE`: The platform (e.g., iOS, Android) used for the sale.
- `SEX`: Gender of the customer.
- `AGE`: Age of the customer.
- `PRICE`: The revenue generated from the sale.

## Key Analysis Steps

1. **Reading and Inspecting the Data**: The dataset is read into a pandas DataFrame, and general information about the data is displayed.
2. **Basic Exploration**: Unique values, frequency counts, and aggregations are calculated for key variables such as `SOURCE`, `PRICE`, and `COUNTRY`.
3. **Grouping and Aggregating**: Data is grouped by various combinations like `COUNTRY`, `SOURCE`, `SEX`, and `AGE` to calculate the average revenue.
4. **Sorting**: The results are sorted by `PRICE` to identify the most valuable segments.
5. **Converting Age to Categorical**: The `AGE` variable is converted into categorical groups to simplify further analysis.
6. **Defining Personas**: New level-based customer personas are created by combining different attributes into a single identifier (e.g., `TUR_ANDROID_FEMALE_31_40`).
7. **Segmentation**: Customers are segmented into four groups ("D", "C", "B", "A") based on their average `PRICE` using the `pd.qcut()` function.
8. **Prediction**: Potential revenue is predicted for new customers based on their segment.
