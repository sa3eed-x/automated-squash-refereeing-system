from ultralytics import YOLO
#if __name__ == '__main__':
# Load a model
#model = YOLO('yolov8s.yaml')  # build a new model from YAML
#-------->>>> Training <<<<--------
#results = model.train(data='D:/!1)year 4/graduation/yolo-trials/Squash_Ball_detection.v1i.yolov8/data.yaml', epochs=10 ,device=0)
#-------->>>> Prediction <<<<--------
# Load a custom trained YOLOv8n model
model = YOLO('D:/!1)year 4/graduation/yolo-trials/runs/detect/train-s/weights/best.pt')
model.predict('D:/!1)year 4/graduation/videos/_THAT REACTION SAYS IT ALL!_ _ Kennedy v Elaraby _ U.S. Open 2023 _ RD3 _ HIGHLIGHTS (SQUASHTV).mp4', save=True, show=True, conf=0.1, augment=True, max_det=1,visualize=True)
#-------->>>> Tracking <<<<--------
#results = model.track(source="D:/!1)year 4/graduation/videos/_THAT REACTION SAYS IT ALL!_ _ Kennedy v Elaraby _ U.S. Open 2023 _ RD3 _ HIGHLIGHTS (SQUASHTV).mp4", conf=0.1, augment=True, max_det=1, iou=0, show=True,tracker="bytetrack.yaml")