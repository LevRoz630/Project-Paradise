---
layout: page
title: QC2025 Infrastructure
---


[← Execution]({{ '/competitions/write-ups/qc2025/ex---qc2025/' | relative_url }}) | **[Workflow]({{ '/competitions/write-ups/qc2025/ex---qc2025/infrastructure/workflow/' | relative_url }})**

---

## Part 1: Feature Selection

Main focus on feature selection using lags, Fourier features, SHAP Explainer and TreeExplainer models.

### Fourier Features

```python
def add_fouriers(df, t_col='time', periods=[7, 30, 365], harmonics=3):
    out = df.copy()
    for p in periods:
        for k in range(1, harmonics + 1):
            out[f'fourier_P{p}_k{k}_sin'] = np.sin(2 * np.pi * k * out[t_col] / p)
            out[f'fourier_P{p}_k{k}_cos'] = np.cos(2 * np.pi * k * out[t_col] / p)
    return out
```

### Rolling Windows

Track 3 main characteristics: `mean()`, `std()`, `z_score`:

```python
feature_cols = [c for c in df.columns if c not in ['time', 'Y1', 'Y2']]
wins = [3, 7, 21, 63]

for w in wins:
    for col in feature_cols:
        g = df[col]
        df[f'{col}_mean{w}'] = g.transform(lambda x: x.rolling(w, min_periods=1).mean())
        df[f'{col}_std{w}']  = g.transform(lambda x: x.rolling(w, min_periods=1).std())
        df[f'{col}_z{w}']    = (df[col] - df[f'{col}_mean{w}']) / (df[f'{col}_std{w}'] + 1e-9)
```

### SHAP Analysis

```python
model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=0)
model.fit(X_train_s, y_train, eval_set=[(X_test_s, y_test)], verbose=False)
explainer = shap.Explainer(model, X_train_s)
shap_values = explainer(X_test_s)
```

**Note:** `n_estimators=200, learning_rate=0.05` was optimal given small number of training rows. Used `TimeSeriesSplit` cross-validator to average SHAP values across folds.

---

## Additional Tests

- **ACF and PACF** tests on Y1 and Y2
- **Lasso coefficients** for linear association
- **Granger Causality Test** for variable correlations at various lags (up to 79999)
- **Periodogram** for seasonality patterns in Y1 & Y2
- **PCA tests** for feature importance
