# 🚀 Execution Time Prediction using Polynomial Regression

This project focuses on predicting program execution time based on input parameters using **Polynomial Regression implemented from scratch**. By bypassing high-level libraries like `scikit-learn`, this project explores the underlying linear algebra of the **Normal Equation** and demonstrates how **feature engineering**—specifically interaction terms—is the key to modeling computational complexity.

---

## 🎯 Problem Statement

Predicting execution time is inherently non-linear because computational complexity usually follows $O(n \cdot m)$ or $O(n^2)$ patterns.

**Inputs:**
- `input_size (n)`: The scale of data being processed.
- `loop_iterations (m)`: The number of times the operation repeats.

**Output:**
- `execution_time`: The predicted time in milliseconds.

---

## 🧠 The Mathematical Approach

Instead of iterative Gradient Descent, this model uses the **Normal Equation** to find the weights $w$ that minimize the sum of squared errors analytically:

$$w = (X^T X)^{-1} X^T y$$

### 🔹 Implementation Detail
To handle potential multi-collinearity and ensure numerical stability, we utilize the **Moore-Penrose Pseudoinverse**:

```python
# Solving for weights using NumPy
w = np.linalg.pinv(X) @ y
```

---

## ⚙️ Feature Engineering Strategy

The core of this project is observing how the model's predictive power changes when we introduce **interaction terms** ($n \times m$).

### 🔴 Model 1: Without Interaction
Focuses on individual growth rates of parameters.
- **Features:** $[1, n, m, n^2, m^2]$
- **Assumption:** $n$ and $m$ contribute to time independently.

### 🟢 Model 2: With Interaction (Optimal)
Captures the multiplicative nature of nested loops.
- **Features:** $[1, n \times m, (n \times m)^2]$
- **Assumption:** Execution time depends on the product of inputs (e.g., $O(n \cdot m)$).

> **The Verdict:** Model 2 significantly outperforms Model 1 because execution time in real-world code is physically tied to the interaction of variables, not just their independent squares.

---

## 📊 Evaluation & Visualization

We evaluate the model using **Root Mean Square Error (RMSE)** and visualize the fit by comparing the Predicted Time vs. Actual Time.

### Performance Comparison
| Metric | Model 1 (No Interaction) | Model 2 (With Interaction) |
| :--- | :--- | :--- |
| **RMSE** | High | **Low (Near Zero)** |
| **Fit Quality** | Linear/Partial | **Highly Accurate** |

---

## 💻 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Misbah374/execution-time-prediction.git
cd execution-time-prediction
pip install numpy pandas matplotlib
python data_generator.py
jupyter notebook
```
