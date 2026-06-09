import streamlit as st
import google.generativeai as gen
gen.configure(api_key = "api key")
model = gen.GenerativeModel("gemini-2.5-flash")
prompt = st.text_input("Answer any questions asked by the user")
if st.button("Submit"):
    res=model.generate_content(prompt+"you are the smart email writer.writes or replies to email with tone adjustment and quick replies.")
    st.write(res.text)