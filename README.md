# Human Activity Recognizer Streamlit Application

A Streamlit (Python Web Framework) Application that detects most common human activities from Pre-Recorded Videos or Live Camera Feed.
The technique of identifying and interpreting distinct human actions and behaviours utilising cutting-edge technology like computer vision and machine learning is known as human activity detection.
<br><br>

In many areas, safety, effectiveness, and convenience are significantly improved by human activity detection, and this technology's continued advancement holds the possibility of revolutionising how humans interact with technology and the outside world.
<br><br>

This web-application was designed within a small period of time, and hence pre-trained ONNX was used for the detection. ".onnx" files are binary files that record the model architecture and parameters in a standardised format, making it simpler to exchange models between various frameworks and tools.

<hr>

<b><i><u>Running the application</u></b></i>
- Clone the repository (do not change the folder structure)
- ```pip install requirements.txt```
- The Model .onnx file needs to be downloaded from : https://github.com/onnx/models/blob/main/vision/classification/resnet/model/resnet34-v2-7.onnx
- Place the <b><i>'resnet34-v2-7.onnx'</i></b> downloaded file inside the <b><i>code</i></b> folder
- In order to run the application : ```python main.py```

<hr>

<u><b><i>Application Preview</b></i></u>

Landing Page:
![Screenshot 2023-08-10 155948](https://github.com/ayushmaanFCB/Human-Activity-Recognizer-Streamlit-Application/assets/92968225/dc679e63-e3ca-4bac-8372-7d7085e5cd31)

<br>

Detection From Pre-Recorded Clip
![Screenshot 2023-08-10 160026](https://github.com/ayushmaanFCB/Human-Activity-Recognizer-Streamlit-Application/assets/92968225/258a09fd-98a5-4965-a25b-cf10b544db66)

<br>

Live Streams - Detection Video with labelled activities can be downloaded
![Screenshot 2023-08-10 160226](https://github.com/ayushmaanFCB/Human-Activity-Recognizer-Streamlit-Application/assets/92968225/d2906530-2a6f-451c-b90c-2c84a340dce1)

<hr>
