# Mathematics of Program Execution Time Prediction

This document summarizes the **mathematics behind the models** used for predicting execution time based on input size (`n`) and loop iterations (`m`).

---

## 1. Notation

| Symbol | Meaning |
|--------|---------|
| `n` | Input size |
| `m` | Loop iterations |
| `x1` | `n` (input size) |
| `x2` | `m` (loop iterations) |
| `x1^2, x2^2` | Polynomial terms |
| `x1 * x2` | Interaction term |
| `y` | Execution time |
| `\hat{y}` | Predicted execution time |
| `w0, w1, ...` | Model coefficients |

---

## 2. Model 1: Polynomial WITHOUT Interaction

**Equation:**

$$
y = w_0 + w_1 x_1 + w_2 x_2 + w_3 x_1^2 + w_4 x_2^2
$$

**Design Matrix:**

$$
X =
\begin{bmatrix}
1 & x_1 & x_2 & x_1^2 & x_2^2 \\
1 & x_1 & x_2 & x_1^2 & x_2^2 \\
\vdots & \vdots & \vdots & \vdots & \vdots
\end{bmatrix}
$$

**Coefficient Calculation (Normal Equation):**

$$
w = (X^T X)^{-1} X^T y
$$

**Prediction:**

$$
\hat{y} = X w
$$

---

## 3. Model 2: Polynomial WITH Interaction

**Equation:**

$$
y = w_0 + w_1 (x_1 x_2) + w_2 (x_1 x_2)^2
$$

**Design Matrix:**

$$
X =
\begin{bmatrix}
1 & x_1 x_2 & (x_1 x_2)^2 \\
1 & x_1 x_2 & (x_1 x_2)^2 \\
\vdots & \vdots & \vdots
\end{bmatrix}
$$

**Coefficient Calculation:**

$$
w = (X^T X)^{-1} X^T y
$$

**Prediction:**

$$
\hat{y} = X w
$$

---

## 4. Model Comparison: Linear vs Polynomial on Interaction

- **Linear Fit:**

$$
y \approx w_0 + w_1 (x_1 x_2)
$$

- **Polynomial Fit:**

$$
y \approx w_0 + w_1 (x_1 x_2) + w_2 (x_1 x_2)^2
$$

**Purpose:** To visualize how **polynomial terms improve fit** over a simple linear model.

---

## 5. Mean Squared Error (MSE)

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

- Used to evaluate **training error** for all models.  

---

## 6. Notes / Key Points

- Interaction terms capture **combined effect** of multiple features.  
- Squared terms capture **non-linear effect** of a feature.  
- Normal equation gives an **exact solution** for linear regression.  
- Libraries like **scikit-learn** handle computation efficiently for large datasets or more complex models.

---

## 7. Mathematics Behind the Plots

The plots visualize how **linear and polynomial models fit the data** by mapping the relationship between input complexity and execution time.

### 🔹 1. Data Sorting for Smooth Plotting
To ensure the regression curves are continuous and smooth, we define the **interaction term** $x_i$ and sort the dataset:

Let:
$$x_i = n_i \cdot m_i$$
(where $n$ is input size and $m$ is iterations) and $y_i$ be the actual execution time.

We sort the data such that:
$$x_1 \le x_2 \le \dots \le x_n$$

---

### 🔹 2. Linear Fit (Interaction Only)
**Design Matrix ($X_{\text{linear}}$):**
We construct the matrix for all $n$ rows. To render correctly in GitHub, we use quadruple backslashes for row breaks:

$$
X_{\text{linear}} = \begin{pmatrix} 1 & x_1 \\\\ 1 & x_2 \end{pmatrix}
$$

**Coefficients ($w_{\text{linear}}$):**
Solved using the Normal Equation via the Pseudo-inverse:

$$w_{\text{linear}} = (X_{\text{linear}}^T X_{\text{linear}})^{-1} X_{\text{linear}}^T y$$

---

### 🔹 3. Polynomial Fit (Degree 2)
**Design Matrix ($X_{\text{poly}}$):**
We add a squared term to the features to capture non-linear growth:

$$
X_{\text{poly}} = \begin{pmatrix} 1 & x_1 & x_1^2 \\\\ 1 & x_2 & x_2^2 \end{pmatrix}
$$

**Coefficients ($w_{\text{poly}}$):**

$$w_{\text{poly}} = (X_{\text{poly}}^T X_{\text{poly}})^{-1} X_{\text{poly}}^T y$$

**Prediction:**
$$\hat{y}_i^{\text{poly}} = w_0 + w_1 x_i + w_2 x_i^2$$

---

### 🔹 4. Purpose of the Plot
The visual comparison allows us to see the model's "intent":

* **Scatter Points:** $(x_i, y_i)$ represent the raw, measured execution time.
* **Linear Curve:** $\hat{y}_i^{\text{linear}}$ shows the best straight-line approximation.
* **Polynomial Curve:** $\hat{y}_i^{\text{poly}}$ shows how the model adapts to the "bend" in the data.

> **Key Insight:** Visual comparison shows how **polynomial terms capture the inherent curvature** and hardware overhead that linear regression simply cannot see.
