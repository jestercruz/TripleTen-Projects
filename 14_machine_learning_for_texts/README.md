# Sentiment Analysis of IMDB Movie Reviews

## Project Overview

The Film Junky Union, a community for classic movie enthusiasts, is innovating the way it categorizes movie reviews. This project aims to develop a machine learning model capable of automatically detecting negative movie reviews, utilizing a dataset of IMDB movie reviews labeled by sentiment. The target performance metric for this model is an F1 score of at least 0.85.

## Data Description

The project uses the `imdb_reviews.tsv` dataset, which consists of movie reviews from IMDB with polarity labeling. Each entry includes:
- `review`: The text of the movie review.
- `pos`: Binary sentiment label, '0' for negative and '1' for positive reviews.
- `ds_part`: Indicates whether the data point belongs to the training or test set.

The dataset, provided by Andrew L. Maas et al., is a benchmark in sentiment analysis, offering a nuanced set of texts for binary classification tasks.

## Methodology

### Data Preprocessing

- The data was loaded and cleaned, with preprocessing steps tailored to textual data. This involved tokenization, lowercasing, removing stop words, and lemmatization to standardize the review texts for model input.

### Exploratory Data Analysis (EDA)

- Conducted EDA to understand the distribution of sentiments and to observe any class imbalances that could impact model performance. The dataset was found to be well-balanced, minimizing the need for class balancing techniques.

### Feature Engineering

- Experimented with TF-IDF vectorization and BERT embeddings to convert text data into a numerical format that machine learning models can process. This step is critical for capturing the semantic meaning of the reviews.

### Model Training and Evaluation

- Trained various models, including Logistic Regression, LightGBM, and a model leveraging BERT embeddings, adjusting hyperparameters to optimize performance.
- The models were evaluated based on their F1 score on a held-out test set, ensuring the chosen model meets the project's accuracy target.

## Results

The evaluation of different models yielded insightful findings:
- **Logistic Regression with TF-IDF**: Served as a strong baseline, highlighting the effectiveness of traditional NLP techniques in sentiment analysis tasks.
- **LightGBM**: Demonstrated competitive performance, benefiting from the ensemble method's ability to handle complex patterns in data.
- **BERT-based Model**: Achieved superior performance with an F1 score surpassing the project target, showcasing the power of transformer models in capturing nuanced sentiment from textual data.

## Conclusions

This project underscores the potential of machine learning and NLP techniques in automating the categorization of movie reviews. The success of the BERT-based model, in particular, points towards the evolving landscape of sentiment analysis, where deep learning methods can offer significant advantages in understanding human language.

Future Directions:
- Further exploration of model interpretability could provide insights into the features most indicative of negative sentiment.
- Expanding the dataset to include a wider variety of sources and genres could enhance the model's robustness and generalizability.

For contributions or further inquiries, please refer to the repository details.

## Acknowledgments

This project utilizes data provided by Andrew L. Maas et al., from their work on learning word vectors for sentiment analysis. The invaluable dataset has enabled the exploration of advanced sentiment analysis techniques.

