---
layout: page
title: QC2025 Part 1 Infrastructure
---


[← Overview]({{ '/competitions/write-ups/qc2025/ov---qc2025/' | relative_url }}) | [Algorithm]({{ '/competitions/write-ups/qc2025/ov---qc2025/algorithm/' | relative_url }}) | [Execution]({{ '/competitions/write-ups/qc2025/ex---qc2025/' | relative_url }})

---

## Feature Engineering

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

Track mean, std, z-score across multiple windows:

```python
wins = [3, 7, 21, 63]
for w in wins:
    for col in feature_cols:
        df[f'{col}_mean{w}'] = df[col].rolling(w, min_periods=1).mean()
        df[f'{col}_std{w}']  = df[col].rolling(w, min_periods=1).std()
        df[f'{col}_z{w}']    = (df[col] - df[f'{col}_mean{w}']) / (df[f'{col}_std{w}'] + 1e-9)
```

---

## SHAP Analysis

```python
model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=0)
model.fit(X_train_s, y_train, eval_set=[(X_test_s, y_test)], verbose=False)
explainer = shap.Explainer(model, X_train_s)
shap_values = explainer(X_test_s)
```

**Parameters:** `n_estimators=200, learning_rate=0.05` optimal for small training data. Used `TimeSeriesSplit` to average SHAP values across folds.

---

## Additional Tests

| Test | Purpose |
|------|---------|
| ACF/PACF | Applied to Y1 and Y2 |
| Lasso Coefficients | Linear association |
| Granger Causality | Variable correlations at lags up to 79999 |
| Periodogram | Seasonality patterns in Y1 & Y2 |
| PCA | Feature importance |

[Workflow Details]({{ '/competitions/write-ups/qc2025/ex---qc2025/infrastructure/workflow/' | relative_url }})
