# Beta Bank Customer Retention Model

## Overview

Beta Bank has been facing a steady decline in customer retention. The project's goal is to develop a predictive model to identify customers likely to churn. By leveraging customer behavior and demographic data, the model aims to predict churn before it happens, enabling the bank to implement retention strategies effectively.

## Dataset Description

The dataset comprises details of the bank's customers, along with a target variable indicating whether the customer has exited (churned). Features include:

- Customer ID, credit score, geography, gender, age.
- Tenure, account balance, number of products used.
- Credit card ownership, activity status, estimated salary.
- Target: Churn status (1 for churned, 0 for retained).

## Project Approach

### Data Preprocessing

- Loaded and examined the data for inconsistencies, missing values, and irrelevant features.
- Processed categorical variables and standardized numerical features.
- Dropped features not contributing to the model's predictive power, such as customer ID and surname.

### Exploratory Data Analysis (EDA)

- Analyzed the distribution of key features and their relationship with the churn status.
- Identified patterns and correlations that could influence model development.

### Handling Class Imbalance

- Evaluated the model's performance with the original imbalanced dataset.
- Implemented upsampling and downsampling techniques to balance the classes.
- Adjusted class weights in the model as an alternative approach to address imbalance.

### Model Development and Evaluation

- Trained Logistic Regression, Decision Tree, and Random Forest models.
- Fine-tuned hyperparameters and applied threshold adjustments to optimize the F1 score.
- Evaluated models based on F1 score and AUC-ROC metric, selecting the best-performing model for the final testing.

## Key Findings

- The initial model without addressing class imbalance showed a poor performance, highlighting the importance of dealing with imbalanced data.
- Among various approaches, the Random Forest model with threshold adjustment demonstrated superior performance, achieving an F1 score of 0.627 and an AUC-ROC of 0.865, surpassing the project requirement of an F1 score of at least 0.59.
- Class weight adjustment and threshold optimization were crucial in improving model performance.

## Conclusion

The predictive model developed for Beta Bank successfully identifies customers at high risk of churn. By implementing this model, Beta Bank can proactively engage with these customers through targeted retention strategies, potentially reversing the decision to leave. This project underscores the value of machine learning in customer retention efforts and sets a foundation for further research into personalized customer engagement strategies.

## Future Work

- Explore additional feature engineering techniques to uncover more predictive signals.
- Investigate the impact of external factors, such as economic conditions, on customer churn.
- Develop a more granular model that predicts the time frame within which a customer might churn.

For more information or contributions to this project, please refer to the contact details provided within this repository.
