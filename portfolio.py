# -*- coding: utf-8 -*-

import streamlit as st

# Page config
st.set_page_config(page_title="ML Portfolio", layout="wide")

# Custom CSS (for styling cards)
st.markdown("""
<style>
.card {
    background-color: #FFFFFF;
    color: #1E293B;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.card:hover {
    transform: scale(1.02);
    transition: 0.3s;
}
.title {
    font-size: 18px;
    font-weight: 600;
}
.desc {
    font-size: 14px;
    color: #64748B;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("Akshay Atanure", text_alignment='center')
st.header('Data Scientist | Machine Learning | Python | Risk Modeling | Attrition Detection | MLOps', text_alignment='center')
st.write("Building end-to-end ML systems for real-world problem solving")

st.info("💡 Click on any project link to explore the live application")

st.markdown("---")

# Layout
col1, col2 = st.columns(2)

# ---------------- CARD 1 ----------------
with col1:
    st.markdown("""
    <div class="card">
        <div class="title">💳 Credit Risk Decision System</div>
        <div class="desc">
        Predicts loan default risk using ML pipeline.<br>
        Handles imbalanced data using PR-AUC & Recall.<br>
        Built with sklearn + Streamlit deployment.
        </div>
        <br>
        <a href="https://creditriskdecisionsystem.streamlit.app" target="_blank">
        🔗 Open Live App
        </a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CARD 2 ----------------
with col2:
    st.markdown("""
    <div class="card">
        <div class="title">🏢🚶🚪📉 Employee Attrition</div>
        <div class="desc">
        Predicts Attrition rate using employee data.<br>
        Includes feature engineering and risk scoring.<br>
        Evaluated using precision-recall metrics.
        </div>
        <br>
        <a href="https://employee-attrition-pred-model.streamlit.app/" target="_blank">
        🔗 Open App
        </a>
    </div>
    """, unsafe_allow_html=True)

# Second row
col3, col4 = st.columns(2)

# ---------------- CARD 3 ----------------
with col3:
    st.markdown("""
    <div class="card">
        <div class="title">💰 Salary Prediction</div>
        <div class="desc">
        Predicts salary using regression models.<br>
        Feature-based prediction with ML pipeline.
        </div>
        <br>
        <a href="https://salary-predictionsystem.streamlit.app/" target="_blank">
        🔗 Open App
        </a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CARD 4 ----------------
with col4:
    st.markdown("""
    <div class="card">
        <div class="title">🏏 IPL Data Analysis and Batsman Performance predictor</div>
        <div class="desc">
        Interactive dashboard for IPL player stats.<br>
        Visual insights and performance tracking.
        </div>
        <br>
        <a href="https://bpipredictor-qqbg8ro8ax6te7n4oo4zbe.streamlit.app/" target="_blank">
        🔗 Open App
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Footer
st.write("📌 Tech Stack: Python | Pandas | Numpy | Scikit-learn | XGBoost | LightGBM | Plotly | Altair | Streamlit")
