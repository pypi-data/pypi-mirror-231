import os
import cv2
import math
import pytz
import time
import yaml
import pickle
import socket
import random
import datetime
import numpy as np
import albumentations as A
import sys

import torch

from .config import config

class Params:
    def __init__(self, project_file):
        self.params = yaml.safe_load(open(project_file).read())
        
    def __getattr__(self, item):
        return self.params.get(item, None)

def save_obj(name, obj):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(f'./'+name + '.pkl', 'rb') as f:
        return pickle.load(f)

def get_config(path_yml):
    return config(Params(path_yml))

def get_path_data(cfg, phase='train'):
    list_image_name = []
    list_mask_name = []

    if phase == 'train' or phase == 'valid':
        print('phase가 train, val일 때 라벨 파일을 기준으로 이미지 불러옴')
        list_file_name = os.listdir(f'{cfg.path_data}/{cfg.path_label}') # 라벨 경로로 바꿈                    # 'abc.' + {'jpg', 'jpeg', 'png', ... }
    elif phase == 'test':
        list_file_name = os.listdir(f'{cfg.test_data_dir}/{cfg.test_image_dir}')                                                      # 'abc.' + {'jpg', 'jpeg', 'png', ... }

    if phase=='test':
        if cfg.test_mode == 'with_gt':
            for file_name in sorted(list_file_name):
                img_paths = os.path.join(cfg.test_data_dir, cfg.test_image_dir, file_name)
                mask_paths = os.path.join(cfg.test_data_dir, cfg.test_label_dir, file_name)
                list_image_name.append(img_paths)                                                             # 'path_data/path_image/abc.' + {'jpg', 'jpeg', 'png', ... }
                list_mask_name.append(mask_paths)                                                             # 'path_data/path_label/abc.png'
        else:
            for file_name in sorted(list_file_name):
                list_image_name.append(f'{cfg.test_data_dir}/{cfg.test_image_dir}/{file_name}')                   # 'path_data/path_image/abc.' + {'jpg', 'jpeg', 'png', ... }
            list_mask_name = np.zeros(len(list_image_name), dtype='uint8')
        return np.stack(list_image_name), np.stack(list_mask_name)

    else:
        for file_name in sorted(list_file_name):
            if os.path.isfile(f'{cfg.path_data}/{cfg.path_label}/{os.path.splitext(file_name)[0]}.png'): ####### modified
                list_image_name.append(f'{cfg.path_data}/{cfg.path_image}/{file_name}')                   # 'path_data/path_image/abc.' + {'jpg', 'jpeg', 'png', ... }
                list_mask_name.append(f'{cfg.path_data}/{cfg.path_label}/{os.path.splitext(file_name)[0]}.png')  # 'path_data/path_label/abc.png'

        len_train = int(len(list_mask_name) - (len(list_mask_name)*cfg.valid_split))
        list_image_name = list_image_name[:len_train] if phase == 'train' else list_image_name[len_train:]
        list_mask_name = list_mask_name[:len_train] if phase == 'train' else list_mask_name[len_train:]
    
        return np.stack(list_image_name), np.stack(list_mask_name)

def get_range(cfg):
    return cfg['range']# if cfg['apply'] else dict_not_apply['']

def get_current_time():
    timezone = pytz.timezone('Asia/Seoul')
    ymd, hms = str(datetime.datetime.fromtimestamp(time.time(), timezone)).split(' ')

    year, month, day = ymd.split('-')
    hour, minute, sec = hms.split('+')[0].split('.')[0].split(':')

    return year, month, day, hour, minute, sec

def get_save_name(path_save, model_name):
    list_weight_name = os.listdir(path_save)
    
    year, month, day, hour, minute, sec = get_current_time()
    base_name = f'{year[-2:]}{month}{day}_{model_name}'
    
    cnt = 1
    while True:
        if not len([weight_name for weight_name in list_weight_name if f'{base_name}_{cnt:02d}' in weight_name]):
            break
        cnt += 1
    
    return f'{base_name}_{cnt:02d}'

cmap = load_obj('cmap_of_pascal')
def decode_segmap(image):
    return cmap[image]
    
from PIL import Image

palette = Image.new('P', (512, 512))
palette.putpalette(cmap)
    
def to_palette(mask):
    return mask.quantize(palette=self.palette)
    
