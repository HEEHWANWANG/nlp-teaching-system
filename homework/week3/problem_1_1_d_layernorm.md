# Problem 1.1-(d): LayerNorm Parameters in Transformer Encoder

## Given Information
- Model dimension: **d_model = 512**
- Number of LayerNorm layers per encoder block: **2**
- Each LayerNorm has learnable parameters: γ (gamma/scale) and β (beta/offset)

---

## Part 1: Understanding Layer Normalization (LayerNorm)

### What is LayerNorm?

**Layer Normalization** is a normalization technique that normalizes inputs across the features (rather than across the batch like Batch Normalization). It helps stabilize training and allows for faster convergence.

### How LayerNorm Works

For an input vector **x** of dimension d_model, LayerNorm performs:

```
1. Calculate mean: μ = (1/d_model) × Σ x_i
2. Calculate variance: σ² = (1/d_model) × Σ(x_i - μ)²
3. Normalize: x̂_i = (x_i - μ) / √(σ² + ε)
4. Scale and shift: y_i = γ_i × x̂_i + β_i
```

Where ε is a small constant (e.g., 1e-5) for numerical stability.

### Learnable Parameters: γ (Gamma) and β (Beta)

#### γ (Gamma) - Scale Parameter
- **Purpose**: Controls the scale/variance of each feature after normalization
- **Dimension**: d_model (one scale value per feature dimension)
- **Initialization**: Usually initialized to 1
- **Role**: Allows the model to learn the optimal scale for each feature

#### β (Beta) - Offset/Bias Parameter
- **Purpose**: Controls the mean/center of each feature after normalization
- **Dimension**: d_model (one offset value per feature dimension)
- **Initialization**: Usually initialized to 0
- **Role**: Allows the model to learn the optimal center for each feature

### Why γ and β are Important

After normalization, all features have mean=0 and variance=1. However, this might not be optimal for the model. The learnable parameters γ and β give the model flexibility to:
- Undo the normalization if needed (by learning γ=σ, β=μ)
- Learn the best scale and shift for each feature dimension
- Adapt the normalization to the specific task

---

## Part 2: Calculate Parameters for ONE LayerNorm Layer

### Step 1: Parameters for γ (Scale)
```
Number of γ parameters = d_model
                      = 512
```

### Step 2: Parameters for β (Offset)
```
Number of β parameters = d_model
                      = 512
```

### Step 3: Total Parameters for One LayerNorm
```
Total parameters per LayerNorm = γ parameters + β parameters
                                = 512 + 512
                                = 1,024 parameters
```

**Formula:**
```
Parameters per LayerNorm = 2 × d_model
                         = 2 × 512
                         = 1,024
```

---

## Part 3: Calculate Parameters for TWO LayerNorm Layers

### LayerNorm Locations in Transformer Encoder Block

A standard Transformer encoder block has **2 LayerNorm layers**:

1. **LayerNorm 1**: After Multi-Head Self-Attention + Residual Connection
   - Located between attention and feed-forward network

2. **LayerNorm 2**: After Feed-Forward Network + Residual Connection
   - Located at the end of the encoder block

### Visual Structure:
```
Input (d_model = 512)
    ↓
Multi-Head Self-Attention
    ↓
Add & Normalize  ← LayerNorm 1 (1,024 parameters)
    ↓
Feed-Forward Network
    ↓
Add & Normalize  ← LayerNorm 2 (1,024 parameters)
    ↓
Output (d_model = 512)
```

### Step-by-Step Calculation:

#### LayerNorm 1 (After Multi-Head Attention):
```
Parameters = 2 × d_model
          = 2 × 512
          = 1,024
```
- γ₁: 512 parameters
- β₁: 512 parameters

#### LayerNorm 2 (After Feed-Forward Network):
```
Parameters = 2 × d_model
          = 2 × 512
          = 1,024
```
- γ₂: 512 parameters
- β₂: 512 parameters

