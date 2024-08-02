import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("Please set the OPENAI_API_KEY environment variable in your .env file.")
else:
    os.environ["OPENAI_API_KEY"] = openai_api_key

# Function to load OpenAI model and get response
def get_openai_response(question):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, api_key=openai_api_key)
    message = HumanMessage(content=question)
    response = llm([message])
    return response.content

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Siri's chatbot")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit and input_text:
    response_text = get_openai_response(input_text)
    st.subheader("The Response is")
    st.write(response_text)
