
import subprocess
import sys

# Install spaCy model if not already installed
try:
    import spacy
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "spacy"])

# Download the model if not already downloaded
try:
    import en_core_web_sm
except ImportError:
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])



import streamlit as st
import agent  

st.set_page_config(page_title="AI Fashion Assistant", layout="wide")

st.title("🛍️ AI Fashion Shopping Assistant")
st.write("Ask me about product searches, shipping estimates, discounts, price comparisons, or return policies!")

query = st.text_input("Enter your request:")
if st.button("Submit"):
    response = agent.agent_response(query)
    
    if isinstance(response, list) and response:
        st.subheader("Here are some matching products:")
        for item in response:
            st.image("https://via.placeholder.com/150", width=100)
            st.write(f"**{item['title']}** - ${item['price']}")
    elif isinstance(response, dict):
        st.json(response)
    else:
        st.write(response)

