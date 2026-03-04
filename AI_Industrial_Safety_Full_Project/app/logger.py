
import os,cv2,time,pandas as pd
from config import VIOLATION_COOLDOWN

os.makedirs("../logs/images",exist_ok=True)
last_logged={}

def log_violation(person,frame):
    pid=person["id"]
    now=time.time()

    if pid in last_logged and now-last_logged[pid]<VIOLATION_COOLDOWN:
        return

    last_logged[pid]=now

    filename=f"../logs/images/{pid}_{int(now)}.jpg"
    cv2.imwrite(filename,frame)

    df=pd.DataFrame([[pid,now]],columns=["person_id","timestamp"])
    df.to_csv("../logs/violations.csv",mode="a",
              header=not os.path.exists("../logs/violations.csv"),
              index=False)
