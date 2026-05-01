import streamlit as st

# Function to assign color
def get_color(value):
    if value > 0.90:
        return "green"
    elif value > 0.75:
        return "orange"
    else:
        return "red"

# Sample values (replace with your actual results)
final_score = 0.92
privacy_score = 0.88
recall = 0.94
fpr = 0.06
best_model = "AL (Entropy + FedProx)"

# Title
st.markdown("<h1 style='text-align: center;'>🚀 Intrusion Detection System Dashboard</h1>", unsafe_allow_html=True)

# Create columns
col1, col2, col3, col4, col5 = st.columns(5)

# Final Score
col1.markdown(f"""
<h3>🏆 Final Score</h3>
<h2 style='color:{get_color(final_score)}'>{final_score}</h2>
""", unsafe_allow_html=True)

# Best Model
col2.markdown(f"""
<h3>🤖 Best Model</h3>
<h2>{best_model}</h2>
""", unsafe_allow_html=True)

# Privacy Score
col3.markdown(f"""
<h3>🔐 Privacy</h3>
<h2 style='color:{get_color(privacy_score)}'>{privacy_score}</h2>
""", unsafe_allow_html=True)

# Recall
col4.markdown(f"""
<h3>🎯 Recall</h3>
<h2 style='color:{get_color(recall)}'>{recall}</h2>
""", unsafe_allow_html=True)

# FPR
col5.markdown(f"""
<h3>⚠️ FPR</h3>
<h2 style='color:{get_color(fpr)}'>{fpr}</h2>
""", unsafe_allow_html=True)

# Insight Box
st.markdown("""
---
### 💡 Insight
**Entropy-based Active Learning with FedProx provides the best balance between accuracy and privacy.**
""")