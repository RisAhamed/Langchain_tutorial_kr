
from langchain.prompts import ChatPromptTemplate
from langchain.prompts  import PromptTemplate
# from posthog import page
import streamlit as st
from langchain_community.llms import CTransformers


st.set_page_config(page_title = "Blog Generator",
                   layout = "wide",
                   initial_sidebar_state="collapsed",
                   page_icon = "��")

st.header("Generate Blogs for the blog generator  page    ")
input_text = st.text_input(
    "Enter the Blog Topic"
)

def getLLamaresponse(input_text,no_words,blog_style):
    llm = CTransformers(model = "model\llama-2-7b-chat.ggmlv3.q2_K.bin",model_type = "llama",
                        config ={"max_new_tokens":256,
                                 "temperature":0.01})
    

    template = """

    write a {blog_style} to make me feel good on {input_text} within {no_words} words"""
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],template= template)
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


col1,col2 =st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")

with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    

submit = st.button("Genrerate")

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))



'''%pip install --upgrade --quiet  ctransformers'''