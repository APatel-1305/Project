import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    .stTextInput > div > div > input {
        background-color: #2a2a2a;
        color: white;
    }
    .stTextArea > div > textarea {
        background-color: #2a2a2a;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📩 Contact Us")

st.write("Have questions, feedback, or want to contribute? We'd love to hear from you!")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")

    if submitted:
        st.success("✅ Thanks for reaching out! We'll get back to you soon.")

