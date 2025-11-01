# Week 3 Homework - Problem 1.1-(c): Feed-Forward Network Parameters

## Problem Statement

Calculate the parameters for the Feed-Forward Network (FFN) in a Transformer encoder block.

**Given:**
- Model dimension: d_model = 512
- FFN hidden dimension: d_ff = 2048
- All linear layers include bias

**Questions:**
- **(c-i)** First linear layer parameters (512 → 2048)
- **(c-ii)** Second linear layer parameters (2048 → 512)
- **(c-iii)** Total FFN parameters

---

## Understanding the Feed-Forward Network (FFN)

### What is the FFN in a Transformer?

The **Feed-Forward Network** (FFN) is a critical component in each Transformer encoder block. After the multi-head attention mechanism processes the input, the FFN applies position-wise transformations to add non-linearity and increase the model's capacity to learn complex patterns.

**Key Characteristics:**
1. **Position-wise**: Applied independently to each position in the sequence
2. **Two-layer architecture**: Expands then contracts the dimensionality
3. **Non-linear activation**: Uses ReLU or GELU between the two layers
4. **Same across all positions**: Shared parameters for all sequence positions

### FFN Architecture

The FFN consists of **two linear transformations** with a non-linear activation in between:

```
FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
```

**Visual Architecture:**
```
Input (d_model = 512)
         ↓
   [Linear Layer 1]
   W₁: 512 × 2048
   b₁: 2048
         ↓
   [ReLU Activation]
   max(0, ·)
         ↓
   [Linear Layer 2]
   W₂: 2048 × 512
   b₂: 512
         ↓
Output (d_model = 512)
```

**Intuition:**
- **First layer (expand)**: Projects from 512 → 2048 dimensions, creating a richer representation space
- **Activation**: ReLU adds non-linearity, enabling complex pattern learning
- **Second layer (contract)**: Projects back from 2048 → 512 dimensions, preserving the model dimension

---

## Solution

### Step 1: Understanding Linear Layer Parameters

For a linear layer: **y = Wx + b**

**Parameters:**
- **Weight matrix W**: input_dim × output_dim
- **Bias vector b**: output_dim

**Total parameters** = (input_dim × output_dim) + output_dim

---

### (c-i) First Linear Layer Parameters (512 → 2048)

The first linear layer transforms from d_model = 512 to d_ff = 2048.

**Components:**

1. **Weight Matrix W₁:**
   - Dimensions: 512 × 2048
   - Number of parameters: 512 × 2048 = **1,048,576**

2. **Bias Vector b₁:**
   - Dimensions: 2048
   - Number of parameters: **2,048**

**Total for First Layer:**
```
Parameters = (Weight matrix) + (Bias vector)
           = 1,048,576 + 2,048
           = 1,050,624
```

**Answer (c-i): 1,050,624 parameters**

---

### (c-ii) Second Linear Layer Parameters (2048 → 512)

The second linear layer transforms from d_ff = 2048 back to d_model = 512.

**Components:**

1. **Weight Matrix W₂:**
   - Dimensions: 2048 × 512
   - Number of parameters: 2048 × 512 = **1,048,576**

2. **Bias Vector b₂:**
   - Dimensions: 512
   - Number of parameters: **512**

**Total for Second Layer:**
```
Parameters = (Weight matrix) + (Bias vector)
           = 1,048,576 + 512
           = 1,049,088
```

**Answer (c-ii): 1,049,088 parameters**

---

### (c-iii) Total FFN Parameters

The total FFN parameters is the sum of both linear layers.

**Calculation:**
```
Total FFN Parameters = (First Layer) + (Second Layer)
                     = 1,050,624 + 1,049,088
                     = 2,099,712
```

**Alternative Formula:**
```
Total = (d_model × d_ff + d_ff) + (d_ff × d_model + d_model)
      = (512 × 2048 + 2048) + (2048 × 512 + 512)
      = (1,048,576 + 2,048) + (1,048,576 + 512)
      = 1,050,624 + 1,049,088
      = 2,099,712
```

**Answer (c-iii): 2,099,712 parameters**

---

## Summary Table

| Component | Calculation | Parameters |
|-----------|-------------|------------|
| **First Linear Layer** | | |
| - Weight W₁ (512 × 2048) | 512 × 2048 | 1,048,576 |
| - Bias b₁ | 2048 | 2,048 |
| **First Layer Total** | | **1,050,624** |
| | | |
| **Second Linear Layer** | | |
| - Weight W₂ (2048 × 512) | 2048 × 512 | 1,048,576 |
| - Bias b₂ | 512 | 512 |
| **Second Layer Total** | | **1,049,088** |
| | | |
| **Total FFN Parameters** | 1,050,624 + 1,049,088 | **2,099,712** |

