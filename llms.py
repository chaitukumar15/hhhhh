
import streamlit as st 
from google import genai


if "message" not in st.session_state:
    st.session_state.message=[]

text_user=st.chat_input("eter your prompt")



if text_user:
    st.session_state.message.append({"role":"user","content":text_user})
    client = genai.Client(api_key="AIzaSyCJ8zmYCmAOYUVGmfoCy-NiY-APoMSDEt8")
    with  st.spinner("loading ......"):
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=text_user
        )
    # st.write(response.text)
    st.session_state.message.append({"role":"assistant","content":response.text})




# st.write(st.session_state.message)


for i in st.session_state.message:
    with st.chat_message(i["role"]):
        #  with st.expander(i["role"]):
            st.write(i["content"])



    # [{
    #     "role":"user",
    #     "content":text_user
    # },
    # {
    #     "role":"assistant",
    #     "content":genini res
    # }
    # ]
  
#   with st.chat_message("user"):
#     st.write(text_user)
#   with st.chat_message("assistant"):
#     st.write(res)

# data=st.text_input("enter prompt")

# btn =st.button("submit")

# if btn:
#     client = genai.Client(api_key="AIzaSyDdoFIa4rPV-4gvMO4gPBgLyV22WjIQ-N8")
#     with  st.spinner("loading ......"):
#         response = client.models.generate_content(
#             model="gemini-2.5-flash", contents=data
#         )
#     st.write(response.text)
   





