# Churn Prediction Model for "Good Seed" Supermarket Chain

## Project Overview
This project aimed to develop a machine learning model to predict customer churn for the "Good Seed" supermarket chain. By leveraging customer data, the model identifies customers likely to churn, enabling targeted customer retention strategies.

## Objectives
- To develop a predictive model that identifies customers at high risk of churn.
- To evaluate the model based on accuracy, precision, recall, F1 score, and ROC-AUC score.

## Methodology
The project followed a comprehensive approach, starting from data preprocessing, through exploratory data analysis (EDA), to model training, evaluation, and selection. Key steps included:

1. **Data Preprocessing**: Involved cleaning data, handling missing values, and engineering features relevant to predicting churn.
2. **Exploratory Data Analysis (EDA)**: Provided insights into the dataset's characteristics and informed the feature selection process.
3. **Model Development and Evaluation**: Multiple models were considered, including logistic regression, random forest, and gradient boosting models like LightGBM, XGBoost, and CatBoost. The models were evaluated using metrics such as ROC-AUC.

## Key Findings
- The **CatBoost** model achieved the highest ROC-AUC score of **0.862934**, indicating its effectiveness in predicting customer churn.
- Models were compared based on their performance metrics, with a focus on achieving a balance between recall and precision.
- Feature importance analysis revealed insights into factors contributing to customer churn, aiding in understanding customer behavior and informing retention strategies.

## Final Model
The final model selected was **CatBoost**, with hyperparameters `{'classifier__depth': 6, 'classifier__iterations': 500, 'classifier__learning_rate': 0.01}`. This model not only achieved the highest ROC-AUC score but also provided a balanced performance across other evaluation metrics.

## Conclusion
The project successfully demonstrated the potential of machine learning models in predicting customer churn. The CatBoost model, in particular, showed promising results and can serve as a valuable tool for the "Good Seed" supermarket chain in formulating effective customer retention strategies.

## Acknowledgments
Special thanks to the team leader, project reviewer, and the Student Guidance Team for their support throughout the project. This project benefitted greatly from their insights and expertise.