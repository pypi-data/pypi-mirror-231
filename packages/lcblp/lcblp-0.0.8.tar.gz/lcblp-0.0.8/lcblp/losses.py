import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

def cross_entropy2d(pred, target, weight=None, reduction='mean', flag_aux=False, list_loss_weight=None):
    temp_target = target
    nt, ht, wt = temp_target.size()
    temp_target = temp_target.view(-1)
    
    if flag_aux:
        loss = 0.
        for head, loss_weight in zip(pred, list_loss_weight):
            temp_pred = head
            n, c, h, w = temp_pred.size()
            if h != ht and w != wt:  # upsample labels
                temp_pred = F.interpolate(temp_pred, size=(ht, wt), mode="bilinear", align_corners=False) # True

            temp_pred = temp_pred.transpose(1, 2).transpose(2, 3).contiguous().view(-1, c)
            
            loss += F.cross_entropy(temp_pred, temp_target, weight=weight, reduction=reduction, ignore_index=250)*loss_weight
    
    else:
        temp_pred = pred
        n, c, h, w = temp_pred.size()
        print("temp_target.shape :", temp_target.shape)
        print("temp_target.size() :", temp_target.size())
        if h != ht and w != wt:  # upsample labels
            temp_pred = F.interpolate(temp_pred, size=(ht, wt), mode="bilinear", align_corners=False)

        temp_pred = temp_pred.transpose(1, 2).transpose(2, 3).contiguous().view(-1, c)
        
        loss = F.cross_entropy(temp_pred, temp_target, weight=weight, reduction=reduction, ignore_index=250)
        
    return loss
        