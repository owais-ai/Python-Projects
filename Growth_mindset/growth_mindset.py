import streamlit as st
import random

# Growth Mindset Quotes
quotes = [
    "Failure is just another step towards success.",
    "Challenges make you stronger, keep going!",
    "Effort and consistency beat talent.",
    "Keep learning, keep growing!",
    "Every expert was once a beginner."
]

# Streamlit UI
st.title("💡 Growth Mindset Quotes")
st.write("Ek naye mindset ke saath din ki shuruaat karo!")

# Button to generate new quote
if st.button("New Quote"):
    st.write(random.choice(quotes))
