# Statistical Data Analysis: Megaline Plans Comparison

## Project Overview

As an analyst at Megaline, a telecom operator, this project aims to identify which of two prepaid plans, Surf and Ultimate, generates more revenue. Using a dataset of 500 clients, this analysis delves into customer usage patterns throughout 2018 to understand behaviors and determine the more profitable plan.

The task involves data preprocessing, exploratory data analysis (EDA), statistical hypothesis testing, and a comprehensive conclusion to inform the commercial department's advertising budget decisions.

## Data Description

The project dataset comprises information on calls, internet usage, messages, user demographics, and plan details:

- `megaline_calls.csv`: Data on calls made by users.
- `megaline_internet.csv`: Web session data for users.
- `megaline_messages.csv`: Information on messages sent by users.
- `megaline_plans.csv`: Details on the Surf and Ultimate plans.
- `megaline_users.csv`: User demographics and plan subscriptions.

## System Requirements

This analysis is performed using Python, specifically with the Pandas library for data manipulation and Matplotlib for visualization. A Jupyter Notebook environment is recommended for running the analysis. Ensure the following are installed:

- Python 3.8+
- Pandas
- Matplotlib
- SciPy (for hypothesis testing)

## Deployment Instructions

1. Ensure that Python and Jupyter Notebook are installed on your machine.
2. Clone this repository to obtain the dataset and Jupyter Notebook.
3. Install required Python packages using `pip install pandas matplotlib scipy`.
4. Open the Jupyter Notebook (`SDA_Project_Megaline_Analysis.ipynb`) and run all cells to reproduce the analysis.

## Key Findings

- **Revenue Comparison**: The Ultimate plan is more profitable than the Surf plan. This is a crucial insight for resource allocation in advertising.
- **Regional Revenue Difference**: There's a statistically significant difference in average revenue between users in the NY-NJ area and other regions, indicating potential for targeted marketing strategies.

## Statistical Analysis

The project includes two hypothesis tests:

1. **Plan Revenue Difference**: Testing whether the average revenue from the Ultimate and Surf plans differs, we found significant evidence to suggest that the Ultimate plan generates higher revenue.
2. **Regional Revenue Difference**: Analyzing if the average revenue from users in the NY-NJ area differs from users in other regions, results indicated a significant difference, suggesting regional revenue variability.

## Conclusion

This detailed analysis provides Megaline with insights into which prepaid plan generates more revenue and highlights the importance of regional differences in user spending. These findings will assist in making informed decisions on marketing and resource allocation to maximize profitability.

## Future Work

- Further segmentation analysis could unveil more specific user behaviors.
- Machine learning models might predict customer plan preference or spending based on usage and demographics.
- A deeper regional analysis could identify other high-potential markets for targeted advertising campaigns.

For any inquiries or contributions to the project, please refer to the contact details provided in this repository.
