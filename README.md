# Car price prediction using Linear Regression ML model


<details>
  <summary style="cursor: pointer; font-size: 40px; color: darkwhite; background-color: darkblack; border: 2px solid gray; border-radius: 5px; padding: 5px;"> Poject implementation strategy </summary>
  

## Introduction
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Software-And-Tools-Requirements](#Software And Tools Requirements)
- [Pipeline Stages](#pipeline-stages)
- [Key Features](#key-features)
- [Expected Benefits](#expected-benefits)
- [Links](#links)
- [Car Price Prediction Analysis](#car-price-prediction-analysis)

## Problem Statement
Accurate car price prediction is essential for both buyers and sellers in the automotive market. Many stakeholders struggle with unreliable valuation methods that do not account for historical pricing trends and vehicle features. This project aims to address this challenge by developing a linear regression model to predict car prices based on historical data.

## Objectives
- Improve the accuracy of car price predictions.
- Assist buyers and sellers in making informed decisions.
- Identify key factors influencing car pricing.
- Enhance market insights through data-driven analysis.

## Software And Tools Requirements
1. [GitHub Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3.[VS CODE IDE](https://code.visualstudio.com/)
4.[Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

```
conda create -p venv python==3.12 -y
```

```
conda activate venv/
```
git configuration
```
git config --global user.name "USER_NAME"
```

```
git config --global user.email "USER_EMAIL"
```
## Pipeline Stages
1. **Data Ingestion:** Collected and merged data about cars from Kaggle ( [Data Source](https://www.kaggle.com/datasets/gunishj/carpricepred)).
2. **Model Training:** Train and evaluate a linear regression machine learning model to predict car price based on the user input.
4. **Model Selection:** Select the best performing model based on metrics such as $R^2$ and RMSE.
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
</details>

# Note

This notebook focuses on training, testing, and forecasting sales using linear regression. For a detailed exploration of exploratory data analysis EDA, data cleaning, and feature engineering, please refer to the **[EDA-Notebook](https://github.com/makina0928/Linear-Regression-Machine-Learning-Model-with-Deployment/blob/main/EDA%20for%20ML/EDA%20of%20Car%20Sales%20Price%202024.ipynb)**.

Credit is given to [Jinesh-Patel](https://medium.com/analytics-vidhya/deploying-linear-regression-ml-model-as-web-application-on-docker-3409f9464a27), the implementor of the methods utilized in this notebook.
