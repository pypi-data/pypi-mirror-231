import os
import argparse
import numpy as np
import cv2
import sys
import skimage.draw
import skimage.io

from .transforms import get_transform
from .wrapper import _predict, _criterion, _metric

## Pytorch
import torch
from .utils import get_config

def inferrence(model, image, label, gpu_available=None, gpu=0, cfg=None):
    model.eval()
    if gpu_available and gpu is not None:
        image = image.cuda(gpu, non_blocking=True)
        # label = label.cuda(cfg.gpu, non_blocking=True)

    with torch.no_grad():
        pred = _predict(model, image, label, cfg.model_type, phase='test')

    # 결과 마스크
    pred = torch.argmax(pred[0], dim=0).detach().cpu().numpy()
    h, w = pred.shape[:2]
    masks = []
    for i in range(1, cfg.num_classes):
        pred_where = np.where(pred[:, :] == i)
        mask = np.zeros([h, w, 1], dtype=np.uint8)
        for y, x in zip(pred_where[0], pred_where[1]):
            mask[y, x] = np.array([255])
        masks.append(mask)

    return masks

def getSegmentedImage(model=None, image=None, gpu=0):
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_yml', type=str, default=f'{os.path.dirname(__file__)}/config.yml')
    args = parser.parse_args()

    cfg = get_config(args.path_yml)

    if type(gpu) != int:
        os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu)
        ngpus = len(os.environ['CUDA_VISIBLE_DEVICES'].split(','))
        main_gpu = 0
    else:
        main_gpu = gpu
        ngpus = 1

    gpu_available = torch.cuda.is_available()

    if not gpu_available:
        print('using CPU, this will be slow')

    elif gpu is not None:
        model = model.cuda(gpu)


    transforms = get_transform(cfg)
    transforms = transforms['valid']

    from PIL import Image, ImageOps

    # image = cv2.imread('data/face/test_temp/images/라온점_김시은_20230824-094100_F.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(image)  # numpy 이미지를 pil 이미지로 변환
    image = ImageOps.exif_transpose(image)
    image = np.uint8(image)

    image = transforms(image=image)
    image = image['image'].float()
    image = image.unsqueeze(0)
    label = torch.tensor([0])

    # criterion = Criterion()  # cross_entropy2d
    criterion = torch.nn.CrossEntropyLoss()

    # masks = valid_epoch(model, valid_loader, test_mode=cfg.test_mode)

    masks = inferrence(model, image, label, gpu_available=gpu_available, gpu=gpu, cfg=cfg)
    mask = masks[0]
    h, w = mask.shape[:2]

    # 혹시 마스크가 두개 이상으로 나뉘어 있을 때 예외 처리
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 1:
        print('many contours !')
        mask = cv2.resize(mask, (w//10, h//10)) # 폴리곤 마스크 생성의 시간 소요를 줄이기 위해 작게 만들어서 처리함
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        contourAreaList = []
        for i in contours:
            contourAreaList.append(cv2.contourArea(i))
        maxContourArea = max(contourAreaList)
        contour = contours[contourAreaList.index(maxContourArea)]
        contour = np.squeeze(contour, axis=1)
        hh, ww = mask.shape[:2]
        mask_new = np.zeros([hh, ww, 1], dtype=np.uint8)
        rr, cc = skimage.draw.polygon(contour[:, -1], contour[:, -2])  # y좌표만, x좌표만
        mask_new[rr, cc, 0] = 255  # 만든 0배열에 polygon 좌표에 1 채워줌
        mask = mask_new

    # cv2.imwrite('cv2pil.png', masks[0])

    return mask

if __name__ == '__main__':
    getSegmentedImage()


