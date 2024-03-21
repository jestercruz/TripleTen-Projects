# OilyGiant New Well Location Analysis

## Overview

This project's objective is to aid the OilyGiant mining company in identifying the optimal location for a new oil well, leveraging machine learning to predict reserve volumes across three distinct regions. The ultimate goal is to maximize profit while minimizing financial risk.

## Dataset Overview

The project utilizes geological exploration data from three regions, encompassing the following features:

- `id`: Unique oil well identifier.
- `f0`, `f1`, `f2`: Three significant features of points (details unspecified but crucial for prediction).
- `product`: Volume of reserves in the oil well (thousand barrels).

## Methodology

### Data Preparation

- The datasets for the three regions (`geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`) were loaded and prepared for analysis.
- Preprocessing steps included data cleaning, feature selection, and splitting the datasets into training and validation sets.

### Model Training and Evaluation

- A Linear Regression model was trained for each region, following a 75:25 split for training and validation sets.
- Model performance was evaluated using RMSE and the average volume of predicted reserves.
- Predictions and accuracy metrics were analyzed to gauge model reliability.

### Profit Calculation and Risk Analysis

- Key financial metrics were defined, including the budget for development, revenue per barrel, and the break-even volume of reserves.
- A profit calculation function was developed to estimate the potential financial gain from the top 200 wells based on model predictions.
- The Bootstrapping technique was employed to assess profit distribution, calculate average profits, identify the 95% confidence interval, and evaluate the risk of loss for each region.

## Key Findings

- **Region 1** emerged as the most favorable location for a new well due to its lowest risk of loss (1%), despite not having the highest average volume of predicted reserves.
- **Region 0** and **Region 2** demonstrated higher potential profits but were disqualified due to exceeding the acceptable risk of loss threshold of 2.5%.
- The analysis underscores the importance of not only considering potential reserves and profit but also evaluating the financial risks associated with exploration and development.

## Conclusion

The comprehensive analysis conducted in this project provides OilyGiant with a data-driven strategy for selecting a new oil well location. By prioritizing regions based on a balanced assessment of profit potential and risk management, OilyGiant can make informed decisions to enhance its operational efficiency and financial stability. Region 1, with its acceptable risk profile and reasonable profit potential, stands out as the recommended choice for development.

## Future Directions

- Further exploration of alternative machine learning models could provide insights into improving prediction accuracy.
- Incorporating additional data, such as geological and economic factors, may enhance the model's predictive power and financial analysis.
- Developing dynamic models that adapt to changing market conditions could offer OilyGiant a competitive advantage in future explorations.

For further information or to contribute to this project, please refer to the contact details provided within this repository.
