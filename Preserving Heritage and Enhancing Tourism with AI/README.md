# 🏛️ Capstone Project: Preserving Heritage – Enhancing Tourism with AI

This repository documents my AIML capstone project focused on **cultural heritage preservation** and **tourism enhancement** using Artificial Intelligence. The project is divided into two main tracks: a deep learning solution to classify heritage structures and a machine learning pipeline to build a recommendation system for tourists.

---

## 🚀 Project Objectives

### 1. 🧠 Heritage Structure Classification with TensorFlow

To support heritage documentation efforts, I developed a deep learning model using **TensorFlow** and **transfer learning** techniques to predict the **category of a structure** from an image (e.g., temple, palace, fort).

#### 🔍 Model Selection

I tested **three CNN architectures**:
- `VGG16`
- `InceptionV3`
- `ResNet50`

📊 **Evaluation Summary**:
- All three models showed signs of **overfitting**.
- **VGG16** and **ResNet50** improved in validation accuracy across epochs.
- **InceptionV3** **decreased** in accuracy over time.
- When analyzing loss:
  - Only **ResNet50** showed a consistently **decreasing validation loss**, suggesting better generalization.

➡️ **Final choice**: `ResNet50` was selected due to its superior and more stable validation performance.

#### 🛠️ Fine-Tuning & Results

- Top layers were modified with dense layers and dropout for regularization.
- The model was compiled with appropriate optimizer and early stopping callbacks.
- **Target Validation Accuracy of 0.9000** was reached **at epoch 1**, confirming early convergence and strong baseline generalization.

---

### 2. 📊 Tourist Recommendation Engine with EDA

To improve tourism outreach, I performed **exploratory data analysis** on visitor demographics and preferences, and developed a **collaborative filtering recommendation engine**.

Key steps:
- Cleaned and merged `user.csv`, `tourism_with_id.csv`, and `tourism_rating.csv`
- Analyzed user age groups, city preferences, and place popularity
- Identified top-rated places and common tourist patterns
- Built a **memory-based collaborative filtering model** using user-item interactions

✅ *MAP@K Score: YY (placeholder — insert your performance metric if available)*
#TODO
---

## 📂 Datasets Used

| Dataset / Folder | Description |
|------------------|-------------|
| `Structures_dataset.zip` | Images of historical structures used for training the classification model |
| `Dataset_test` | Folder containing validation images used to test the trained CNN models |
| `user.csv` | Tourist demographic information |
| `tourism_with_id.csv` | Tourist attraction metadata (name, category, city, etc.) |
| `tourism_rating.csv` | Ratings of tourist places by users |

---

## 💡 Project Outcome

This project demonstrates how AI can:
- Automate **cultural classification** for improved heritage archiving
- Personalize tourism via **data-driven recommendations**
- Contribute to **smart, sustainable tourism development**

---

## 🔗 Repository Structure

📁 data/ → raw and processed datasets
📁 notebooks/ → Jupyter notebooks for both parts
📁 models/ → Saved models and training logs
📄 README.md → Project overview

---

## 📸 Sample Outputs *(Optional – Add screenshots or visualizations)*

- 📊 EDA Charts: Age group distribution, Top-rated places per city  
- 🏷️ Classification Result: Sample image and predicted category  
- 📍 Recommendations: Top 5 places for a sample user  

---

## 📌 Tools & Libraries
- Python, TensorFlow, Keras  
- Pandas, NumPy, Matplotlib, Seaborn  
- Scikit-learn, Surprise (for collaborative filtering)  
- OpenCV (for image processing)

---

## 🙋‍♀️ Author  
**Filomena Forina**  
PGC AIML Capstone 2025 — Caltech Post Graduate Program in AI and Machine Learning / Caltech
[LinkedIn Profile] <a href="https://www.linkedin.com/in/filomenaforina/" target="_blank">Filomena FORINA</a> 

---
