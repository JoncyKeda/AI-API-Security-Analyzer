import streamlit as st
from utils.analyzer import analyze_security

st.set_page_config(page_title="AI Security Analyzer", layout="wide")

st.title("🔐 AI API Security Analyzer")

st.write("Analyze API code or AI prompts for vulnerabilities and security risks.")

user_input = st.text_area("Paste your code or prompt here:", height=300)

if st.button("Analyze Security"):
    if user_input:
        with st.spinner("Analyzing security risks..."):
            result = analyze_security(user_input)

        st.subheader("🚨 Security Analysis")
        st.write(result)
    else:
        st.warning("Please enter code or prompt to analyze.")
