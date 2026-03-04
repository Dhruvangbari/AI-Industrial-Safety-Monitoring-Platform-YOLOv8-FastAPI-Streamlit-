
import uuid

class Tracker:
    def update(self,detections):
        tracked=[]
        for d in detections:
            x1,y1,x2,y2,label=d
            tracked.append({
                "id":str(uuid.uuid4())[:8],
                "bbox":(x1,y1,x2,y2),
                "label":label
            })
        return tracked
