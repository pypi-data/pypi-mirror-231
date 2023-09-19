import cv2
import json
import numpy as np
import albumentations as A
from albumentations.pytorch import ToTensorV2
import os

from utils import get_range

dict_interpolation  = {'Nearest'    : 0,  # cv2.INTER_NEAREST
                       'Linear'     : 1,  # cv2.INTER_LINEAR
                       'Bicubic'    : 2,  # cv2.INTER_CUBIC
                       'Area'       : 3,  # cv2.INTER_AREA
                       'Lanczos'    : 4}  # cv2.INTER_LANCZOS4
                      
dict_border_mode    = {'Constant'   : 0,  # cv2.BORDER_CONSTANT
                       'Replicate'  : 1,  # cv2.BORDER_REPLICATE
                       'Reflect'    : 2,  # cv2.BORDER_REFLECT
                       'Wrap'       : 3,  # cv2.BORDER_WRAP
                       'Reflect101' : 4}  # cv2.BORDER_REFLECT_101

## should be automatic method
def get_transform(cfg):
    if type(cfg.input_size) is int:
        input_shape = (cfg.input_size, cfg.input_size)
    else:
        cfg.input_size = eval(cfg.input_size)
        input_shape = (cfg.input_size[0], cfg.input_size[1])

    ## json parsing from path_aug
    with open(f'{os.path.dirname(__file__)}/{cfg.path_aug}') as json_file:
        json_decoded = json.load(json_file)
    
    p = json_decoded['Probability']

    ## Inversion
    aug_inversion = []
    if json_decoded['Inversion']['Mirror']:
        aug_inversion.append(A.HorizontalFlip(p=p))
        
    if json_decoded['Inversion']['Flip']:
        aug_inversion.append(A.VerticalFlip(p=p))

    if json_decoded['Inversion']['Transpose']:
        aug_inversion.append(A.Transpose(p=p))
    
    
    ## AffineTransform
    aug_affine = []
    aug_affine.append(A.ShiftScaleRotate(get_range(json_decoded['AffineTransform']['Shift']),
                                         get_range(json_decoded['AffineTransform']['Zoom']), 
                                         get_range(json_decoded['AffineTransform']['Rotation']), 
                                         dict_interpolation[cfg.interpolation],
                                         dict_border_mode[json_decoded['BorderMode']], p=p))
    
    ## Fit
    aug_fit = []
    if json_decoded['RandomCrop']:
        aug_fit.append(A.RandomCrop(input_shape[0],
                                    input_shape[1],
                                    always_apply=True))
    
    else:
        aug_fit.append(A.Resize(input_shape[0], 
                                input_shape[1],
                                dict_interpolation[cfg.interpolation],
                                always_apply=True))
    
    ## ColorAdjustment
    aug_color = []
    aug_color.append(A.ColorJitter(get_range(json_decoded['ColorAdjustment']['Brightness']),
                                   get_range(json_decoded['ColorAdjustment']['Contrast']),
                                   get_range(json_decoded['ColorAdjustment']['Saturation']),
                                   get_range(json_decoded['ColorAdjustment']['Hue']), p=p)) # Customized
    
    
    ## Filter
    aug_filter = []
    aug_filter.append(A.GaussNoise(get_range(json_decoded['Filter']['Noise']), p=p))
    aug_filter.append(A.GaussianBlur((3,3), p=p)) ## get_range(json_decoded['Filter']['Smoothing']) # UserWarning

    
    ## Base
    aug_base = []
    aug_base.append(A.Normalize(cfg.dataset_mean,
                                cfg.dataset_std,
                                cfg.dataset_max,
                                always_apply=True))
    
    aug_base.append(ToTensorV2())


    transform_train = A.Compose([A.Resize(input_shape[0], 
                                input_shape[1],
                                dict_interpolation[cfg.interpolation], always_apply=True),
                                              
                                # A.ColorJitter(),
                                # A.MultiplicativeNoise(multiplier=(0.9, 1.1), always_apply=False, p=1.0),
                                # A.Blur((3,5), always_apply=False, p=1.0),
                                # A.MotionBlur((3,5), always_apply=False, p=1.0),
                                A.ShiftScaleRotate(shift_limit=0.15, scale_limit=0.1, rotate_limit=30, border_mode=cv2.BORDER_CONSTANT, p=0.5),
                                A.Normalize(cfg.dataset_mean,
                                                cfg.dataset_std,
                                                cfg.dataset_max,
                                                always_apply=True),
                                ToTensorV2(),
                              ], p=1.0)
    
    transform_valid = A.Compose([ A.Resize(input_shape[0], 
                                        input_shape[1],
                                        dict_interpolation[cfg.interpolation],
                                        always_apply=True),
                                A.Normalize(cfg.dataset_mean,
                                              cfg.dataset_std,
                                              cfg.dataset_max,
                                              always_apply=True),
                                  ToTensorV2(),
                                ], p=1.0)

    
    ## Set Transforms
    #transform_train = A.Compose(aug_fit+aug_inversion+aug_affine+aug_color+aug_filter+aug_base)
    #transform_valid = A.Compose(aug_fit+aug_base)
    
    transforms = {'train': transform_train,
                  'valid': transform_valid }
    
    return transforms


def letter_boxing(image, mask=None):
    max_border = max(image.shape[0], image.shape[1])
    letter_boxed = np.zeros((max_border, max_border, image.shape[-1]), dtype='uint8')
    
    xmin = np.random.randint(max_border-image.shape[1]) if max_border > image.shape[1] else 0
    ymin = np.random.randint(max_border-image.shape[0]) if max_border > image.shape[0] else 0
    
    letter_boxed[ymin:ymin+image.shape[0], xmin:xmin+image.shape[1]] = image
    
    if mask is None:
        return letter_boxed 
    else:
        letter_boxed_mask = np.zeros((max_border, max_border), dtype='uint8')
        letter_boxed_mask[ymin:ymin+mask.shape[0], xmin:xmin+mask.shape[1]] = mask
        
        return letter_boxed, letter_boxed_mask