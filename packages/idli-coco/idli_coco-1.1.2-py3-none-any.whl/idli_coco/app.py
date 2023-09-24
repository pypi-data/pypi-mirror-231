import streamlit as st
from PIL import Image

def app():
    image = Image.open('idli_coco.jpg')
    st.image(image, caption='Idli & Coco')

if __name__ == "__main__":
    app()