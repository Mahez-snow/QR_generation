import streamlit as st
from qr import generate_qr

st.set_page_config(page_title="QR Code Generator", page_icon="🔗")

st.title("🔗 QR Code Generator")
st.write("Generate a QR code for any URL using Python")

url = st.text_input("Enter your URL")

if st.button("Generate QR Code"):
    if url:
        file_path = generate_qr(url)
        st.success("QR Code generated successfully!")

        st.image(file_path, caption="Generated QR Code")

        with open(file_path, "rb") as file:
            st.download_button(
                label="Download QR Code",
                data=file,
                file_name="qr.png",
                mime="image/png"
            )
    else:
        st.warning("Please enter a valid URL")
