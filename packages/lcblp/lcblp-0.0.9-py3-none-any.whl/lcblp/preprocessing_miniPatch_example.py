import cv2
import json
import numpy as np
import time
import copy
import os
import glob
import sys
from tqdm import tqdm

# # 시스템 경로 추가
# sys.path.append(f'{os.path.dirname(__file__)}')

# face segmentation model load -------
from getSegMask_function import getSegmentedImage
from models import get_model
import torch

model_type='DeepLabv3'
backbone='resnet50'
path_weight='segmentation/weights/230912_face_deeplabv3_01.pt'
input_size=1024

model, desc, _1, _2 = get_model(model_type, backbone, 2, True, input_size)
chechpoint = torch.load(path_weight)
model.load_state_dict(chechpoint['model_state_dict'])

# 변수 설정 ---
unitSize = 256
load_dir = 'inputs'
save_dir = f'outputs/{unitSize}'

image_paths = glob.glob(os.path.join(load_dir, '*.jpg'))
pbar = tqdm(image_paths, total = len(image_paths), desc = '진행률', ascii=' =', leave=True) # ascii는 앞에 공백이 하나 있어야함
time_list = []
for image_path in pbar:
    start_time = time.time()

    image = cv2.imread(image_path)
    image_name = image_path.split('/')[-1]

    # face segmentation 수행 ---
    mask = getSegmentedImage(model=model, image=image, gpu=0)

    # minipatch 만듦 ---
    from miniPatch_preprocessing import preprocessing_miniPatch
    imageAndMask, miniPatches = preprocessing_miniPatch(image=image, mask=mask, unitSize=unitSize)

    # minipatch 저장 ---
    save_dir_dir = os.path.join(save_dir, f'{image_name.split(".")[0]}')
    os.makedirs(save_dir_dir, exist_ok=True)

    cv2.imwrite(os.path.join(save_dir, image_name.split(".")[0]+'.png'), imageAndMask) # bit and 이미지 저장
    for i in range(len(miniPatches)):
        for j in range(len(miniPatches[i])):
            minipatch = miniPatches[i][j].squeeze()
            # if np.sum(w) == 0: continue # 정보가 없는 이미지
            save_path = os.path.join(save_dir_dir, f'{image_name.split(".")[0]}_{i}_{j}.png')
            cv2.imwrite(save_path, minipatch)

    end_time = time.time()
    print(end_time-start_time, 'sec')
    time_list.append(end_time-start_time)

# 한 정면 이미지 처리하는 걸리는 평균 시간
print(sum(time_list)/len(time_list), 'sec')


