import cv2
import json
import numpy as np
import time
import copy
import os
import glob

def resizeToMultiple(img, unitSize=128):
    new_h, new_w = 0, 0
    h, w = img.shape[:2]

    a = h%unitSize
    if a == 0: new_h = h
    else: new_h = h + (unitSize - a)

    a = w%unitSize
    if a == 0: new_w = w
    else: new_w = w + (unitSize - a)

    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)

def makeMiniPatch(img, unitSize=256):
    h, w = img.shape[:2]
    len_h_patch = h // unitSize; len_w_patch = w // unitSize
    img_patches = []
    for i in range(len_h_patch):
        w_patches = []
        for j in range(len_w_patch):
            w_patches.append(np.array([img[i * unitSize:(i + 1) * unitSize, j * unitSize: (j + 1) * unitSize]]))
            # w_patches.append([j])
        img_patches.append(w_patches)

    return img_patches, len_h_patch, len_w_patch

def preprocessing_miniPatch(image=None, mask=None, unitSize=256):
    '''
    :param image: original image, 3D numpy array
    :param mask: mask, 1D numpy array
    :param unitSize: patch size, int
    :return: list, ex) [[numpy array], [numpy array] ...]
    '''

    h, w = image.shape[:2]
    mask = cv2.resize(mask, (w, h))
    mask_3d = cv2.merge((mask, mask, mask))
    image_and_mask = cv2.bitwise_and(image, mask_3d)

    mask_where = np.where(mask > 0) # y, x
    x_min = min(mask_where[1])
    x_max = max(mask_where[1])
    y_min = min(mask_where[0])
    y_max = max(mask_where[0])

    face_RoI = image_and_mask[y_min : y_max, x_min : x_max]
    face_RoI_rsz = resizeToMultiple(face_RoI, unitSize=unitSize)
    miniPatches, num_h_patch, num_w_patch = makeMiniPatch(face_RoI_rsz, unitSize=unitSize)

    return image_and_mask, miniPatches


if __name__ == '__main__':
    preprocessing_miniPatch()







