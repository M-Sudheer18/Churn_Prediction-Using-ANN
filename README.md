# 🧠 Bank Customer Churn ANN Model

## Overview

This repository contains the trained **Artificial Neural Network (ANN)** model used to predict whether a bank customer is likely to churn.

The model was trained using TensorFlow/Keras on the Bank Customer Churn dataset after preprocessing and feature scaling.

---

## Model Information

* Model Type: Artificial Neural Network (ANN)
* Framework: TensorFlow / Keras
* Model File: `ann_model.h5`
* Prediction Type: Binary Classification

---

## Input Features

The model expects **9 input features** in the following order:

1. CreditScore
2. Gender
3. Age
4. Tenure
5. Balance
6. NumOfProducts
7. HasCrCard
8. IsActiveMember
9. EstimatedSalary

---

## Output

The model returns a probability between **0 and 1**.

* Probability ≥ 0.5 → Customer is likely to churn.
* Probability < 0.5 → Customer is likely to stay.

---

## Model Architecture

* Input Layer: 9 Features
* Hidden Layer 1: Dense (ReLU)
* Hidden Layer 2: Dense (ReLU)
* Output Layer: Dense (Sigmoid)

---

## Loading the Model

```python
import tensorflow as tf

model = tf.keras.models.load_model("ann_model.h5")
```

---

## Example Prediction

```python
prediction = model.predict(input_data)

if prediction[0][0] > 0.5:
    print("Customer will leave.")
else:
    print("Customer will stay.")
```

---

## Dependencies

* TensorFlow
* NumPy

---

## License

This model is provided for educational and portfolio purposes.
