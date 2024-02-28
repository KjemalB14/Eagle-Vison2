from ultralytics import YOLO

model = YOLO('/home/ENKH/Senior Project/Eagle-Vison2/Senior_cap/best10.pt')

model.predict(source='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmathmonks.com%2Fwp-content%2Fuploads%2F2020%2F04%2FSquare.jpg&f=1&nofb=1&ipt=6b21da0b4f8a2241860a4304771cd459f77cbdba0e6d91c567e4b5ec477fe4df&ipo=images', show=True, conf=.50, save=True)