#### Total for 2 LayerNorm Layers:
```
Total LayerNorm parameters = LayerNorm 1 + LayerNorm 2
                           = 1,024 + 1,024
                           = 2,048 parameters
```

---

## Part 4: Complete Solution Summary

### Detailed Breakdown:

| Component | γ (Scale) | β (Offset) | Total |
|-----------|-----------|------------|-------|
| **LayerNorm 1** | 512 | 512 | **1,024** |
| **LayerNorm 2** | 512 | 512 | **1,024** |
| **Total** | **1,024** | **1,024** | **2,048** |

### Calculation Steps:

**Step 1:** Calculate parameters for one LayerNorm
```
Parameters per LayerNorm = γ + β
                         = d_model + d_model
                         = 512 + 512
                         = 1,024
```

**Step 2:** Calculate total for 2 LayerNorm layers
```
Total parameters = 2 × (Parameters per LayerNorm)
                 = 2 × 1,024
                 = 2,048
```

**Alternative formula:**
```
Total parameters = Number of LayerNorms × 2 × d_model
                 = 2 × 2 × 512
                 = 2,048
```

---

## Final Answer

### Problem 1.1-(d): LayerNorm Parameters

**Given:**
- d_model = 512
- Number of LayerNorm layers = 2

**Solution:**

**For ONE LayerNorm layer:**
- γ (scale) parameters: 512
- β (offset) parameters: 512
- **Total per LayerNorm: 1,024 parameters**

**For TWO LayerNorm layers in encoder block:**
- LayerNorm 1 (after attention): 1,024 parameters
- LayerNorm 2 (after FFN): 1,024 parameters
- **Total LayerNorm parameters: 2,048 parameters**

**Formula:**
```
Total LayerNorm parameters = 2 × 2 × d_model
                           = 2 × 2 × 512
                           = 2,048 parameters
```

---

## Key Takeaways

1. **LayerNorm normalizes across features** (not across batch)
2. **Each LayerNorm has 2 learnable parameter vectors**: γ and β
3. **Each parameter vector has dimension d_model**
4. **Parameters per LayerNorm = 2 × d_model**
5. **Transformer encoder has 2 LayerNorm layers**
6. **Total = 2 × (2 × d_model) = 2,048 parameters**

---

## Comparison with Other Components

For context, here's how LayerNorm parameters compare to other parts of the Transformer encoder block (d_model = 512):

| Component | Parameters | Percentage |
|-----------|-----------|------------|
| Multi-Head Attention (8 heads) | 1,048,576 | 99.6% |
| Feed-Forward Network | 2,099,200 | - |
| **LayerNorm (2 layers)** | **2,048** | **0.0006%** |

**Observation:** LayerNorm has very few parameters compared to attention and FFN, but plays a crucial role in stabilizing training!

---

## Educational Notes

### Why is LayerNorm Important?

1. **Training Stability**: Reduces internal covariate shift
2. **Faster Convergence**: Helps gradients flow better
3. **Less Sensitive to Initialization**: Normalizes activations
4. **Works Well with Transformers**: Unlike BatchNorm, doesn't depend on batch size

### LayerNorm vs Batch Normalization

| Aspect | LayerNorm | BatchNorm |
|--------|-----------|-----------|
| Normalization axis | Across features | Across batch |
| Dependency | Independent samples | Needs batch statistics |
| Best for | NLP, variable lengths | Computer Vision |
| Parameters | 2 × d_model | 2 × d_model |

---

## Practice Exercise

**Try calculating LayerNorm parameters for different configurations:**

1. If d_model = 768 (BERT-base), what are the LayerNorm parameters?
   - Answer: 2 × 2 × 768 = 3,072

2. If d_model = 1024 (BERT-large), what are the LayerNorm parameters?
   - Answer: 2 × 2 × 1024 = 4,096

3. If a model has 6 encoder blocks, each with 2 LayerNorms, total LayerNorm parameters?
   - Answer: 6 × 2,048 = 12,288 (for d_model = 512)

---

**Document created for educational purposes**
**NLP Teaching System - Week 3 Homework**
