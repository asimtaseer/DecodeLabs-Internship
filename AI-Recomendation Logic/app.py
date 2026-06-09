import json
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ─────────────────────────────────────────────
#  Page configuration
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  Custom CSS – modern, clean, beginner-friendly
# ─────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    /* ── Global ── */
    * { font-family: 'Inter', sans-serif; }
    html, body, [class*="css"] {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #e2e8f0;
    }

    /* Main container */
    .block-container { padding: 2.5rem 1.5rem 4rem; max-width: 860px; margin: auto; }

    /* ── Hero header ── */
    .hero {
        text-align: center;
        padding: 2.2rem 1rem 1.8rem;
        background: linear-gradient(135deg, rgba(99,102,241,0.18), rgba(139,92,246,0.14));
        border: 1px solid rgba(139,92,246,0.35);
        border-radius: 20px;
        margin-bottom: 2rem;
        backdrop-filter: blur(12px);
    }
    .hero h1 {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #a78bfa, #818cf8, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 0.4rem;
    }
    .hero p { color: #94a3b8; font-size: 1rem; margin: 0; }

    /* ── Input label ── */
    label { color: #c4b5fd !important; font-weight: 600 !important; font-size: 0.95rem !important; }

    /* ── Text input ── */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(139,92,246,0.45) !important;
        border-radius: 12px !important;
        color: #f1f5f9 !important;
        padding: 0.7rem 1rem !important;
        font-size: 1rem !important;
        transition: border-color 0.2s;
    }
    .stTextInput > div > div > input:focus {
        border-color: #818cf8 !important;
        box-shadow: 0 0 0 3px rgba(129,140,248,0.25) !important;
    }

    /* ── Button ── */
    .stButton > button {
        width: 100%;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 700;
        color: #fff !important;
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        border: none !important;
        border-radius: 12px !important;
        cursor: pointer;
        transition: transform 0.15s, box-shadow 0.15s;
        margin-top: 0.5rem;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(99,102,241,0.45) !important;
    }

    /* ── Result card ── */
    .result-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(135deg, rgba(99,102,241,0.14), rgba(139,92,246,0.10));
        border: 1px solid rgba(139,92,246,0.30);
        border-radius: 14px;
        padding: 1rem 1.4rem;
        margin-bottom: 0.85rem;
        backdrop-filter: blur(8px);
        transition: transform 0.15s;
    }
    .result-card:hover { transform: translateX(4px); }
    .card-rank {
        font-size: 1.6rem;
        font-weight: 800;
        color: rgba(167,139,250,0.5);
        min-width: 2.2rem;
        text-align: center;
    }
    .card-name {
        flex: 1;
        padding: 0 1rem;
        font-size: 1.05rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    .card-score {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: #fff;
        font-size: 0.88rem;
        font-weight: 700;
        padding: 0.3rem 0.75rem;
        border-radius: 999px;
        white-space: nowrap;
    }

    /* ── Section title ── */
    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #a78bfa;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 1.8rem 0 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #475569;
        font-size: 0.82rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255,255,255,0.07);
    }

    /* hide Streamlit default elements */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────
#  Data loading
# ─────────────────────────────────────────────
@st.cache_data
def load_items(path: str = "items.json"):
    """Load learning items from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ─────────────────────────────────────────────
#  Core recommendation function (reusable)
# ─────────────────────────────────────────────
def recommend(user_input: str, items: list, top_n: int = 5) -> list[dict]:
    """
    Content-based recommendation using TF-IDF + Cosine Similarity.

    Parameters
    ----------
    user_input : str   – free-text interests entered by the user
    items      : list  – list of dicts with 'name' and 'tags' keys
    top_n      : int   – number of recommendations to return

    Returns
    -------
    list of dicts: [{"name": ..., "score": ...}, ...]
    """
    if not user_input.strip():
        return []

    # Build corpus: index 0 = user query, rest = item tags
    tag_corpus = [user_input] + [item["tags"] for item in items]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(tag_corpus)

    # Cosine Similarity between user query (row 0) and all items
    user_vector = tfidf_matrix[0]
    item_vectors = tfidf_matrix[1:]
    similarity_scores = cosine_similarity(user_vector, item_vectors).flatten()

    # Rank by score (descending)
    ranked_indices = np.argsort(similarity_scores)[::-1][:top_n]

    results = []
    for idx in ranked_indices:
        score = float(similarity_scores[idx])
        if score > 0:  # only include items with any relevance
            results.append({"name": items[idx]["name"], "score": round(score, 4)})

    return results


# ─────────────────────────────────────────────
#  UI – Hero section
# ─────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <h1>🎯 AI-Powered Learning Assistant</h1>
        <p>Discover personalised learning resources powered by Content-Based Filtering</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Load dataset
try:
    items = load_items("items.json")
except FileNotFoundError:
    st.error("❌ `items.json` not found. Make sure it is in the same folder as `app.py`.")
    st.stop()

# ─────────────────────────────────────────────
#  UI – Input section
# ─────────────────────────────────────────────
user_input = st.text_input(
    "💡 Enter your interests",
    placeholder="e.g.  python  machine learning  neural networks  ai",
    help="Type keywords that describe what you want to learn. Separate with spaces.",
)

get_recs = st.button("🚀  Get Recommendations")

# ─────────────────────────────────────────────
#  UI – Results section
# ─────────────────────────────────────────────
if get_recs:
    if not user_input.strip():
        st.warning("⚠️ Please enter at least one interest keyword before clicking the button.")
    else:
        with st.spinner("Analysing your interests …"):
            results = recommend(user_input, items, top_n=5)

        if not results:
            st.info("🔍 No matching items found. Try different or broader keywords.")
        else:
            st.markdown(
                '<div class="section-title">✨ Top Recommendations for You</div>',
                unsafe_allow_html=True,
            )

            for rank, item in enumerate(results, start=1):
                score_pct = f"{item['score'] * 100:.1f}%"
                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="card-rank">#{rank}</div>
                        <div class="card-name">{item['name']}</div>
                        <div class="card-score">Match: {score_pct}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown(
                f"<p style='color:#64748b; font-size:0.82rem; margin-top:0.5rem;'>"
                f"Showing top {len(results)} recommendations out of {len(items)} available items.</p>",
                unsafe_allow_html=True,
            )

# show a hint when idle
elif not get_recs:
    st.markdown(
        """
        <div style='text-align:center; margin-top:3rem; color:#475569;'>
            <p style='font-size:3rem; margin:0;'>🧠</p>
            <p style='font-size:1rem; margin-top:0.5rem;'>
                Enter your interests above and hit <strong style='color:#a78bfa;'>Get Recommendations</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
#  Footer
# ─────────────────────────────────────────────
st.markdown(
    "<div class='footer'>Built with ❤️ using Streamlit · TF-IDF · Cosine Similarity &nbsp;|&nbsp; DecodeLabs Internship</div>",
    unsafe_allow_html=True,
)
