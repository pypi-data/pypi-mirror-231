import streamlit as st
from PIL import Image
import os

def app():
    st.title('Idli & Coco')
    image_path = os.path.join(os.path.dirname(__file__), 'idli_coco.jpg')
    image = Image.open(image_path)
    st.image(image, caption='Idli & Coco')

if __name__ == "__main__":
    app()