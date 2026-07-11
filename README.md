# 🏦 Bank Customer Churn Prediction using Artificial Neural Networks (ANN)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge\&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow?style=for-the-badge\&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### Predict customer churn using a Deep Learning model deployed as an interactive Streamlit web application.

### 🌐 **Live Demo**

**https://churn-predictions-ann.streamlit.app/**

</div>

---

# 📖 Overview

Customer churn is one of the biggest challenges faced by banks. Retaining existing customers is significantly more cost-effective than acquiring new ones.

This project leverages an **Artificial Neural Network (ANN)** built with **TensorFlow/Keras** to predict whether a customer is likely to leave the bank based on demographic and financial information.

The trained model is integrated into a **Streamlit web application**, allowing users to perform real-time churn predictions through an intuitive interface.

---

# ✨ Features

* 🧠 Deep Learning-based Binary Classification
* ⚡ Real-time Customer Churn Prediction
* 📊 Probability Score for Better Decision Making
* 🌐 Interactive Streamlit Web Interface
* 📈 Standardized Input using StandardScaler
* 🚀 Ready for Cloud Deployment
* 💡 Clean and User-Friendly UI

---

# 🌐 Live Application

🔗 **Streamlit App**

https://churn-predictions-ann.streamlit.app/

Try different customer profiles and instantly view the churn prediction along with its probability.

---

# 📂 Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── app.py                 # Streamlit Application
├── ann_model.h5           # Trained ANN Model
├── scaler.pkl             # StandardScaler
├── dataset.csv            # Dataset
├── requirements.txt
├── README.md
└── assets/
```

---

# 🧠 Model Pipeline

```text
             Customer Information
                     │
                     ▼
           Data Preprocessing
         (StandardScaler.pkl)
                     │
                     ▼
     Artificial Neural Network
        (TensorFlow / Keras)
                     │
                     ▼
      Churn Probability Score
                     │
                     ▼
      Customer Stay / Customer Churn
```

---

# 📊 Dataset

The project uses the **Bank Customer Churn Dataset**, containing customer demographic, financial, and behavioral information.

## Input Features

| Feature            | Description              |
| ------------------ | ------------------------ |
| Credit Score       | Customer credit score    |
| Gender             | Male / Female            |
| Age                | Customer age             |
| Tenure             | Years with the bank      |
| Balance            | Current account balance  |
| Number of Products | Banking products owned   |
| Has Credit Card    | Yes / No                 |
| Is Active Member   | Active membership status |
| Estimated Salary   | Annual salary            |

## Target Variable

| Value | Meaning         |
| ----- | --------------- |
| **0** | Customer Stays  |
| **1** | Customer Churns |

---

# 🧠 Artificial Neural Network Architecture

```text
Input Layer (9 Features)
          │
          ▼
Dense Layer (ReLU)
          │
          ▼
Dense Layer (ReLU)
          │
          ▼
Output Layer (Sigmoid)
```

### Model Configuration

| Parameter         | Value               |
| ----------------- | ------------------- |
| Framework         | TensorFlow / Keras  |
| Optimizer         | Adam                |
| Loss Function     | Binary Crossentropy |
| Output Activation | Sigmoid             |
| Evaluation Metric | Accuracy            |

---

# ⚙️ Data Preprocessing

The following preprocessing steps were performed before model training:

* Removed unnecessary columns
* Encoded categorical values
* Selected relevant numerical features
* Train/Test split
* Feature Scaling using **StandardScaler**

The trained scaler is stored as:

```text
scaler.pkl
```

This guarantees that inference data is transformed exactly as the training data.

---

# 🚀 How Prediction Works

```text
Customer Inputs
        │
        ▼
StandardScaler
        │
        ▼
Artificial Neural Network
        │
        ▼
Prediction Probability
        │
        ▼
Stay or Churn
```

---

# 🖥️ Application Inputs

The web application accepts:

* Credit Score
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Status
* Active Membership
* Estimated Salary

---

# 📈 Sample Prediction

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

### Output

```text
Prediction Probability : 34%

Prediction :
Customer is likely to Stay.
```

---

# 🛠️ Tech Stack

| Category            | Technologies      |
| ------------------- | ----------------- |
| Language            | Python            |
| Deep Learning       | TensorFlow, Keras |
| Machine Learning    | Scikit-learn      |
| Data Processing     | Pandas, NumPy     |
| Web Framework       | Streamlit         |
| Model Serialization | Joblib            |

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/M-Sudheer18/Churn_Prediction-Using-ANN.git
```

Navigate into the project

```bash
cd Churn_Prediction-Using-ANN
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

The application will launch automatically in your browser.

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

# ☁️ Deployment

The project can be deployed on:

* ✅ Streamlit Community Cloud
* ✅ Hugging Face Spaces
* ✅ Render
* ✅ Railway
* ✅ AWS EC2
* ✅ Microsoft Azure
* ✅ Google Cloud Platform

---

# 🚀 Future Improvements

* 🌍 Geography Feature Support
* 📈 SHAP Explainability
* 📂 Batch Prediction using CSV Upload
* ⚡ FastAPI REST API
* 🐳 Docker Containerization
* 📊 Model Monitoring Dashboard
* 🗄️ Database Integration
* 🔐 Authentication & User Login
* 📉 Model Performance Visualization

---

# 📷 Application Preview

The application provides:

* Interactive Input Widgets
* Instant Predictions
* Churn Probability
* Responsive Layout
* Easy-to-use Interface

> *(Add screenshots or GIFs here for a richer GitHub presentation.)*

---

# 👨‍💻 Author

## **Sudheer Muthyala**

**B.Tech – Electronics and Communication Engineering**

**Aspiring Data Scientist | Machine Learning Engineer | Deep Learning Enthusiast | Python Developer**

### Connect with Me

* **GitHub:** https://github.com/M-Sudheer18
* **LinkedIn:** https://www.linkedin.com/in/sudheer-muthyala-317180268

---

# ⭐ Support the Project

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

💬 Share your feedback

🚀 Contribute improvements

Every contribution is appreciated!

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it for educational and research purposes.

---

<div align="center">

## ⭐ If you like this project, don't forget to Star the Repository!

**Made with ❤️ by Sudheer Muthyala**

</div>
