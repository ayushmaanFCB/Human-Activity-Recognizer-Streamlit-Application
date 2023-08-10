import streamlit as st
import pandas as pd
import numpy as np
import imutils
import sys
import cv2
import os
import shutil

st.set_page_config(page_title="Activity Detection - LIVE STREAM", page_icon="⏺️", layout="centered",
                   initial_sidebar_state="expanded")

cache_clear = st.sidebar.button("Clear the Cache and Temporary Files")
if cache_clear:
    if os.path.exists("./temp"):
        shutil.rmtree("./temp")
        st.sidebar.success(
            "The temporary files have been cleared successfully 🗑️")
    else:
        st.sidebar.success("No temporary files detected")

st.markdown("""
<h1 style="text-align:center">DETECTING ACTIVITY FROM LIVE WEB CAMERA FEED</h1>
<hr>
""", unsafe_allow_html=True)


z1, z2 = st.columns([1, 1])
with z2:
    st.image("./assets/live-1.png")

with z1:
    st.markdown("""
        <p style="text-align:justify; font-size:18px">Click the button to start the camera stream. The output will be visible in a pop-up window. The output can an be downloaded once the camera stream is closed.</p>
""", unsafe_allow_html=True)

    st.markdown("""
            <p style="text-align:center; font-size:18px; border-style:dashed;border-width:1px; padding:10px"><b>NOTE</b><br><i>In order to <u>Close the Live Stream</u>, press 'X' on the Keyboard.</i></p>
    """, unsafe_allow_html=True)

    detect_but = st.button("START LIVE STREAM", use_container_width=True)


if detect_but:

    if detect_but:
        try:
            with st.spinner('Starting the Live Camera feed, Output window will appear.....'):
                os.system(
                    "python ./code/detection.py --model ./code/resnet-34_kinetics.onnx --classes ./code/Actions.txt")

                st.balloons()

                x1, x2 = st.columns([5, 1])

                with x1:
                    st.success(
                        "Activity detection was successfull, you can now download the output: ", icon="✅")

                with x2:
                    with open("./temp/output.mp4", "rb") as file:
                        btn = st.download_button(
                            label="Download Output",
                            data=file,
                            file_name="output.mp4",
                            mime="application/octet-stream"
                        )

        except Exception as e:
            print(e)
            st.error(
                "There has been some issue, please check for Camera permissions and connectivity", icon="⚠️")

st.markdown("""
        <hr>
""", unsafe_allow_html=True)
