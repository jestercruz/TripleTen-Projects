# Megaline Mobile Plan Recommendation System

## Project Overview

This project develops a machine learning model for Megaline, a mobile carrier, to recommend the most suitable mobile plans ("Smart" or "Ultra") to its subscribers based on their usage behavior. Utilizing subscriber behavior data, such as call numbers, total call duration, text message counts, and internet usage, the model aims to predict the optimal plan for each user. The goal is to achieve a model accuracy of at least 0.75 on the test dataset.

## Data Description

The dataset comprises monthly user behavior information, including:

- `calls`: Number of calls made by the user.
- `minutes`: Total call duration in minutes.
- `messages`: Number of text messages sent.
- `mb_used`: Internet traffic used in MB.
- `is_ultra`: Indicator of the user's plan for the current month (1 for Ultra, 0 for Smart).

## Methodology

### Data Splitting

- The dataset was split into training (60%), validation (20%), and test (20%) sets to evaluate model performance accurately.

### Model Selection and Hyperparameter Tuning

- **Decision Tree**, **Random Forest**, and **Logistic Regression** models were trained and tuned to identify the model with the best performance.
- Hyperparameters were adjusted through a series of experiments to optimize each model's accuracy.

### Model Evaluation

- The Random Forest model demonstrated the highest accuracy on the validation set and was selected for the final evaluation.
- Model performance was assessed using the test dataset to ensure the accuracy met the project's threshold.

### Sanity Check

- Conducted a sanity check by comparing the model's performance against a random model and analyzing the confusion matrix and feature importance.
- These steps confirmed that the model was making predictions based on the data and not by chance.

## Key Findings

- The **Random Forest model** achieved the best performance, surpassing the accuracy threshold set for the project.
- **Feature importance analysis** indicated that internet usage (mb_used) and call duration (minutes) were significant predictors of plan preference.
- The model’s performance was robust across both the validation and test sets, confirming its effectiveness in predicting user plan preference based on behavior.

## Conclusion

The machine learning pipeline developed in this project enables Megaline to analyze subscriber behavior accurately and recommend the most suitable mobile plans. By leveraging user data, the model can facilitate more personalized and effective marketing strategies, encouraging users to switch to newer plans that align with their usage patterns. Future work may explore more complex models, feature engineering techniques, and cross-validation to further enhance model accuracy and reliability.

For additional inquiries or contributions, please refer to the contact details provided within this repository.
