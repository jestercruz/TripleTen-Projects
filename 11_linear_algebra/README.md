# Sure Tomorrow Insurance Customer Analysis & Data Protection

## Project Overview

This project encompasses a comprehensive approach to address several machine learning tasks for the Sure Tomorrow Insurance Company. The objective is to utilize machine learning to find similar customers, predict the likelihood and quantity of insurance benefits, and implement a data protection mechanism that safeguards client data without diminishing the model's performance.

## Data Description

The dataset consists of anonymized client information, including:

- Gender, age, salary, and family members count as features.
- Number of insurance benefits received in the past five years as the target.

The project tasks are segregated as follows:

1. **Customer Similarity Search**: Identifying customers similar to a given reference using the k-nearest neighbors (kNN) algorithm.
2. **Benefit Prediction**: Developing a model to predict the likelihood of a new customer receiving an insurance benefit.
3. **Benefit Quantity Prediction**: Employing linear regression to estimate the number of insurance benefits a new customer might receive.
4. **Data Protection**: Designing and validating a data transformation algorithm that obfuscates client data to prevent personal information recovery while retaining the model's efficacy.

## Methodology

### Data Preparation

- Initial data exploration included assessing data integrity, identifying missing values, and understanding feature distributions.
- Feature scaling was applied to normalize the data, enhancing the kNN algorithm's performance for customer similarity search.

### Model Development

- **Task 2 & 3**: Linear regression models were trained to predict both the likelihood and the quantity of insurance benefits. Model performance was benchmarked against a dummy model to establish its efficacy.
- **Task 4**: A data transformation algorithm based on matrix multiplication was devised for data obfuscation. The algorithm's impact on linear regression predictions was analytically and empirically evaluated to ensure model performance remained unchanged.

## Key Findings

- **Customer Similarity**: The application of the kNN algorithm with properly scaled features effectively identified customers similar to a given reference, aiding targeted marketing strategies.
- **Benefit Prediction**: The predictive models surpassed the performance of the dummy model, demonstrating the feasibility of using machine learning for benefit prediction.
- **Data Protection**: The developed data obfuscation method successfully protected client information without degrading the predictive accuracy of the machine learning models. The approach was validated through both theoretical proof and practical experimentation, showing no significant difference in model performance before and after data transformation.

## Conclusion

The project successfully demonstrated the application of machine learning techniques to enhance the Sure Tomorrow Insurance Company's operational efficiency. By leveraging customer data, we developed models that not only predict customer behavior but also ensure data privacy through innovative obfuscation techniques. These achievements highlight the potential of machine learning in refining insurance processes, improving customer targeting, and ensuring data security.

The linear regression models' robustness, even post-data transformation, underscores the viability of protecting sensitive information without compromising on analytical insights. This balance between data privacy and utility is crucial for maintaining client trust and compliance with data protection regulations.

## Future Work

- Exploration of more sophisticated algorithms for customer similarity and benefit prediction could yield further improvements in model accuracy and insights.
- Enhancing the data protection algorithm to support a broader range of machine learning models, including those with non-linear decision boundaries.
- Investigating the impact of additional data features and external factors on insurance benefit predictions to refine model predictions further.

For more information or contributions, please refer to the contact details provided within this repository.
