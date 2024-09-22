import streamlit as st
from PIL import Image
import pytesseract

# Specify the correct path to Tesseract
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'



# Title for the web app
st.title("OCR and Document Search Application")

# File uploader to allow users to upload an image
uploaded_image = st.file_uploader("Upload an Image (JPEG, PNG)", type=["png", "jpg", "jpeg"])

# If an image is uploaded
if uploaded_image is not None:
    # Open the image
    img = Image.open(uploaded_image)
    
    # Display the uploaded image on the web page
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(img, lang="eng+hin")
    
    # Show extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)
    
    # Search functionality
    st.subheader("Search in Extracted Text")
    search_query = st.text_input("Enter a keyword to search")
    
    # If user enters a search query
    if search_query:
        if search_query.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_query}' found in the text.")
        else:
            st.write(f"Keyword '{search_query}' not found.")

