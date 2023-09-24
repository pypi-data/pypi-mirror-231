import subprocess
import os
import streamlit as st

def run():
    # Display the dog image
    st.image("https://as2.ftcdn.net/v2/jpg/02/86/14/97/1000_F_286149728_jCLJnMOT2Yj7AMSXgFmBHoVbnT3MnAYM.jpg")

    # Call the streamlit run command
    subprocess.call(["streamlit", "run", os.path.join(os.path.dirname(__file__), 'main.py')])

if __name__ == "__main__":
    run()