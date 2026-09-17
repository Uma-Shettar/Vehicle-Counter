from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

model = YOLO("yolov8s.pt") 

Class_names = model.names 
print(Class_names)

vid = cv2.VideoCapture("Video/vid_3.mp4") 

tracker = Sort(max_age=25, min_hits=3, iou_threshold=0.3)

line = [(200, 300), (900, 300)]
total = []

while True:
    success, frame = vid.read()

    if not success:
        break

    results = model(frame, stream=True) 
    detection = np.empty((0, 5))
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            w, h = x2 - x1, y2 - y1

            conf = math.ceil(box.conf[0] * 100) / 100

            classname = Class_names[int(box.cls[0])]

            if conf > 0.4 and classname in ["motorcycle", "car", "truck", "bus", "bicycle"]:
                cvzone.putTextRect(frame, f"{Class_names[int(box.cls[0])]} {conf}", (max(0, int(x1)), max(35, int(y1))), scale=1, thickness=2, offset=3)
                cvzone.cornerRect(frame, (int(x1), int(y1), int(w), int(h)), l=5, t=3, rt=1, colorR=(255, 0, 255))
                detection = np.vstack((detection, [x1, y1, x2, y2, conf]))

    tracks = tracker.update(detection)
    cv2.line(frame, line[0], line[1], (0, 0, 255), 5)
    for track in tracks:
        x1, y1, x2, y2, id = track
        #cvzone.putTextRect(frame, f"ID: {int(id)}", (max(0, int(x1)), max(35, int(y1))), scale=1, thickness=2, offset=3)
        #cvzone.cornerRect(frame, (int(x1), int(y1), int(x2 - x1), int(y2 - y1)), l=10, t=3, rt=1, colorR=(255, 0, 255))

        x_center = int((x1 + x2) / 2)
        y_center = int((y1 + y2) / 2)

        cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), cv2.FILLED)

        if line[0][1] - 5 < y_center < line[0][1] + 20 and line[0][0] < x_center < line[1][0]:
            if total.count(id) == 0:
                total.append(id)
                cvzone.cornerRect(frame, (int(x1), int(y1), int(x2 - x1), int(y2 - y1)), l=15, t=5, rt=1, colorC=(255, 0, 0))
                
    cvzone.putTextRect(frame, f"Total Vehicles: {len(total)}", (50, 50), scale=2, thickness=3, offset=10, colorR=(0, 0, 255))
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
