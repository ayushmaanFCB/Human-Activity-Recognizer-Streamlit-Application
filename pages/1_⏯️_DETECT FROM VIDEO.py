import streamlit as st
import pandas as pd
import numpy as np
import imutils
import sys
import cv2
import os
import shutil

st.set_page_config(page_title="Activity Detection - FROM VIDEOS", page_icon="⏯️", layout="wide",
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
<h1 style="text-align:center">DETECTING ACTIVITY FROM A VIDEO</h1>
<hr>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 3])

with col1:
    x = st.video("./assets/demo-read.mp4")

with col2:
    st.markdown("""
        <p style="text-align:justify; font-size:18px">Please upload the video for activity detection here. The output will be visible in a pop-up window and can be downloaded after the output is shown.</p>
""", unsafe_allow_html=True)

    video_file = st.file_uploader(
        "Upload the Video (should be of format '.mp4')", type=["mp4"])

    y1, y2, y3 = st.columns([1, 1, 1])
    with y2:
        detect_but = st.button("DETECT ACTIVITIES", use_container_width=True)

    if detect_but:
        try:

            with st.spinner('Processing the Video, Output should shortly appear.....'):
                if not os.path.exists("./temp"):
                    os.makedirs("./temp")

                with open(os.path.join("temp", "uploaded_media.mp4"), "wb") as f:
                    f.write(video_file.getbuffer())
                x.video("./temp/uploaded_media.mp4")

                # st.toast('Your edited image was saved!', icon='😍')

                os.system(
                    "python ./code/detection.py --model ./code/resnet-34_kinetics.onnx --classes ./code/Actions.txt --input ./temp/uploaded_media.mp4")

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
                "There has been some issue, make sure a file was uploaded and the type is .mp4 only. Please Retry !!!", icon="⚠️")

st.markdown("""
<hr>
""", unsafe_allow_html=True)
