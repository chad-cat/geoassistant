import streamlit as st
from llm_handler import ask_text_query, ask_image_query
from utils import load_csv_summary, load_image

st.set_page_config(page_title=" LLM Geology Assistant")

st.title(" LLM Geology Assistant")

option = st.sidebar.radio("Choose an action", ["Ask a Question", "Analyze CSV", "Analyze Image"])

if option == "Ask a Question":
    query = st.text_input(" Enter your geology question:")
    if query and st.button("Ask"):
        response = ask_text_query(f"Answer this geology question simply: {query}")
        st.success(response)

elif option == "Analyze CSV":
    csv_file = st.file_uploader(" Upload a CSV file", type=["csv"])
    if csv_file:
        with open("temp.csv", "wb") as f:
            f.write(csv_file.read())
        summary = load_csv_summary("temp.csv")
        response = ask_text_query(f"Analyze this CSV:\n{summary}")
        st.success(response)

elif option == "Analyze Image":
    img_file = st.file_uploader(" Upload an image (Gemini only)", type=["jpg", "jpeg", "png"])
    if img_file:
        image = load_image(img_file)
        response = ask_image_query("Describe this geology image in detail.", image)
        st.image(img_file, caption="Uploaded Image", use_column_width=True)
        st.success(response)
