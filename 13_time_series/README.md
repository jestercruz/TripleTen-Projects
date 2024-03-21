# Taxi Demand Forecasting for Sweet Lift Taxi Company

## Project Overview

Sweet Lift Taxi company, operating a robust fleet at airports, aims to optimize its services by predicting taxi demand. This project focuses on developing a predictive model to forecast the number of taxi orders for the next hour, enabling the company to manage its fleet more efficiently during peak hours.

## Data Description

The project utilizes historical data on taxi orders, including technical specifications and time stamps. Key features encompass technical specs, trim versions, prices, and the number of orders (`num_orders` column). The dataset's temporal nature demands precise time series forecasting techniques.

## Methodology

### Data Preparation

- The dataset was resampled to an hourly frequency to align with the forecasting objective.
- Preliminary data analysis included identifying patterns, trends, and seasonality in taxi demand.

### Feature Engineering

- Developed features capturing temporal dynamics, such as time of day and lag features, to encapsulate past order information.
- Analyzed feature importance to identify the most predictive variables for taxi order volumes.

### Model Development and Evaluation

- Trained various models, including **Random Forest, Linear Regression, and gradient boosting models (CatBoost)**, adjusting hyperparameters for optimal performance.
- Employed the RMSE metric to evaluate model predictions, with a goal of achieving an RMSE of less than 48 on the test set.
- Assessed models based on prediction quality, speed, and training time to find the best fit for operational needs.

## Results

Our evaluation highlighted the effectiveness of different models in forecasting taxi demand:

- **CatBoost** emerged as the top performer, offering the highest prediction accuracy with an RMSE significantly below the target threshold. Its ability to handle categorical and temporal features effectively contributed to its superior performance.
- **Random Forest** also showed commendable results, balancing accuracy with relatively swift prediction and training times.
- **Linear Regression** served as a valuable baseline, ensuring that more complex models provided a meaningful improvement over simpler approaches.

Key insights from feature importance analysis included the critical role of temporal features, especially the 24-hour lag, indicating a daily cycle in taxi demand.

## Conclusion

The project successfully developed a predictive model capable of forecasting taxi demand for the Sweet Lift Taxi company, with the CatBoost model standing out for its predictive accuracy. This model will enable Sweet Lift Taxi to deploy its fleet more strategically during peak demand hours, enhancing service availability and customer satisfaction.

## Future Work

- Further exploration of hyperparameter tuning and model ensembling could enhance prediction accuracy.
- Implementing real-time data streams into the forecasting model could provide more dynamic and responsive demand predictions.
- Investigating additional external factors (e.g., weather conditions, events) that could impact taxi demand may refine forecasting models further.

For inquiries or contributions, please refer to the contact details within this repository.
