# 🏦 Bank Customer Churn Prediction using Artificial Neural Network (ANN)

## 📌 Overview

This project is a **Deep Learning-based Bank Customer Churn Prediction System** that predicts whether a customer is likely to leave the bank based on their demographic and financial information.

The project consists of three main components:

* 🧠 **Artificial Neural Network (ANN) Model** (`ann_model.h5`)
* 📊 **StandardScaler** (`scaler.pkl`) for preprocessing
* 🌐 **Streamlit Web Application** (`app.py`) for user interaction

The application accepts customer details, preprocesses the data using the saved scaler, performs inference using the trained ANN model, and displays the probability of churn along with the final prediction.

---

# 🚀 Features

* Deep Learning-based Binary Classification
* Interactive Streamlit Interface
* Real-time Customer Churn Prediction
* StandardScaler for consistent preprocessing
* Probability Score Display
* Easy Deployment on Hugging Face Spaces
* Clean and Responsive UI

---

# 📂 Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── app.py                # Streamlit Frontend
├── ann_model.h5          # Trained ANN Model
├── scaler.pkl            # Saved StandardScaler
├── requirements.txt
├── README.md
└── dataset.csv
```

---

# 📊 Dataset

The project uses the **Bank Customer Churn Dataset**.

### Input Features

| Feature         | Description                   |
| --------------- | ----------------------------- |
| CreditScore     | Customer's credit score       |
| Gender          | Customer gender               |
| Age             | Customer age                  |
| Tenure          | Number of years with the bank |
| Balance         | Current account balance       |
| NumOfProducts   | Number of bank products       |
| HasCrCard       | Credit card ownership         |
| IsActiveMember  | Active membership status      |
| EstimatedSalary | Estimated annual salary       |

### Target Variable

| Value | Meaning                 |
| ----- | ----------------------- |
| 0     | Customer Stays          |
| 1     | Customer Leaves (Churn) |

---

# 🧠 Artificial Neural Network (ANN)

The project uses a fully connected **Artificial Neural Network** for binary classification.

## Model Architecture

| Layer          | Description           |
| -------------- | --------------------- |
| Input Layer    | 9 Input Features      |
| Hidden Layer 1 | Dense Layer (ReLU)    |
| Hidden Layer 2 | Dense Layer (ReLU)    |
| Output Layer   | Dense Layer (Sigmoid) |

### Activation Functions

* ReLU
* Sigmoid

### Optimizer

Adam Optimizer

### Loss Function

Binary Crossentropy

### Evaluation Metric

Accuracy

---

# 📈 Data Preprocessing

Before training, the following preprocessing steps were performed:

* Removed unnecessary columns
* Encoded Gender
* Selected relevant numerical features
* Split dataset into Training and Testing sets
* Standardized features using **StandardScaler**

The fitted scaler was saved as:

```text
scaler.pkl
```

This ensures that every new customer entered in the Streamlit application is transformed exactly as the training data.

---

# 📁 Model Files

## 🧠 ANN Model

```text
ann_model.h5
```

Contains the trained Artificial Neural Network.

Load the model:

```python
import tensorflow as tf

model = tf.keras.models.load_model("ann_model.h5")
```

---

## 📊 StandardScaler

```text
scaler.pkl
```

Contains the trained StandardScaler.

Load the scaler:

```python
import joblib

scaler = joblib.load("scaler.pkl")
```

Scale the user input:

```python
scaled_input = scaler.transform(input_data)
```

---

## 🌐 Streamlit Frontend

```text
app.py
```

The frontend collects customer information, preprocesses the data using the saved StandardScaler, sends it to the ANN model, and displays the prediction result.

---

# 🔄 Prediction Workflow

```text
User Input
      │
      ▼
Streamlit Frontend
      │
      ▼
StandardScaler (scaler.pkl)
      │
      ▼
ANN Model (ann_model.h5)
      │
      ▼
Prediction Probability
      │
      ▼
Stay or Churn
```

---

# 🖥️ User Inputs

The application accepts the following inputs:

* Credit Score
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Is Active Member
* Estimated Salary

---

# 📌 Example Prediction

### Input

```text
Credit Score        : 619
Gender              : Female
Age                 : 42
Tenure              : 2
Balance             : 0
Products            : 1
Has Credit Card     : Yes
Is Active Member    : Yes
Estimated Salary    : 101348.88
```

### Model Output

```text
Prediction Probability : 0.34

Customer is likely to Stay.
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Bank-Customer-Churn-Prediction.git
```

Move to the project directory

```bash
cd Bank-Customer-Churn-Prediction
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```text
streamlit
tensorflow
numpy
pandas
scikit-learn
joblib
```

---

# 🌍 Deployment

This project can be deployed on:

* 🤗 Hugging Face Spaces
* Streamlit Community Cloud
* Render
* Railway
* AWS EC2
* Microsoft Azure
* Google Cloud Platform

---

# 📸 Application Preview

The application provides:

* Interactive sliders and input fields
* Real-time prediction
* Churn probability score
* Customer Stay/Leave result

---

# 🚀 Future Enhancements

* Add Geography feature
* SHAP Explainable AI
* Batch Prediction using CSV Upload
* REST API with FastAPI
* Docker Containerization
* Model Monitoring Dashboard
* Database Integration
* Authentication System

---

# 👨‍💻 Author

**Sudheer Muthyala**

**B.Tech – Electronics and Communication Engineering**

Aspiring **Data Scientist | Machine Learning | Deep Learning | Python Developer**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# 📄 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project for educational and research purposes.

---

## ⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork the repository

🛠️ Contribute improvements

📢 Share it with others

Thank you for visiting this project!
