from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from prompt import *


# Load environment variables from the .env file
load_dotenv()

# Access the environment variables just like you would with os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Response Format For my LLM Model
def story_generation(user_input, genre, tone ,mood,length,point_of_view,plot,keywords):
    # Define the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=1, api_key=GOOGLE_API_KEY)  

    # Define the prompt
    PROMPT_TEMPLATE = PROMPT  # Imported
    prompt = PromptTemplate(
            input_variables=["user_input", "genre", "tone" ,"mood","length","point_of_view","plot","keywords"], # input in prompt
            template=PROMPT_TEMPLATE,
        )
      
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate Response
    response=llm_chain.run({"user_input":user_input, 
                            "genre":genre ,
                            "tone":tone,
                            "mood":mood,
                            "length":length,
                            "point_of_view":point_of_view,
                            "plot":plot,
                            "keywords":keywords})
    return response

# Streamlit app
st.set_page_config(page_title="Story Generation")
st.header("Story Generation")

# Input text
user_input = st.text_area("Enter your Story topic", height=200)


# Side bar for parameters
with st.sidebar:
    st.title("Parameters:")
    genre=st.selectbox("Select The Genre of story ",["Romance","Science Fiction","Fantasy","Mystery","Horror","None"])
    tone=st.selectbox("Select The Tone of story ",["Happy","Sad","Melancholic","Inspirational","None"])
    mood=st.selectbox("Select The Mood of story ",["Peaceful","Energetic","Contemplative","Humorous","None"])
    length=st.text_input("Select The Length of story ")
    point_of_view=st.selectbox("Select The Point of View of story ",["First Person","Third Person Limited","Third Person Omniscient","Second Person","None"])
    plot=st.selectbox("Select The Plot Type of story ",["Linear","Non-Linear","Twist-Ending","Character-Driven","Plot-Driven","None"])
    keywords=st.text_area("Provide a list of keywords related to theme ")

if st.button("Generate"):
        response=story_generation(user_input, genre, tone ,mood,length,point_of_view,plot,keywords)
        st.write(response)



