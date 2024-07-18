# import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st
# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the model
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, api_key=api_key)

# Create a simple prompt template
prompt_template = ChatPromptTemplate.from_template("You are a helpful assistant. {input}")

# Create a LangChain LLMChain
chain = LLMChain(llm=chat_model, prompt=prompt_template)

# Streamlit interface
st.title("3.5 Turbo Chatbot")
user_input = st.text_input("Enter the input ---")

if user_input:
    with st.spinner("Thinking..."):
        response = chain.run(input=user_input)
    st.write("**Response:**")
    st.write(response)
