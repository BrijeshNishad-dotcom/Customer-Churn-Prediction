# Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to churn or stay based on customer demographics, services, contract details, and billing information.

## 🚀 Live Demo

[Customer Churn Risk Analyzer](https://customer-churn-risk-analyzer-ml.streamlit.app/)

## 📌 Project Overview

Customer churn is an important business problem for subscription-based companies. Identifying customers who are likely to leave can help businesses take timely retention actions.

This project uses **Logistic Regression** to predict customer churn and provides an interactive **Streamlit** interface where users can enter customer details and get a churn/stay prediction with churn probability.

## ✨ Features

- Interactive customer input form
- 19 customer features
- Churn probability prediction
- User-friendly Yes/No inputs
- Saved ML model and preprocessing pipeline
- Streamlit web interface
- Deployed online using Streamlit Community Cloud

## 🧠 Machine Learning Workflow

1. Data loading
2. Exploratory Data Analysis (EDA)
3. Data preprocessing
4. Feature preparation
5. Train-test split
6. Model training
7. Model comparison
8. ROC-AUC evaluation
9. Final model selection
10. Model and preprocessor saving
11. Streamlit deployment

## 🤖 Models Compared

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

### ROC-AUC Results

| Model | ROC-AUC |
|---|---:|
| Logistic Regression | 0.8421 |
| Decision Tree | 0.6477 |
| Random Forest | 0.8185 |
| Gradient Boosting | 0.8433 |
| XGBoost | 0.8205 |

**Final deployed model: Logistic Regression**

Gradient Boosting achieved a slightly higher ROC-AUC, but Logistic Regression was selected as the final deployed model in this project.

## 📊 Final Model Performance

The saved Logistic Regression model was verified after loading:

- **Accuracy:** 80.55%
- **ROC-AUC:** 0.8421

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| 0 - Stay | 0.85 | 0.89 | 0.87 |
| 1 - Churn | 0.66 | 0.56 | 0.60 |

## 🧾 Input Features

The application uses these 19 features:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── models/
│   ├── logistic_regression.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   └── eda_01.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Run Locally

### Clone the repository

```bash
git clone https://github.com/BrijeshNishad-dotcom/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

## 📦 Model Files

The trained model and preprocessing pipeline are saved using Joblib:

- `models/logistic_regression.pkl`
- `models/preprocessor.pkl`

The Streamlit application loads these files to make predictions on new customer data.

## 🎯 Example Output

The application predicts:

- **Customer is likely to Churn**
- **Customer is likely to Stay**

along with the predicted churn probability.

## 🔮 Future Improvements

- Improve recall for the churn class
- Experiment with additional hyperparameter tuning
- Add probability/risk visualization
- Add customer retention recommendations
- Build a React + FastAPI version for learning

## 👨‍💻 Author

**Brijesh Nishad**

B.Tech Computer Science & Engineering

[GitHub Profile](https://github.com/BrijeshNishad-dotcom)
