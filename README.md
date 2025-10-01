Churn Predictor for a Telecom Company
Overview

This project implements a machine learning-based churn prediction system for a telecom company. The objective is to identify customers likely to discontinue services, enabling targeted retention strategies.

The project demonstrates a complete end-to-end machine learning workflow:

Data exploration and visualization.

Feature engineering and preprocessing.

Model training, testing, and evaluation.

Deployment of the prediction model as a web application using Flask and Docker.

Hosting the application on Render (Free Tier) for public access.

Features

EDA and Insights (Churn.ipynb):

Analyzed customer demographics, contract types, payment methods, and service usage.

Identified key churn drivers such as tenure, contract type, and monthly charges.

Model Development (churn_deploy_training.ipynb):

Preprocessing with custom frequency encoding (customencoder.py).

Balanced dataset using imbalanced-learn.

Built and trained classification models (Random Forest, Logistic Regression, etc.).

Evaluated using accuracy, precision, recall, and F1-score.

Model Testing (churn_deploy_test.ipynb):

Validated trained models on test data.

Compared results and confirmed model generalization.

Deployment:

Flask application (app.py) with an HTML interface (templates/index.html).

Packaged and containerized with Docker (Dockerfile).

Deployed on Render, providing a live demo link.

Tech Stack

Languages: Python

Libraries: pandas, NumPy, scikit-learn, imbalanced-learn, matplotlib, seaborn, Flask

Deployment: Docker, Render (Free Tier)

Version Control: Git, GitHub
