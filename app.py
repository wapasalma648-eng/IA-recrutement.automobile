import streamlit as st
import pdfplumber
import json

st.title("🚗 IA de Tri de CV - Secteur Automobile")

with open('criteria.json', 'r') as f:
    criteria = json.load(f)

uploaded_file = st.file_uploader("Upload ton CV (PDF)", type="pdf")

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "".join([page.extract_text() for page in pdf.pages])
    
    score = 0
    found = []
    for cat, keywords in criteria.items():
        for word in keywords:
            if word.lower() in text.lower():
                score += 25
                found.append(f"✅ {cat} : {word}")
                break
    
    st.subheader(f"Score : {score}/100")
    st.write(found)
