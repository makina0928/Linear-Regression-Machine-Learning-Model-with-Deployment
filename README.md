# Predicting Customer Satisfaction with Machine Learning (ZenML & MLflow)


<details>
  <summary style="cursor: pointer; font-size: 40px; color: darkwhite; background-color: darkblack; border: 2px solid gray; border-radius: 5px; padding: 5px;"> Poject implementation strategy </summary>
  

## Introduction
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Solution Overview](#solution-overview)
- [Pipeline Stages](#pipeline-stages)
- [Key Features](#key-features)
- [Expected Benefits](#expected-benefits)
- [Links](#links)
- [Customer Satisfaction Analysis](#customer-satisfaction-analysis)

## Problem Statement
Understanding customer satisfaction is crucial for driving loyalty and reducing churn. Unfortunately, many businesses lack accurate methods to assess customer sentiment towards their products. This project aims to solve this challenge by developing a machine learning model that predicts customer satisfaction scores based on historical data.

## Objectives
- Improve customer satisfaction and loyalty.
- Reduce churn and enhance customer retention.
- Provide targeted interventions and personalized experiences.
- Identify key factors influencing customer satisfaction.

## Solution Overview
This project leverages a powerful technology stack to build a robust and reproducible machine learning pipeline:

- **ZenML:** Automates and orchestrates the entire pipeline, ensuring consistency and efficiency.
- **MLflow:** Tracks experiments, models, and artifacts, enabling easy comparison and analysis.

## Pipeline Stages
1. **Data Ingestion:** Collect customer data from Kaggle ( [Data Source](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)).
2. **Data Preprocessing:** Clean, transform and engineer features for optimal model performance.
3. **Model Training:** Train and evaluate different machine learning models (Logistic Regression, XGBoost or Random Forest) to predict customer satisfaction scores.
4. **Model Selection:** Select the best performing model based on metrics such as accuracy, F1 score and AUC-ROC.
5. **Model Deployment:** Deploy the chosen model to production using ZenML and MLflow deployment tools.
6. **Prediction and Action:** Generate customer satisfaction predictions and trigger targeted interventions based on predictions and business rules.
7. **Monitoring and Feedback:** Continuously monitor model performance and gather feedback for improvement.

## Key Features
- **Reproducible Pipeline:** ZenML guarantees consistent development and deployment across environments.
- **Experiment Tracking:** MLflow provides comprehensive insights into model runs, parameters and performance.

## Expected Benefits
- Increased accuracy in predicting customer satisfaction.
- Enhanced transparency and understanding of model decisions.
- Data-driven insights for product improvement and customer experience optimization.
- A robust and maintainable machine learning workflow.

## Customer Satisfaction Analysis
- Provide specific potential targeted interventions based on customer satisfaction predictions, using [Evidence](https://docs.evidence.dev/).

## Links
- Consider relevant documentation for [ZenML](https://zenml.io/) and [MLflow](https://mlflow.org/)

</details>


<details>
  <summary style="cursor: pointer; font-size: 40px; color: darkwhite; background-color: darkblack; border: 2px solid gray; border-radius: 5px; padding: 5px;"> Poject Structure </summary>
 
- [Machine Learning](#)
  - [data](#)
    - [SalesData.csv](#)
  - [src](#)
    - [data_cleaning.py](#)
    - [evaluation.py](#)
    - [model_dev.py](#)
  - [steps](#)
    - [ingest_data.py](#)
    - [clean_data.py](#)
    - [model_train.py](#)
    - [evaluation.py](#)
    - [config.py](#)
  - [pipelines](#)
    - [deployment_pipeline.py](#)
    - [training_pipeline.py](#)
    - [utils.py](#)
  - [streamlit_app.py](#)
  - [run_deployment.py](#)
  - [run_pipeline.py](#)
  - [requirements.txt](#)
  - [README.md](#)
  - [.zen](#)


## Steps:

1. **Ingest Data**: `steps/ingest_data.py` - Code for ingesting data.
2. **Clean Data**: `steps/clean_data.py` - Code for data cleaning and preprocessing.
3. **Model Training**: `steps/model_train.py` - Code for training the model.
4. **Model Evaluation**: `steps/evaluation.py` - Code for model evaluation.
5. **Configuration**: `steps/config.py` - Configuration file.
