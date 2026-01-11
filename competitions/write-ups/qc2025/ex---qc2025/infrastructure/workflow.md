---
layout: page
title: QC2025 Workflow
---


[← Infrastructure]({{ '/competitions/write-ups/qc2025/ex---qc2025/infrastructure/' | relative_url }}) | [Execution]({{ '/competitions/write-ups/qc2025/ex---qc2025/' | relative_url }})

---

## Approach 1: Stacked Model

### Step 1: XGBoost Base

```python
xgb_model = xgb.XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=4,
    random_state=4
)
```

### Step 2: Neural Net on Residuals

```python
resid_train = train - pred_xgb_train

nn = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)
])
```

### Step 3: LightGBM (Parallel)

```python
lgb_model = LGBMRegressor(n_estimators=200, learning_rate=0.04, max_depth=3)
```

`max_depth=3` prevents overfitting.

### Step 4: Meta-Learner

Stack predictions and apply final model:

| Target | Meta-Learner |
|--------|--------------|
| Y1 | Ridge (alpha=1) |
| Y2 | CatBoost (non-linear) |

```python
meta_X_val = np.vstack([pred_final, pred_lgb_val]).T

meta_model_Y1 = Ridge(alpha=1)
meta_model_Y2 = CatBoostRegressor(iterations=5000, learning_rate=0.1, depth=4)
```

---

## Approach 2: Penalized Regression + NN

1. Run penalized regression (Lasso vs Ridge) on all features excluding O and P
2. No lags included (Granger Causality showed no significance at 5% level)
3. Neural net on residuals for remaining non-linearity

Compare Lasso vs Ridge performance including NN, select better overall.
