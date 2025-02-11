import streamlit as st
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"  
)

def analyze_sentiment_and_suggest(text):
    prompt = f"""You are an assistant who has to understand the sentiment of the given sentence input by the user.
    That sentence is: {text}
    Based on the above text, you have to classify the user's sentiment into three categories: Positive, Negative, or Neutral.
    If the sentiment is positive, suggest ways that should be taken ahead.
    If the sentiment is negative, suggest ways that can be used to make the sentiment positive.
    If the sentiment is neutral, suggest ways that should be used to make the sentiment positive."""
    
    response = llm.invoke(prompt, max_tokens=250)
    return response.content


st.title("Sentiment Analysis & Suggestions")
st.write("Enter a sentence to analyze its sentiment and receive suggestions.")


user_input = st.text_area("Enter your sentiment:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = analyze_sentiment_and_suggest(user_input)
        st.write("Analysis Result:")
        st.write(result)
    else:
        st.warning("Please enter a valid sentence.")
