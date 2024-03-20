# Taxi Rides in Chicago: Data Analysis Project

## Overview

This project analyzes taxi ride data in Chicago, exploring company competitiveness, ride distributions across neighborhoods, and the impact of weather conditions on ride durations. By investigating data from November 2017, this analysis aims to uncover patterns that can guide strategic decisions for a new entrant in the market, Zuber.

## Datasets

The analysis utilizes three CSV files obtained through SQL queries, covering:

- **Taxi Companies and Ride Counts**: Information on the number of rides per taxi company during November 15-16, 2017.
- **Neighborhood Drop-offs**: Average number of rides ending in Chicago neighborhoods in November 2017.
- **Ride Durations to O'Hare Airport**: Specifics on rides from the Loop to O'Hare International Airport, including weather conditions and duration.

## Objectives

- Determine the most popular taxi companies based on ride counts.
- Identify top neighborhoods for taxi drop-offs.
- Analyze the effect of weather on ride durations from the Loop to O'Hare International Airport.

## Methodology

### Data Retrieval and Preparation

- Imported CSV files into Python using Pandas.
- Ensured data types were appropriate for analysis.
- Calculated total sales and conducted exploratory data analysis (EDA) to understand ride distributions.

### Exploratory Data Analysis (EDA)

- Analyzed ride counts for taxi companies and identified market leaders.
- Explored drop-off neighborhood popularity and discovered top destinations.
- Visualized data through bar charts and graphs for clearer insights.

### Hypothesis Testing

- Tested the hypothesis: "The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays."
- Chose an appropriate significance level and conducted a t-test to compare ride durations under different weather conditions.

## Key Findings

- **Taxi Companies**: Flash Cab dominates the market with significantly more rides compared to competitors.
- **Neighborhood Drop-offs**: The Loop is the prime destination for taxi rides, suggesting a high demand in downtown Chicago.
- **Weather Impact**: Weather conditions significantly affect ride durations to O'Hare Airport on Saturdays, particularly during rain.

## Conclusions

The analysis provides valuable insights into the taxi ride market in Chicago, highlighting Flash Cab's dominance, the significance of strategic neighborhood targeting, and the influence of weather on ride durations. These findings are crucial for Zuber's strategic planning as it considers entering the Chicago taxi market.

## Future Directions

- Further analysis could explore the impact of special events and holidays on taxi demand.
- Investigating customer satisfaction and service quality across companies may reveal additional competitive advantages.
- A deeper dive into the relationship between ride durations, distances, and fares could uncover pricing strategies.

For inquiries or contributions to the project, please refer to the contact details provided within this repository.
