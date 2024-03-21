# Age Verification Model for Alcohol Sales Compliance

## Project Overview

In response to the necessity for strict adherence to alcohol laws, the supermarket chain Good Seed embarked on a pioneering project to leverage Data Science and computer vision technologies for age verification. This initiative aims to develop a machine learning model capable of accurately determining an individual's age from a photo, thus ensuring compliance with legal age restrictions on alcohol sales. The project utilizes a dataset of facial photographs with associated age labels to train a model capable of this task.

## Data Description

The dataset comprises facial photographs obtained from the ChaLearn Looking at People challenge. It includes:
- A collection of 7.6k photographs stored in the `/datasets/faces/final_files/` directory.
- Age labels for each photograph provided in the `/datasets/faces/labels.csv` file.

Given the considerable size of the image dataset, a sequential reading approach using the `ImageDataGenerator` generator is recommended to manage computational resources effectively.

## Methodology

### Exploratory Data Analysis (EDA)
- Evaluated the dataset's size and distribution, highlighting the age diversity among the photographed individuals.
- Visualized the age distribution to understand the dataset's bias and representation.
- Sampled images across different ages to assess variations in image quality, lighting, and facial expressions that could impact model training.

### Model Development and Training
- Adopted the ResNet50 architecture with ImageNet weights for transfer learning, fine-tuned for the age prediction task.
- Employed data augmentation techniques such as rotation, width and height shifts, zooming, and horizontal flipping to enhance model robustness.
- Utilized callbacks like `ReduceLROnPlateau` and `EarlyStopping` to optimize training by adjusting the learning rate and preventing overfitting.

### Evaluation
- The model's performance was evaluated based on the Mean Absolute Error (MAE) metric, with a focus on achieving a low MAE to ensure reliable age predictions.

## Results

- The final model demonstrated a test MAE of 7.9070, indicating its effectiveness in predicting ages from images with reasonable accuracy.
- Through data augmentation and optimized training strategies, the model showed an ability to generalize well to unseen data, suggesting its potential utility for real-world applications in age verification.

## Conclusions

The Good Seed project represents a significant step forward in leveraging technology to enhance compliance with alcohol sales regulations. By developing a model capable of accurately verifying individuals' ages from photographs, we offer a scalable solution that not only aids in preventing underage alcohol sales but also streamlines the customer experience. Future improvements may focus on further reducing the MAE and exploring additional architectures or techniques to handle edge cases and improve prediction accuracy for a wider age range.

For further information or to contribute to this project, please refer to the repository details.

## Acknowledgments

This project utilizes data provided by the ChaLearn Looking at People challenge. We extend our gratitude to the organizers and participants for their valuable contributions to advancing research in computer vision and age estimation.
