# Customer Churn Predictor

This project implements a **customer churn prediction system** for a NovaConnect, a fictional company. The model identifies customers at risk of leaving the service, helping enable appropriate retention strategies.  

The application is deployed as a **Flask web app** inside a Docker container, making it easy to run locally or host on platforms like **Render**. Users can input customer details through a simple web form and receive churn predictions in real time.

## Company Background and Business Challenge:

**Company Background**  
**NovaConnect** is a mid-sized subscription-based internet service provider operating across multiple regions. With increasing market competition and rising customer acquisition costs, leadership has shifted focus from acquiring new customers to retaining existing ones.

**Business Challenge**  
NovaConnect has observed increasing customer churn. Executives need a predictive system to answer the critical question:

- **Who is likely to churn?**

This repository includes the EDA, training and testing notebooks, a production-ready inference pipeline, and a Dockerized Flask app that serves churn predictions.

---

## Data
The dataset contains customer-level features such as:
- **Demographics** (e.g., SeniorCitizen, Gender)
- **Service Details** (e.g., InternetService, TechSupport, Contract)
- **Billing Details** (e.g., MonthlyCharges, PaymentMethod, TotalCharges)

The target variable is **Churn** (Yes/No).

---

## Features
- End-to-end **machine learning pipeline** for churn prediction
- Deployed via **Flask** with a web-based interface
- Containerized with **Docker** for portability
- Hosted on **Render**

---

## Project Files

- app.py -> Flask application

- CustomEncoder.py -> Custom frequency encoder for categorical features
  
- Dockerfile -> Docker configuration
  
- requirements.txt -> Python dependencies
  
- templates/
  
  - churn.html -> Frontend HTML form for user input
    
-  notebooks/
  
  - Churn.ipynb -> Exploratory Data Analysis, Modeling
    
  - churn_deploy_training.ipynb -> Model training pipeline
    
  - churn_deploy_test.ipynb -> Model testing and validation
    
- my_ml_pipeline # pickle file of trained model



---

## Model Pipeline
1. **Preprocessing**
   - Missing value handling
   - Custom frequency encoding of categorical features
2. **Model Training**
   - Built with **scikit-learn** and **imbalanced-learn**
   - Addressed class imbalance with Synthetic Minority Oversampling Technique (SMOTE)
3. **Evaluation**
   - Metrics: F1-Score, Recall, Precision, CV Score
   - Achieved strong balance between precision and recall for identifying churners
4. **Deployment**
   - Model serialized with `pickle`
   - Integrated with Flask web app for real-time inference

---


This project is deployed on **Render** using **Docker**.  
Render automatically builds the container from the `Dockerfile` and serves the Flask app.  

- Public link: [Churn Predictor App](https://churn-predictor-sbr0.onrender.com)
- Backend: Flask + scikit-learn model
- Containerization: Docker

---


## Results and Insights

### The Random Forest model provided strong performance with:
F1-score: 80%
Recall: 82%
Precision: 77%
Variance error: 2%

### Key churn drivers include:

- Contract type: Month-to-month contracts are high risk.

- Tenure: Short-term customers are more likely to churn.

- Monthly charges: Higher charges increase churn likelihood.

- Online services usage: Lack of additional services seem to affect customer churn, for instance lack of tech support has caused a customers to churn.


## Tech Stack

Languages: Python
Libraries: pandas, NumPy, scikit-learn, imbalanced-learn, matplotlib, seaborn, Flask
Deployment: Docker, Render
Version Control: Git, GitHub

---

This project is deployed on **Render** using **Docker**.  
Render automatically builds the container from the `Dockerfile` and serves the Flask app.  

- Public link: [Churn Predictor App](https://churn-predictor-sbr0.onrender.com)
- Backend: Flask + scikit-learn model
- Containerization: Docker


Author
Gayathri K

