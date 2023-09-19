import torch
import torch.nn.functional as F

def _predict(model, image, label, model_type, phase):        
    if model_type == 'SETR':
        pred = model(img=image, gt_semantic_seg=label, img_metas=None)
        pred = torch.chunk(pred, chunks=5, dim=0)
    else:
        pred = model(image)

    return pred


def _criterion(criterion, pred, label, model_type, phase):
    if model_type == 'STDCSeg':
        if phase == 'train':
            H, W = label.size()[2:]
            out, out16, out32, detail8 = pred
            out = F.interpolate(out, (H, W), mode='bilinear', align_corners=True)
            out16 = F.interpolate(out16, (H, W), mode='bilinear', align_corners=True)
            out32 = F.interpolate(out32, (H, W), mode='bilinear', align_corners=True)
        
            lossp = criterion[0](out, label)
            loss2 = criterion[1](out16, label)
            loss3 = criterion[2](out32, label)
            
            boundery_bce_loss8,  boundery_dice_loss8 = criterion[3](detail8, label)
            
            loss = lossp + loss2 + loss3 + boundery_bce_loss8 + boundery_dice_loss8
        else:
            loss = None
    
    else:
        loss = criterion(pred, label).mean()
    
    return loss

def _metric(metric, label, pred, num_classes, model_type, phase, each_iou=False):
    if model_type == 'STDCSeg':
        if phase == 'train':
            metric_results = [None, len(pred)]
        else:
            metric_results = metric(label, pred, num_classes, each_iou=each_iou)

    else:
        metric_results = metric(label, pred, num_classes, each_iou=each_iou)
    
    return metric_results