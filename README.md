# Car Price Prediction Using Linear Regression ML Model


## Tools and Environment setup
1. [GitHub Account](https://github.com)
2. [Docker](https://www.docker.com/)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Create a New Environment
```bash
conda create -p venv python==3.12 -y
```

```bash
conda activate venv/
```

### Git Configuration
```bash
git config --global user.name "USER_NAME"
```

```bash
git config --global user.email "USER_EMAIL"
```

###  Starting a Docker Container
```bash
docker-compose up -d
```
###  Stopping a Docker Container
```bash
docker-compose down
```

## Introduction
This project focuses on predicting car selling prices using a linear regression model. Accurate predictions are vital for buyers and sellers in the automotive market, as many rely on unreliable valuation methods that overlook historical pricing trends and vehicle features. This project aims to enhance pricing accuracy, assist stakeholders in making informed decisions, and identify factors influencing car prices.

## Objectives
- Improve the accuracy of car price predictions.
- Assist buyers and sellers in making informed decisions.
- Identify key factors influencing car pricing.

## Key Features
- **Reproducible Environment:** Docker ensures consistent deployment across systems.
- **Version Control:** GitHub tracks all versions and changes to the codebase.

## Expected Benefits
- Increased accuracy in predicting car prices.
- Enhanced transparency and understanding of model predictions.
- Data-driven insights for market trends and customer needs.
- A robust and maintainable machine learning workflow.

## Project Structure

```
[web/]
├── [src/]
│   ├── [mlmodel/]
│   │   ├── car_price_prediction.pkl
│   │   └── scaling.pkl
│   ├── [static/]
│   │   ├── car1.jpg
│   │   └── style.css
│   └── [templates/]
│       ├── car.html
│       ├── error.html
│       └── result.html
├── app.py
├── config.py
├── forms.py
├── requirements.txt
├── Car_data.csv
└── docker-compose.yaml
└── Notebook for LR Model
```

## Pipeline Stages

1. **Data Ingestion** (`[web/]` and `[src/]`)
   - Data about cars was collected and merged from [Kaggle](https://www.kaggle.com/datasets/gunishj/carpricepred) , and stored in the main directory `[web/]` as [Car_data.csv](./Car_data.csv).
   - Relevant code to load and preprocess this data is stored in `[src/]` as [Notebook-for-LR-Model.ipynb](./src/Notebook-for-LR-Model.ipynb).

2. **Model Training, Testing and Evaluation** (`[src/mlmodel/]`)
   - The pickle file of the trained and evaluated model from [Notebook-for-LR-Model.ipynb](./src/Notebook-for-LR-Model.ipynb) is housed in `[src/mlmodel/]` and saved as [car_price_prediction.pkl](./src/mlmodel/car_price_prediction.pkl).

3. **Model Scaling** (`[src/mlmodel/]`)
   - The pickle file of the Standardization object from [Notebook-for-LR-Model.ipynb](./src/Notebook-for-LR-Model.ipynb) is housed in `[src/mlmodel/]` and saved as [scaling.pkl](./src/mlmodel/scaling.pkl).

4. **Model Deployment** (`[web/]`)
   - The web application setup is configured in the `[web/]` directory, with the primary deployment environment managed by [Dockerfile](./Dockerfile) and [docker-compose.yaml](./docker-compose.yaml).
   - Docker ensures that model deployment is consistent and reproducible across different systems.

5. **Prediction and Action** (`[src/templates/]` and `[src/static/]`)
   - User input is handled through forms in `[src/templates/]`, which contains HTML templates ([car.html](./web/src/templates/car.html), [error.html](./src/templates/error.html), and [result.html](./src/templates/result.html)) for displaying input, error messages, and prediction results, respectively.
   - Static files such as [image](./src/static/car1.jpg) images and [CSS](./src/static/style.css) for styling are located in `[src/static/]`.


## Pipeline Details

- **[app.py](./app.py)**: The main application file that runs the web server and handles routing.
- **[config.py](./src/config.py)**: Configuration file for application parameters and environment variables.
- **[forms.py](./src/forms.py)**: Contains form definitions and validations.
- **[requirements.txt](./requirements.txt)**: Lists Python dependencies required to run the application.
- **[Car_data.csv](./Car_data.csv)**: Dataset used for training and predictions.
- **[Dockerfile](./Dockerfile)**: Configuration file for managing application services with Docker.
- **[Notebook for LR Model](./src/Notebook%20for%20LR%20Model)**: Jupyter Notebook for experiments and analysis.

### [src/](./src/)
Contains the source code and resources for the application.

#### [mlmodel/](./src/mlmodel/)
Holds machine learning models and related files.

- **[car_price_prediction.pkl](./src/mlmodel/car_price_prediction.pkl)**: Pickled machine learning model for predicting car prices.
- **[scaling.pkl](./src/mlmodel/scaling.pkl)**: Pickled scaler object for standardizing input features.

#### [static/](./src/static/)
Contains static files such as images and stylesheets.

- **[car1.jpg](./src/static/car1.jpg)**: Image file used in the web application.
- **[style.css](./src/static/style.css)**: CSS file for styling the application.

#### [templates/](./src/templates/)
Contains HTML templates for rendering web pages.

- **[car.html](./src/templates/car.html)**: Template for displaying car information.
- **[error.html](./src/templates/error.html)**: Template for displaying error messages.
- **[result.html](./src/templates/result.html)**: Template for displaying prediction results.


### Note
This project focuses on training, testing, and forecasting the selling price using a linear regression model. For a detailed exploration of exploratory data analysis (EDA), data cleaning, and feature engineering, please refer to the **[EDA Notebook](https://github.com/makina0928/Linear-Regression-Machine-Learning-Model-with-Deployment/blob/main/EDA%20for%20ML/EDA%20of%20Car%20Sales%20Price%202024.ipynb)**.

**Credit is given to [Jinesh Patel](https://medium.com/analytics-vidhya/deploying-linear-regression-ml-model-as-web-application-on-docker-3409f9464a27) for the implementation methods utilized in this project.**


