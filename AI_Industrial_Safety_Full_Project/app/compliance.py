
def evaluate(tracked):
    persons=[o for o in tracked if o["label"]=="person"]
    helmets=[o for o in tracked if o["label"]=="helmet"]
    masks=[o for o in tracked if o["label"]=="mask"]

    violations=[]

    for p in persons:
        px1,py1,px2,py2=p["bbox"]

        helmet_ok=any(
            hx1<px2 and hx2>px1 and hy1<py2 and hy2>py1
            for hx1,hy1,hx2,hy2 in [h["bbox"] for h in helmets]
        )

        mask_ok=any(
            mx1<px2 and mx2>px1 and my1<py2 and my2>py1
            for mx1,my1,mx2,my2 in [m["bbox"] for m in masks]
        )

        if not helmet_ok or not mask_ok:
            violations.append(p)

    return violations
