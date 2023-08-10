import numpy as np
import argparse
import imutils
import sys
import cv2
import os


ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
                help="path to model")
ap.add_argument("-c", "--classes", required=True,
                help="path to labels file")
ap.add_argument("-i", "--input", type=str, default="",
                help="optional video file")
args = vars(ap.parse_args())


ACT = open(args["classes"]).read().strip().split("\n")
SAMPLE_DURATION = 16
SAMPLE_SIZE = 112


print("\n\nLOADING.........")
gp = cv2.dnn.readNet(args["model"])

print("ACCESSING........")
vs = cv2.VideoCapture(args["input"] if args["input"] else 0)
writer = None
fps = vs.get(cv2.CAP_PROP_FPS)
print("<Original FPS: ", fps, " >")

if not os.path.exists("./temp"):
    os.makedirs("./temp")


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./temp/output.mp4', fourcc, 20.0, (640, 480))

while True:
    frames = []
    originals = []
    flag=0

    for i in range(0, SAMPLE_DURATION):
        (grabbed, frame) = vs.read()
        if not grabbed:
            print("All frames are over, nothing to read, EXITING.......")
            sys.exit(0)
        originals.append(frame)
        frame = imutils.resize(frame, width=400)
        frames.append(frame)

    blob = cv2.dnn.blobFromImages(frames, 1.0,
                                  (SAMPLE_SIZE, SAMPLE_SIZE),
                                  (114.7748, 107.7354, 99.4750),
                                  swapRB=True, crop=True)
    blob = np.transpose(blob, (1, 0, 2, 3))
    blob = np.expand_dims(blob, axis=0)

    gp.setInput(blob)
    outputs = gp.forward()
    label = ACT[np.argmax(outputs)]

    for frame in originals:

        cv2.rectangle(frame, (0, 0), (300, 40),
                      (0, 0, 0), -1)
        cv2.putText(frame, label, (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2)

        cv2.imshow("Activity Recognition", frame)

        frame = cv2.resize(frame, (640, 480))
        out.write(frame)

        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('x'):
            out.release()
            flag=1
            break
    if flag == 1:
        break
        
cv2.destroyAllWindows()

        
    
