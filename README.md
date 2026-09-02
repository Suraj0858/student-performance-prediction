# Student Performance Prediction using Linear Regression

## Project Overview

This project uses **Linear Regression** to predict a student's **Performance Index** based on academic and daily activity-related features.

The project covers both **Simple Linear Regression** and **Multiple Linear Regression**, followed by model evaluation and saving the trained model for future predictions.

## Objective

The objective of this project is to predict student performance using:

* Previous Scores
* Hours Studied
* Sleep Hours
* Sample Question Papers Practiced

The project also compares the performance of a model using a single input feature with a model using multiple input features.

## Dataset

The dataset contains student-related information such as:

* **Hours Studied** – Number of hours studied
* **Previous Scores** – Student's previous score
* **Extracurricular Activities** – Whether the student participates in extracurricular activities
* **Sleep Hours** – Number of hours slept
* **Sample Question Papers Practiced** – Number of sample papers practiced
* **Performance Index** – Target variable representing student performance

## Machine Learning Approach

### 1. Simple Linear Regression

Initially, **Previous Scores** was selected as the input feature because it showed a strong correlation with the Performance Index.

**Input Feature:**

* Previous Scores

**Target:**

* Performance Index

### Simple Linear Regression Results

| Metric   |  Result |
| -------- | ------: |
| MAE      |  6.5980 |
| MSE      | 60.0643 |
| RMSE     |  7.7501 |
| R² Score |  0.8340 |

### 2. Multiple Linear Regression

The model was then developed using multiple numerical input features:

* Hours Studied
* Previous Scores
* Sleep Hours
* Sample Question Papers Practiced

**Target:**

* Performance Index

### Multiple Linear Regression Results

| Metric   | Result |
| -------- | -----: |
| MAE      | 1.5763 |
| MSE      | 3.9334 |
| RMSE     | 1.9833 |
| R² Score | 0.9891 |

The Multiple Linear Regression model achieved a higher R² score and lower error values compared with the Simple Linear Regression model.

## Model Evaluation

The following regression evaluation metrics were used:

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**
* **Adjusted R²**

## Model Saving and Prediction

The trained Multiple Linear Regression model was saved using **Joblib**.

The saved model contains:

* Input features
* Target feature
* Trained Linear Regression model

The saved model can be loaded later to make predictions for new student data.

Example prediction:

```text
Predicted Performance: 75.71
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook

## Machine Learning Algorithm

**Linear Regression**

The project demonstrates:

* Simple Linear Regression
* Multiple Linear Regression
* Train-Test Split
* Model Training
* Prediction
* Model Evaluation
* Model Saving
* Future Prediction

## Project Structure

```text
student-performance-linear-regression/
│
├── student_performance_linear_regression.ipynb
├── linear_regression.joblib
└── README.md
```

## Key Learning Outcomes

* Understanding Simple Linear Regression
* Understanding Multiple Linear Regression
* Selecting input and target features
* Using correlation for initial feature analysis
* Splitting data into training and testing sets
* Training regression models using Scikit-learn
* Evaluating regression models using different metrics
* Comparing Simple and Multiple Linear Regression
* Saving and loading trained models using Joblib
* Making predictions using a saved model
