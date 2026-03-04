
import cv2
from detector import detect
from tracker import Tracker
from compliance import evaluate
from logger import log_violation
from config import CAMERA_SOURCES

tracker=Tracker()
caps=[cv2.VideoCapture(src) for src in CAMERA_SOURCES]

while True:
    for idx,cap in enumerate(caps):
        ret,frame=cap.read()
        if not ret:
            continue

        detections=detect(frame)
        tracked=tracker.update(detections)
        violations=evaluate(tracked)

        for obj in tracked:
            x1,y1,x2,y2=obj["bbox"]
            color=(0,255,0)

            if obj in violations:
                color=(0,0,255)
                log_violation(obj,frame)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
            cv2.putText(frame,obj["label"],(x1,y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)

        cv2.imshow(f"Camera {idx}",frame)

    if cv2.waitKey(1)&0xFF==ord("q"):
        break

for cap in caps:
    cap.release()

cv2.destroyAllWindows()
