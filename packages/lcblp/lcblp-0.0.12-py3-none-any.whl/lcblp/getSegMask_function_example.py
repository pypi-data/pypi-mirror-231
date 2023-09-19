from .getSegMask_function import getSegmentedImage
import cv2
from .models import get_model
import torch

model_type='DeepLabv3'
backbone='resnet50'
path_weight='weights/230912_face_deeplabv3_01.pt'
input_size=1024
gpu = 0

model, desc, _1, _2 = get_model(model_type, backbone, 2, True, input_size)
chechpoint = torch.load(path_weight, map_location=torch.device(f'cuda:{gpu}'))
model.load_state_dict(chechpoint['model_state_dict'])

image = cv2.imread('data/face/test_temp/images/라온점_김시은_20230824-094100_F.png')
mask = getSegmentedImage(model=model, image=image, gpu=gpu)
# cv2.imwrite('lastTest12.png', mask)