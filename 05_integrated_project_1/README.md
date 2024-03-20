# Video Game Sales Data Analysis

## Project Overview

This project is an analysis for the online store Ice, focusing on the video game industry. Utilizing user and expert reviews, genres, platforms (e.g., Xbox, PlayStation), and historical sales data, we aim to uncover patterns that indicate a game's success. This analysis will guide the planning of advertising campaigns by identifying potential big winners in the market.

### Objectives

- Analyze game sales data to identify trends that determine game success.
- Explore the impact of user and critic reviews on game sales.
- Examine how ESRB ratings influence game sales in different regions.
- Predict market behavior for 2017 based on data up to 2016.

## Data Description

The dataset, derived from open sources, includes the following information:

- Game title, platform, genre, and year of release.
- Sales data across North America, Europe, Japan, and other regions.
- Critic scores (out of 100) and user scores (out of 10).
- ESRB ratings (e.g., Teen, Mature).

## Methodology

### Data Preparation

1. Standardized column names to lowercase.
2. Converted data types for analysis efficiency and accuracy.
3. Addressed missing values thoughtfully, considering the context and possible implications.
4. Calculated total sales for each game across all regions.

### Data Analysis

- Conducted a yearly analysis of game releases and sales trends.
- Identified platforms with the highest total sales and analyzed their lifespan and market evolution.
- Analyzed sales performance by platform, genre, and ESRB rating.
- Examined the correlation between reviews and sales.
- Created user profiles for each region to understand market preferences.

### Hypothesis Testing

1. **Xbox One vs. PC User Ratings**: Tested if average user ratings are the same across these platforms.
2. **Action vs. Sports Genres**: Compared average user ratings to see if they significantly differ between these genres.

## Key Findings

- Transition periods between console generations significantly impact sales patterns.
- No strong correlation between user or critic scores and sales, suggesting that other factors play a larger role in a game's commercial success.
- Genre and platform preferences vary by region, influencing sales strategies.
- The ESRB rating has a varied impact on sales in different regions, with mature-rated games performing particularly well in North America and Europe.

## Conclusions

The analysis reveals the complexity of the video game market, highlighting the importance of regional preferences and platform life cycles. For the upcoming year, focusing on emerging platforms like the PS4 and Xbox One in North America and Europe, and the continued dominance of handheld consoles in Japan, could be key strategies. Action and Shooter genres, along with titles rated Mature, are likely to perform well in Western markets, while Japan shows a strong preference for Role-Playing games.

## Future Directions

- Further analysis could refine predictions by incorporating more nuanced data on social media trends and marketing campaigns.
- Longitudinal studies on the impact of digital distribution on game sales could offer additional insights.

## Usage

This project is structured in a Jupyter Notebook, making it easy to follow the analysis process step-by-step. Users interested in replicating the study or applying the methodology to new data sets will find detailed instructions and code comments to guide them through the process.

For any inquiries or contributions, please refer to the contact details provided in this repository.
