import streamlit as st
from langchain_groq import ChatGroq

def correct_grammar(text):
    llm = ChatGroq(
        model="gemma2-9b-it",
        temperature=0,
        groq_api_key="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" 
    )
    
    prompt = f"""
    Check the grammar of the following text. If it's correct, return it as is.
    If it has grammar mistakes, correct them without changing the meaning or adding extra words.
    Also, list the incorrect words and provide feedback on what went wrong.
    
    Text: {text}
    """
    
    response = llm.invoke(prompt)
    corrected_text = response.content
    
    return corrected_text

def main():
    st.title("Grammar Checker with AI and Correction")
    
    input_text = st.text_area("Enter a sentence to check grammar:")
    
    if st.button("Check Grammar"):
        if input_text.strip():
            corrected_text = correct_grammar(input_text)
            
            if corrected_text.strip() == input_text.strip():
                st.success("✅ Your sentence is already correct!")
            else:
                st.subheader("Corrected Text:")
                st.write(corrected_text)
        else:
            st.warning("⚠️ Please enter some text to check.")

if __name__ == "__main__":
    main()
