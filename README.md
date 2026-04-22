# 🔐 AI API Security Analyzer

### 👨‍💻 Developed by: AI Developer

---

## 📌 Overview

**AI API Security Analyzer** is an intelligent tool that analyzes code snippets and AI prompts to detect potential security vulnerabilities, unsafe practices, and prompt injection risks.

It leverages a Large Language Model (LLM) to perform advanced reasoning and provide actionable security recommendations, helping developers build safer and more robust AI systems.

---

## ✨ Features

- 🔍 Analyze API code for vulnerabilities  
- 🧠 Detect prompt injection risks  
- 🚨 Identify unsafe coding practices  
- 📊 Provide risk level (Low / Medium / High)  
- 💡 Suggest security fixes and improvements  
- ⚡ Simple UI using Streamlit  

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- OpenAI API (LLM-based analysis)  

---

## 🏗️ Architecture

Input (Code / Prompt)  
        ↓  
LLM Security Analysis  
        ↓  
Risk Detection  
        ↓  
Fix Suggestions  
        ↓  
Streamlit UI Output  

---

## 📂 Project Structure

ai-security-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   └── analyzer.py  

---

## ▶️ How to Run

### 1️⃣ Install dependencies

pip install -r requirements.txt  

---

### 2️⃣ Set OpenAI API Key

Mac/Linux:
export OPENAI_API_KEY=your_api_key  

Windows:
set OPENAI_API_KEY=your_api_key  

---

### 3️⃣ Run the app

streamlit run app.py  

---

## 💡 Example Input

```python
password = "123456"
