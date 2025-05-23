import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_utils import validate_data
from analysis import analyze_margins
from dashboard_planner import suggest_dashboard

st.set_page_config(page_title="Finance Insight Bot", layout="wide")
st.title("📊 Finance Insight & Dashboard Assistant")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("🔍 Data Validation Report")
    validation_report = validate_data(df)
    st.write(validation_report)

    st.subheader("💡 Margin & KPI Analysis")
    margin_insights = analyze_margins(df)
    st.write(margin_insights)

    st.subheader("🧠 GPT-Based Dashboard Suggestion")
    dashboard_idea = suggest_dashboard(df)
    st.write(dashboard_idea)

    st.subheader("📈 Sample Visualization")
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        st.pyplot(fig)