def save_predict(epoch, image, label, pred, save_name, img_name='', path_test=None, test_name=None, flag_merge=True, phase = 'train', cfg=None):
    img_name = img_name.split('.')[0]
    img_copy = image.copy()
    image = cv2.putText(image, 'Input', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 255), 2) ##
    
    pred = torch.argmax(pred, dim=0).detach().cpu().numpy()
    pred_copy2 = pred.copy()
    pred_copy = decode_segmap(pred).copy()
    if flag_merge:
        pred = cv2.cvtColor(decode_segmap(pred), cv2.COLOR_RGB2BGR) ##
        pred = cv2.putText(pred, 'Pred', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 255), 2) ##

    if phase != 'test':
        if type(label) != type(None):
            label = label.cpu().numpy().astype('uint8')
            label = cv2.cvtColor(decode_segmap(label), cv2.COLOR_RGB2BGR) ##
            label = cv2.putText(label, 'True', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 255), 2) ##
    
            merged_results = np.concatenate((image, label, pred), axis=1) ##
        else:
            if flag_merge:
                merged_results = np.concatenate((image, pred), axis=1) ##

    if phase == 'train' or phase == 'valid':
        save_dir = f'{cfg.path_train_output}'
    elif phase == 'test':
        save_dir = f'{cfg.test_output_dir}/logs'

    if phase != 'test':
        if test_name is None:
            cv2.imwrite(f'{save_dir}/visualize/{save_name}/img_name_{epoch:03d}.jpg', merged_results)
        else:
            if flag_merge:
                cv2.imwrite(f'{path_test}/{os.path.basename(test_name)}', merged_results)
            else:
                to_palette(Image.fromarray(pred.astype('uint8'))).save(f'{path_test}/{os.path.splitext(os.path.basename(test_name))[0]}.png')

    # cv2.imwrite('temp.jpg', pred)
    # exit()
    # h, w, c = pred_copy.shape
    pred_copy_sirloin_where = np.where(pred_copy2[:,:] == 1)
    for y, x in zip(pred_copy_sirloin_where[0], pred_copy_sirloin_where[1]):  # sirloin convert
        pred_copy[y, x, :] = np.array([0,255,0])

    pred_copy_backfat_where = np.where(pred_copy2[:,:] == 2)
    for y, x in zip(pred_copy_backfat_where[0], pred_copy_backfat_where[1]):  # sirloin convert
        pred_copy[y, x, :] = np.array([255, 0, 0])

    os.makedirs(f'{save_dir}/visualize_overlay/{save_name}/img', exist_ok = True)
    os.makedirs(f'{save_dir}/visualize_overlay/{save_name}/pred', exist_ok = True)
    os.makedirs(f'{save_dir}/visualize_overlay/{save_name}/overlay', exist_ok = True)

    overlay_img = cv2.addWeighted(img_copy, 0.5, pred_copy, 0.5, 0)
    cv2.imwrite(f'{save_dir}/visualize_overlay/{save_name}/img/{img_name}_{epoch:03d}.jpg', img_copy)
    cv2.imwrite(f'{save_dir}/visualize_overlay/{save_name}/pred/{img_name}_{epoch:03d}.jpg', pred_copy)
    cv2.imwrite(f'{save_dir}/visualize_overlay/{save_name}/overlay/{img_name}_{epoch:03d}.jpg', overlay_img)

def without_crop(transform):
    return A.Compose(transform[-2:])
       
def calc_miou(y_true, y_pred, num_classes, mode='each', each_iou=False): # iou를 각각 구하려고 추가함
    per_batch_miou = 0
    cnt_calculated = 0

    for temp_true, temp_pred in zip(y_true, y_pred):
        temp_pred = temp_pred.permute((1,2,0)).argmax(-1)
        temp_classes = len(torch.unique(temp_true))
        
        if (temp_classes == 1):
            continue
        
        per_image_miou = 0
        iou_list = []
        for j in range(1,temp_classes):
            per_image_miou += torch.sum((temp_true==j)&(temp_pred==j))/(torch.sum((temp_true==j)|(temp_pred==j))+1e-16)
            iou_list.append((torch.sum((temp_true==j)&(temp_pred==j))/(torch.sum((temp_true==j)|(temp_pred==j))+1e-16)).item())

        per_batch_miou += per_image_miou/(temp_classes-1)
        cnt_calculated += 1

    if each_iou == True: # iou를 각각 구하려고 추가함
        if cnt_calculated > 0:
            return per_batch_miou.item(), cnt_calculated, iou_list
        else:
            return per_batch_miou, cnt_calculated, iou_list

    if cnt_calculated > 0:
        return per_batch_miou.item(), cnt_calculated
    else:
        return per_batch_miou, cnt_calculated

def get_denormed_img(image, cfg):
    image = image.detach().cpu().numpy().transpose(1,2,0)
    image = (((image*cfg.dataset_std)+cfg.dataset_mean)*255).astype('uint8')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    return image
    
  