import streamlit as st
import pandas as pd
import numpy as np
import os
import shutil

st.set_page_config(page_title="Activity Detection - HOME", page_icon="🏠", layout="wide",
                   initial_sidebar_state="expanded")

cache_clear = st.sidebar.button("Clear the Cache and Temporary Files")
if cache_clear:
    if os.path.exists("./temp"):
        shutil.rmtree("./temp")
        st.sidebar.success(
            "The temporary files have been cleared successfully 🗑️")
    else:
        st.sidebar.success("No temporary files detected")


st.markdown("<h1 style='text-align:center'>HUMAN ACTIVITY DETECTION</h1><hr>",
            unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])


with col1:
    st.markdown("""
        <p style="text-align:justify; font-size:18px">The technique of identifying and interpreting distinct human actions and behaviours utilising cutting-edge technology like computer vision and machine learning is known as human activity detection. There are several uses for this technology, including smart homes, surveillance and security systems, and healthcare monitoring. The system can identify and classify actions like walking, running, sitting, gesturing, or even more complicated activities like cooking or playing sports by analysing visual or sensor data, such as video feeds or motion sensors. In many areas, safety, effectiveness, and convenience are significantly improved by human activity detection, and this technology's continued advancement holds the possibility of revolutionising how humans interact with technology and the outside world.</p>
        """, unsafe_allow_html=True)

    st.markdown("""
        <p style="text-align:justify; font-size:18px">This web-application was designed within a small period of time, and hence pre-trained ONNX was used for the detection.</p>
        <ul style="text-align:justify; font-size:18px">
                <li style="text-align:justify; font-size:18px">".onnx" files are binary files that record the model architecture and parameters in a standardised format, making it simpler to exchange models between various frameworks and tools.</li>
                <li style="text-align:justify; font-size:18px">ONNX (Open Neural Network Exchange) is an open-source format created to represent machine learning models.</li>
                <li style="text-align:justify; font-size:18px">We can export a machine learning model to an.onnx file after training it using a particular framework, such as PyTorch or TensorFlow.</li>
                <li style="text-align:justify; font-size:18px">This eliminates the requirement for model conversion or retraining by allowing you to import the model and use it in other frameworks or tools that support ONNX.</li>
        </ul>
        """, unsafe_allow_html=True)

with col2:
    st.image("./assets/home.png", output_format="PNG")
    st.image("./assets/home2.png", output_format="PNG")

st.markdown("<hr>",
            unsafe_allow_html=True)
