import streamlit as st
import agent  

# Set up Streamlit app configurations
st.set_page_config(page_title="AI Fashion Assistant", layout="wide")

# App title and description
st.title("🛍️ AI Fashion Shopping Assistant")
st.write("Ask me about product searches, shipping estimates, discounts, price comparisons, or return policies!")

# User input and response
query = st.text_input("Enter your request:")
if st.button("Submit"):
    response = agent.agent_response(query)
    
    # Display product search results if the response is a list
    if isinstance(response, list) and response:
        st.subheader("Here are some matching products:")
        for item in response:
            st.image("https://via.placeholder.com/150", width=100)
            st.write(f"**{item['title']}** - ${item['price']}")
    
    # Display price comparison or other details if response is a dictionary
    elif isinstance(response, dict):
        st.json(response)
    
    # Default message if the query is not recognized
    else:
        st.write(response)