---

## Key Insights

### 1. FFN Dominates Transformer Parameters

The FFN contains **significantly more parameters** than the multi-head attention mechanism (from previous problems).

**Comparison:**
- Multi-head attention (8 heads): ~1.05M parameters
- FFN: ~2.1M parameters
- **FFN has ~2× more parameters**

This explains why FFNs are crucial for the Transformer's representational capacity!

### 2. Expansion Factor

The FFN uses an **expansion factor** of 4:
```
d_ff / d_model = 2048 / 512 = 4
```

**Standard practice**: d_ff = 4 × d_model
- This 4× expansion creates a richer intermediate representation space
- Allows the model to learn more complex non-linear transformations

### 3. Why Two Layers?

**First layer (expand):**
- Projects to higher dimension (512 → 2048)
- Creates a richer feature space
- Allows for more expressive transformations

**Second layer (contract):**
- Projects back to original dimension (2048 → 512)
- Maintains consistency with model architecture
- Preserves residual connection compatibility

**Activation in between:**
- ReLU or GELU provides non-linearity
- Without it, two linear layers = one linear layer (no benefit)
- Non-linearity enables learning of complex patterns

### 4. Parameter Efficiency

Notice the weight matrices have the **same number of parameters**:
- W₁: 512 × 2048 = 1,048,576
- W₂: 2048 × 512 = 1,048,576

The difference in total parameters comes from the **bias vectors**:
- b₁: 2048 (larger)
- b₂: 512 (smaller)

---

## Connection to Previous Problems

If you solved Problem 1.1-(a) and (b) about multi-head attention:

**Complete Encoder Block Parameters:**
```
Encoder Block = Multi-Head Attention + FFN + Layer Norms
              ≈ 1.05M + 2.1M + small
              ≈ 3.15M parameters per block

For 6 encoder blocks:
Total ≈ 6 × 3.15M ≈ 18.9M parameters
```

The FFN is the **largest component** in each Transformer encoder block!

---

## Verification

Let's verify our calculation using the general formula:

**General Formula for FFN:**
```
FFN_params = (d_model × d_ff + d_ff) + (d_ff × d_model + d_model)
           = d_model × d_ff + d_ff + d_ff × d_model + d_model
           = 2 × d_model × d_ff + d_ff + d_model
```

**Substituting values:**
```
FFN_params = 2 × 512 × 2048 + 2048 + 512
           = 2 × 1,048,576 + 2048 + 512
           = 2,097,152 + 2048 + 512
           = 2,099,712 ✓
```

**Matches our answer!**

---

## Final Answers

**(c-i) First linear layer (512 → 2048):**
```
Answer: 1,050,624 parameters
```

**(c-ii) Second linear layer (2048 → 512):**
```
Answer: 1,049,088 parameters
```

**(c-iii) Total FFN parameters:**
```
Answer: 2,099,712 parameters
```

---

## Educational Notes

### Why is the FFN Important?

1. **Non-linearity**: Provides essential non-linear transformations
2. **Capacity**: Contains majority of parameters in each encoder block
3. **Position-wise**: Processes each position independently (unlike attention)
4. **Complementary**: Works with attention to capture both global (attention) and local (FFN) patterns

### Computational Perspective

**Forward Pass:**
- Input: [batch_size, seq_len, 512]
- After Layer 1: [batch_size, seq_len, 2048]
- After ReLU: [batch_size, seq_len, 2048]
- After Layer 2: [batch_size, seq_len, 512]
- Output: [batch_size, seq_len, 512]

**Memory:**
- Intermediate activations temporarily expand to 2048 dimensions
- Need to store activations for backpropagation
- Memory bottleneck in long sequences!

---

## Practice Questions

To deepen your understanding:

1. **Question**: If we change d_ff to 4096 (8× expansion), how many FFN parameters would we have?

2. **Question**: What percentage of total Transformer parameters does the FFN represent?

3. **Question**: Why do we expand then contract, rather than just use one layer?

4. **Question**: What would happen if we removed the ReLU activation?

Think about these questions to solidify your understanding!

---

**Great job working through this problem! The FFN is a crucial component of the Transformer architecture, and understanding its parameter count helps you appreciate its computational requirements.**
