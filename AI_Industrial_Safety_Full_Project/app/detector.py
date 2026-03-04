
from ultralytics import YOLO
from config import MODEL_PATH, CONFIDENCE_THRESHOLD

model = YOLO(MODEL_PATH)

def detect(frame):
    results = model(frame, verbose=False)[0]
    detections = []
    for box in results.boxes:
        conf = float(box.conf[0])
        if conf >= CONFIDENCE_THRESHOLD:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            x1,y1,x2,y2 = map(int, box.xyxy[0])
            detections.append((x1,y1,x2,y2,label))
    return detections
