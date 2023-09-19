import os
import json
import numpy as np
from PIL import Image, ImageOps

import torch
from torch.utils.data import Dataset

from pycocotools import mask as mask_tool

from transforms import letter_boxing

import cv2
import albumentations as A

class NAVANG_MARS_Dataset(Dataset):
    def __init__(self, path_images, each_labels, transform, cfg, phase):
        self.path_images = path_images
        self.each_labels = each_labels
        self.transform = transform
        
        self.length = len(each_labels)
        self.sampling_factor = cfg.sampling_factor
        self.cfg = cfg
        
        self.phase = phase
    
    def __getitem__(self, index):
        image = Image.open(self.path_images[index%len(self.each_labels)]).convert('RGB')
        img_name = self.path_images[index%len(self.each_labels)].split('/')[-1]
        # image = Image.open(self.path_images[index]).convert('RGB')
        image = ImageOps.exif_transpose(image)
        image = np.uint8(image)
        
        if (self.phase == 'test') and (self.cfg.test_mode == 'without_gt'):
            #image = letter_boxing(image)
            augmented_data = self.transform(image=image)

            return augmented_data['image'].float(), torch.tensor([0]), img_name
        
        else:
            if self.cfg.label_type in ['navi', 'pascal']:
                mask = np.int16(Image.open(self.each_labels[index%len(self.each_labels)]))

            elif self.cfg.label_type == 'ai_gov':
                with open(self.each_labels[index%len(self.each_labels)]) as json_file:
                    json_decoded = json.load(json_file)
                
                if type(json_decoded['annotations']) == list:
                    json_decoded['annotations'] = json_decoded['annotations'][0]
                
                mask = np.zeros(image.shape[:2], dtype='int16')
                for polygon in json_decoded['annotations']['polygon']:
                    mask = cv2.fillPoly(mask, [np.int32(polygon['points'])], (1,))

            elif self.cfg.label_type == 'coco':
                with open(self.each_labels[index%len(self.each_labels)]) as json_file:
                    json_decoded = json.load(json_file)
                
                mask = np.zeros(image.shape[:2], dtype='int16')
                for annotation in json_decoded['annotations']:
                    if 'segmentation' in annotation:
                        if type(annotation['segmentation']) == list:
                            mask = cv2.fillPoly(mask, [np.int32(annotation['segmentation'])], (annotation['categori_id'],))
                            
                        elif type(annotation['segmentation']) == dict:
                            encoded_mask = mask_tool.frPyObjects(annotation['segmentation'], annotation['segmentation']['size'][0], annotation['segmentation']['size'][1])
                            decoded_mask = mask_tool.decode(encoded_mask).astype('int16')*annotation['categori_id']
                            mask[decoded_mask!=0] = decoded_mask[decoded_mask!=0]
                            
                        else:
                            print(type(annotation['segmentation']))
                            print(annotation['segmentation'])
                            exit()
            
            else:
                print('label_type should be in {navi, coco, pascal, ai_gov}')
                print('you should grow up.')
                exit()
            
            augmented_data = self.transform(image=image, mask=mask)
            
            return augmented_data['image'].float(), augmented_data['mask'].long(), img_name

    def __len__(self):
        return int(self.length*self.sampling_factor) if self.phase == 'train' else self.length