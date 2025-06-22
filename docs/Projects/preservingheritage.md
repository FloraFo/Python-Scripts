# Preserving Heritage – Enhancing Tourism with AI

This capstone project addresses a dual challenge: preserving historical heritage through automation and enhancing the tourist experience through intelligent recommendations. It is divided into two core parts involving both deep learning and machine learning techniques.

## Project Objectives

### 1. Heritage Structure Classification with TensorFlow 🧠
Using **TensorFlow**, I developed a deep learning model to classify historical structures based on images. Leveraging **transfer learning** with a pre-trained CNN backbone, the model was fine-tuned to predict the **category of heritage structures** (e.g., temples, forts, monuments). Key steps included:
- Image preprocessing and augmentation
- Transfer learning using frozen convolutional layers
- Fine-tuning the top dense layers with dropout regularization
- Model training with validation accuracy monitoring
- Visualization of training metrics to detect overfitting

### 2. Tourist Recommendation Engine with EDA 📊
For the second part, I used **machine learning and EDA** to build a personalized tourist **recommendation engine**. This included:
- Data cleaning and exploratory data analysis on user demographics and location preferences
- Insights on the most visited and highly rated tourist places
- Development of a **collaborative filtering model** to suggest attractions based on user behavior

## Datasets Used
- `Structures_dataset.zip` – Images of historical structures
- `Dataseet_test` – Images of historical structures for validation
- `user.csv`, `tourism_with_id.csv`, `tourism_rating.csv` – User demographics and tourism activity

## Outcome
The combined AI solutions automate heritage categorization and intelligently connect tourists with culturally rich destinations, supporting both preservation and sustainable tourism.

