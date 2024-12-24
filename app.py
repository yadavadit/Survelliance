import streamlit as st
import process
import os
import cv2
from PIL import Image
import numpy as np

def main():
    st.title("Surveliance App")
    
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        os.makedirs('input', exist_ok=True)
        os.makedirs('processed', exist_ok=True)
        
        temp_path = os.path.join('input', uploaded_file.name)
        with open(temp_path, 'wb') as f:
            f.write(uploaded_file.getvalue())
            
        try:
            processed_path = process.process_image(uploaded_file.name)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Original Image")
                original_image = Image.open(uploaded_file)
                st.image(original_image, use_column_width=True)
                
            with col2:
                st.subheader("Processed Image")
                processed_image = Image.open(processed_path)
                st.image(processed_image, use_column_width=True)
                
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()