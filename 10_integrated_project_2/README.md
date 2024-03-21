# Zyfra Gold Mining Project

## Project Overview

This project aims to assist the Zyfra Gold Mining company in maximizing gold recovery through predictive modeling. By analyzing data from various stages of the gold flotation process, we develop models to predict the efficiency of gold recovery, enabling the identification of optimal processing parameters.

## Data Description

The dataset comprises parameters measured at different stages of the gold recovery process, including:

- **gold_recovery_train.csv, gold_recovery_test.csv, gold_recovery_full.csv**: These files contain the raw data, including features like the quality of the feed, concentration of gold (Au), silver (Ag), and lead (Pb) at different purification stages, and the volume of reserves in each oil well.

## Methodology

### Data Preparation

- The datasets were loaded and inspected for data types, missing values, and the presence of irrelevant features.
- Recovery calculation was verified against provided values to ensure data integrity.
- Features not present in the test set were analyzed and understood for their impact on model training.

### Exploratory Data Analysis (EDA)

- Metal concentration changes across purification stages were visualized, highlighting the efficiency of gold enrichment.
- Feed particle size distributions across training and test sets were compared to ensure model validity.
- Total concentrations of substances at different stages were examined for anomalies, which were then addressed to improve model reliability.

### Model Building

- A Linear Regression model was selected in compliance with project requirements.
- The data was split into training, validation, and test sets following a 75:25 ratio.
- Models were trained for each region, and predictions were made for the validation set to assess model performance.
- A custom function was developed to calculate the final sMAPE value, optimizing model selection based on this metric.

## Key Findings

- **Model Performance**: Linear Regression models demonstrated an ability to predict gold recovery rates accurately, with validation through both MAE and sMAPE metrics.
- **Metal Concentration**: The concentration of gold increased significantly at each purification stage, validating the process's efficiency. In contrast, silver and lead showed varying trends, indicating their selective removal.
- **Anomaly Detection**: The analysis of total substance concentrations revealed outliers, particularly in the final concentrate stages, which were addressed to improve model accuracy.
- **Optimal Region Selection**: Based on profit calculations and risk analysis using bootstrapping, an optimal region for new well development was recommended, balancing potential profit and operational risks.

## Conclusion

The predictive models developed in this project provide Zyfra and the OilyGiant mining company with valuable insights into optimizing gold recovery processes. By accurately estimating gold recovery rates and analyzing purification efficiency, the models enable informed decision-making for operational adjustments and new well development. The project underscores the importance of data-driven approaches in enhancing resource recovery, operational efficiency, and profitability in the mining industry.

## Future Directions

- **Advanced Modeling**: Exploring more complex models or ensemble methods could yield improvements in prediction accuracy.
- **Operational Data Integration**: Incorporating additional operational parameters could enhance model insights, offering more nuanced optimization strategies.
- **Real-Time Analytics**: Developing a framework for real-time data analysis and prediction could provide dynamic process adjustments, further maximizing recovery rates and operational efficiency.

For further information or contributions, please refer to the contact details provided within this repository.
