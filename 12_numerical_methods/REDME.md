# Rusty Bargain Used Car Price Prediction

## Overview

Rusty Bargain is innovating the used car market with a new app that provides instant car valuation for users looking to sell or understand the market value of their vehicles. This project aims to develop a robust predictive model that accurately determines a car's market value based on its specifications and historical data.

## Data Description

The dataset consists of historical data on used cars, including technical specifications, trim versions, and their sold prices. Key features include:

- Vehicle attributes like type, registration year, gearbox type, power, and brand.
- Mileage, registration month, fuel type, whether the car was repaired, and more.
- The target variable is the price at which the car was sold.

## Methodology

### Data Preparation

- Initial data exploration to understand the dataset structure, missing values, and data types.
- Preprocessing steps including handling of missing values, encoding categorical variables, and normalization of numerical features.

### Model Development

- Exploration of various machine learning models including **Random Forest, Decision Tree, Linear Regression, and gradient boosting models (LightGBM, CatBoost, and XGBoost)**.
- Hyperparameter tuning was performed for each model to optimize performance, focusing on balancing predictive accuracy with computational efficiency.

### Evaluation Criteria

- **Prediction Quality**: Assessed using the Root Mean Square Error (RMSE) metric to quantify the accuracy of predictions.
- **Prediction Speed**: Measured the time taken by the model to make predictions, prioritizing fast responses for app integration.
- **Training Time**: Evaluated the time required to train each model, considering the practical limitations of computational resources.

## Results

Our analysis yielded insightful findings on the trade-offs between model accuracy, prediction speed, and training time:

- **CatBoost** emerged as the leader in prediction accuracy with the lowest RMSE, proving its effectiveness for this specific use case.
- **LightGBM** showcased exceptional speed during both training and prediction phases, making it an attractive option for scenarios where computational efficiency is paramount.
- **Random Forest and Decision Tree** provided a good balance between speed and accuracy but were outperformed by gradient boosting methods in terms of prediction quality.
- **Linear Regression**, while not competitive in accuracy, served as an essential baseline for sanity checks and highlighted the advanced models' value.

## Conclusion

The project successfully developed a predictive model that Rusty Bargain can leverage to provide accurate and instant car valuations through their app. Gradient boosting models, particularly CatBoost and LightGBM, demonstrated superior performance, offering a promising solution to Rusty Bargain's need for accurate price predictions. The findings emphasize the importance of model selection based on specific business requirements, including prediction quality, speed, and training time.

## Future Directions

- Explore deeper hyperparameter tuning and model ensembling techniques to further enhance prediction accuracy.
- Investigate the deployment strategies for integrating the predictive model into the Rusty Bargain app, ensuring real-time performance.
- Conduct user feedback sessions to refine the app's user experience based on the model's predictions and accuracy.

This project stands as a testament to the potential of machine learning in transforming the used car market, offering users a reliable tool for car valuation and Rusty Bargain a competitive edge in the industry.

For further information or contributions, please refer to the contact details provided within this repository.
