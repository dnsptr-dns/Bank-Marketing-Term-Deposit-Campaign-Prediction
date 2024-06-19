# Bank Marketing Term Deposit Campaign Prediction
## Introduction
This project revolves around analyzing data from direct marketing campaigns conducted by a Portuguese banking institution, where phone calls were made to clients to gauge their interest in subscribing to a bank term deposit. The primary aim is to develop a predictive model using supervised learning algorithms like K-Nearest Neighbors (KNN), Support Vector Machines (SVM), Decision Trees, Gradient Boosting and Random Forests to forecast customer subscription tendencies accurately. With insights gleaned from this dataset, the model seeks to optimize the bank's marketing efforts by identifying potential subscribers more effectively. By leveraging targeted strategies, the bank can allocate resources efficiently, enhance campaign efficiency, and ultimately drive business growth.

## Main Features

This project offers several critical analysis and prediction features tailored to address the challenges of analyzing data from direct marketing campaigns conducted by a Portuguese banking institution:

- **Customer Subscription Tendency Forecasting:** Through the utilization of supervised learning algorithms such as K-Nearest Neighbors (KNN), Support Vector Machines (SVM), Decision Trees, Gradient Boosting, and Random Forests, this feature aims to develop predictive models to forecast the likelihood of customers subscribing to the bank's term deposit product accurately.  
- **Feature Selection and Engineering:** This feature focuses on identifying and refining pertinent features that significantly impact customer subscription tendencies. By enhancing model accuracy and interpretability, it enables the optimization of marketing efforts and resource allocation, driving business growth effectively.

## Methodology

The methodology for predicting customer subscription tendencies is structured across several key stages to ensure a thorough and effective analysis:

1. **Data Preprocessing:** The initial step involves preprocessing the dataset to ensure its cleanliness and suitability for analysis. This includes handling missing values, encoding categorical variables, and scaling numerical features to ensure consistency and accuracy.
2. **Exploratory Data Analysis (EDA):** In this phase, comprehensive visualization techniques and statistical analysis are employed to uncover underlying patterns, distributions, and correlations within the dataset. EDA provides valuable insights into customer behavior and informs subsequent modeling decisions.
3. **Feature Engineering:** Feature engineering plays a crucial role in enhancing the predictive capabilities of the models. By selecting, transforming, and creating new features based on domain knowledge and insights gained from EDA, this stage aims to improve model performance and interpretability.
4. **Model Selection and Training:** Leveraging a diverse ensemble of machine learning algorithms, including Support Vector Machines (SVM), K-Nearest Neighbors (KNN), XGBoost, Random Trees, and Random Forests, the project explores the strengths of each method in predicting customer subscription tendencies accurately. Models are trained on the preprocessed data and evaluated based on their performance metrics.
5. **Model Evaluation and Validation:** Rigorous evaluation metrics and cross-validation techniques are employed to assess the performance of each model. This ensures robustness and reliability in real-world applications and helps identify the best-performing model for deployment.
6. **Hyperparameter Tuning:** Fine-tuning the parameters of each model further enhances their predictive accuracy and generalization ability. This optimization process aims to optimize performance across different datasets and scenarios, ensuring the models are well-suited for predicting customer subscription tendencies.
7. **Ensemble Learning:** Ensemble methods, such as XGBoost and Random Forests, are employed to combine predictions from multiple models. This approach helps improve prediction accuracy and mitigate overfitting, offering a comprehensive and robust solution for predicting customer subscription tendencies effectively.

## Results

The ensemble of machine learning algorithms, including Support Vector Machines (SVM), K-Nearest Neighbors (KNN), XGBoost, Random Trees, and Random Forests, delivers promising outcomes in predicting customer churn effectively. Through thorough evaluation and validation, the models showcase their capability to forecast churn with a notable degree of accuracy. These results underscore the effectiveness of the approach in analyzing and predicting customer churn, offering valuable insights for enhancing customer retention strategies in the banking industry.

## File Descriptions

- Bank-Marketing-Term-Deposit-Campaign-Prediction.ipynb: Main notebook containing the analysis and modeling process.
- Bank-Marketing-Term-Deposit-Campaign-Prediction_inference.ipynb: Additional notebook focusing on further model insights. 
- selected_features.txt: Selected columns used as features in machine learning models 
- model_pipeline: Machine learning model created in this project

## References

Dataset     : <a href="https://archive.ics.uci.edu/dataset/222/bank+marketing">Bank Marketing</a>.  
HuggingFace : <a href="https://huggingface.co/spaces/taliida-nabilah/Banks_Customer_Deposit_Subscription">Banks_Customer_Deposit_Subscription</a>. 

