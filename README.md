# Loan Approval Prediction Using Machine Learning

## Project Overview

This project predicts whether a loan application is likely to be approved based on the applicant's personal, financial, employment, and credit-related information.

I developed a machine learning model using **Logistic Regression** and built an interactive web application using **Streamlit**, allowing users to enter customer details and receive a prediction.

## Problem Statement

Financial institutions need to assess loan applications using information such as income, employment experience, loan amount, credit score, and previous loan defaults.

The objective of this project is to build a classification model that learns patterns from historical loan application data and predicts the loan status of a new applicant.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Logistic Regression
- StandardScaler
- OneHotEncoder
- ColumnTransformer
- Joblib
- Streamlit

## Dataset Features

The model uses the following input features:

| Category | Features |
|---|---|
| Personal details | Age, gender, education |
| Financial details | Annual income, loan amount, loan interest rate, loan percentage of income |
| Employment | Employment experience |
| Housing | Home ownership |
| Loan details | Loan intent |
| Credit details | Credit history length, credit score, previous loan defaults |

**Target variable:** `loan_status`

## Machine Learning Workflow

1. Load and prepare the dataset.
2. Separate the input features and target variable.
3. Split the data into training and testing sets using an 80:20 ratio.
4. Separate numerical and categorical features.
5. Standardize numerical features using `StandardScaler`.
6. Encode categorical features using `OneHotEncoder`.
7. Combine preprocessing steps using `ColumnTransformer`.
8. Train a Logistic Regression classification model.
9. Evaluate the model on the test dataset.
10. Save the trained model pipeline using Joblib.
11. Build a Streamlit application for interactive predictions.

## Model and Preprocessing

The project uses Logistic Regression for binary classification.

A preprocessing pipeline handles numerical and categorical features before they are passed to the classifier. This helps ensure that new application inputs receive the same preprocessing as the training data.

The saved model is loaded into the Streamlit application to generate predictions.

## Streamlit Web Application

The application allows users to enter customer details through a web form.

Key features include:

- Input fields for applicant and loan details
- Dropdown menus for categorical information
- Validation for required fields and numeric ranges
- Loan approval prediction
- Approval probability display when supported by the model

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Prabagaranthirumoorthy/Loan_Prediction.git
cd Loan_Prediction
```

### 2. Install the dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages:

```bash
pip install streamlit pandas scikit-learn
```

Use compatible package versions if your saved model requires them.

### 3. Run the application

Make sure `app.py` and `loan_model.pkl` are in the expected locations, then run:

```bash
streamlit run app.py
```

The application will open in your browser.

## Future Improvements

- Improve model performance through hyperparameter tuning.
- Compare Logistic Regression with other classification algorithms.
- Add additional evaluation visualizations.
- Deploy the application to a public hosting platform.
- Improve the interface and provide clearer explanations of predictions.

## Author

**Prabagaran Thirumoorthy**

GitHub: `Prabagaranthirumoorthy`

