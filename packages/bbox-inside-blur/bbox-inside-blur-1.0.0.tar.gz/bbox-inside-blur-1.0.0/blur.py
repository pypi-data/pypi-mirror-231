from sahi import AutoDetectionModel
from sahi.utils.cv import read_image
from sahi.utils.file import download_from_url
from sahi.predict import get_prediction
import cv2
import time
from glob import glob
from tqdm import tqdm
from IPython.display import Image

start_time = time.time()

# YOLOv5 modelinin yolunu belirtin
yolov5_model_path = '/home/yusufesat-ai/PycharmProjects/shop-sign-blur/best.pt'

# Detection modelini yükleyin
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov5',
    model_path=yolov5_model_path,
    confidence_threshold=0.5,
    device="cuda:0",
)

data_path = glob("/home/yusufesat-ai/PycharmProjects/shop-sign-blur/images/*")

# image_path = "/home/yusufesat-ai/PycharmProjects/shop-sign-blur/images/1e9vchvZb1MZjWRbyURsYA_1_jpeg.rf.7a18d08289410d94bdfa9efc0bf365ba.jpg"

for i in tqdm(data_path):
    img = cv2.imread(i)
    result_ = get_prediction(read_image(i), detection_model)
    object_prediction_list = result_.object_prediction_list
    name = i.split("/")[-1]
    objects = []
    ids = []
    scores = []
    for j in object_prediction_list:
        id = j.category.name
        coord = str(j.bbox).split("(")[1].split(")")[0].split(",")
        b_ = []
        for b in coord:
            c_ = int(float(b))
            b_.append(c_)
        objects.append(b_)
        ids.append(id)

        xmin, ymin, xmax, ymax = b_

        roi = img[ymin:ymax, xmin:xmax]

        roi_blurred = cv2.GaussianBlur(roi, (25, 25), 15)

        img[ymin:ymax, xmin:xmax] = roi_blurred

    cv2.imwrite("/home/yusufesat-ai/PycharmProjects/shop-sign-blur/inferences/" + name, img)

# result = get_prediction(read_image(image_path), detection_model)
#
# result.export_visuals(export_dir="/home/yusufesat-ai/PycharmProjects/shop-sign-blur/demo_data")
# Image("/home/yusufesat-ai/PycharmProjects/shop-sign-blur/demo_data/prediction_visual.png")

end_time = time.time()
execution_time = end_time - start_time
print("Time Spent: ", execution_time)
