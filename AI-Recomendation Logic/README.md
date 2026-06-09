# 🎯 AI-Powered Learning Assistant
### Content-Based Recommendation System · DecodeLabs Internship

A clean, interactive Streamlit web application that recommends personalised learning resources based on your interests using **Content-Based Filtering** (TF-IDF Vectorization + Cosine Similarity).

---

## 📌 Project Overview

| Property | Detail |
|---|---|
| **Type** | Content-Based Recommendation System |
| **Frontend** | Streamlit |
| **Core Algorithm** | TF-IDF Vectorization + Cosine Similarity |
| **Dataset** | `items.json` (20 learning resources) |
| **Language** | Python 3.9+ |

---

## 🗂️ Project Structure

```
AI-Recomendation Logic/
 ├── app.py            ← Main Streamlit application
 ├── items.json        ← Dataset (20 learning items with tags)
 ├── requirements.txt  ← Python dependencies
 └── README.md         ← This file
```

---

## ⚙️ How It Works

```
User Types Interests
        │
        ▼
 TF-IDF Vectorization
 (converts text → numerical vectors)
        │
        ▼
 Cosine Similarity
 (measures closeness between user query & item tags)
        │
        ▼
 Ranked Top-5 Recommendations
```

1. **Load Dataset** – reads all items from `items.json`
2. **TF-IDF** – converts the user's input and every item's tags into weighted term vectors
3. **Cosine Similarity** – computes how closely each item matches the user query
4. **Ranking** – sorts by similarity score and returns the top 5

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run app.py
```

### 3. Open in browser
Streamlit will automatically open `http://localhost:8501`

---

## 💡 Usage

1. Type your interests in the text box
   > Example: `python machine learning neural networks`
2. Click **Get Recommendations**
3. View personalized, ranked results

### Sample Output
```
#1  Machine Learning Fundamentals      Match: 82.4%
#2  Python for AI                      Match: 79.1%
#3  Deep Learning with TensorFlow      Match: 71.3%
#4  Statistics for Machine Learning    Match: 63.0%
#5  Feature Engineering                Match: 55.8%
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `scikit-learn` | TF-IDF & Cosine Similarity |
| `numpy` | Numerical operations |

---

## 🔑 Key Function

```python
recommend(user_input, items, top_n=5)
```

| Parameter | Type | Description |
|---|---|---|
| `user_input` | `str` | Keywords entered by the user |
| `items` | `list` | Items loaded from `items.json` |
| `top_n` | `int` | Number of results to return (default: 5) |

**Returns:** list of `{"name": str, "score": float}` dicts, sorted by relevance.

---

## 📝 Dataset Format (`items.json`)

```json
[
  {
    "name": "Machine Learning Fundamentals",
    "tags": "machine learning algorithms supervised unsupervised ..."
  }
]
```

To add more items, simply append new objects to `items.json` — no code changes required.

---

*Built with ❤️ using Streamlit · TF-IDF · Cosine Similarity | DecodeLabs Internship*
