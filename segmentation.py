# Check Pytorch installation
import torch, torchvision

# Check MMSegmentation installation
import mmseg

import matplotlib.pyplot as plt
from mmengine.model.utils import revert_sync_batchnorm
from mmseg.apis import init_model, inference_model, show_result_pyplot
from mmengine.structures import PixelData
from mmseg.structures import SegDataSample

import argparse
import numpy as np
import cv2
from PIL import Image

class_label = {'aero':1, 'bird':3, 'car':7, 'cat':8, 'person':15, 'sheep':17, 'sofa':18}

def image_segmentation(inputImgPath, configPath, checkpointPath, label): 
    device = None

    if torch.cuda.is_available():
        device = 'cuda'
        print("CUDA available")
    else:
        device = 'cpu'
        print("CPU mode runs")

    # configPath = './configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-20k_voc12aug-512x512.py'
    # checkpointPath = './checkpoints/deeplabv3plus_r101-d8_512x512_20k_voc12aug_20200617_102345-c7ff3d56.pth'

    # build the model from a config file and a checkpoint file
    model = init_model(configPath, checkpointPath, device=device) # cuda to cpu

    # test a single image
    if not torch.cuda.is_available():
        model = revert_sync_batchnorm(model)
    result = inference_model(model, inputImgPath)

    predPixel = None

    # Take every pixel with class
    for k, v in result.items():
        if k == 'pred_sem_seg':
            predPixel = v

    # Convert pixel data type into numpy
    predPixelToNp = predPixel.numpy()

    # Get label infos and squeeze the dimension of pixel numpy
    pixelInfo = np.squeeze(predPixelToNp.values())

    # Get original image
    originalImg = Image.open(inputImgPath)

    copyImgPNG = np.array(originalImg.convert('RGBA'))

    # Set alpha value as 100 if the label of pixel is not the class wanted
    for i in range(pixelInfo.shape[0]):
        for j in range(pixelInfo.shape[1]):
            
            # EDIT NEEDED!! class 8 disignates a label of 'cat'
            # EDIT NEEDED!! class 7 disignates a label of 'car'
            # EDIT NEEDED!! class 15 disignates a label of 'person'
            
            if pixelInfo[i][j] != class_label[label]:
                copyImgPNG[i, j, 3] = 0

    # return PNG img in numpy type
    return copyImgPNG

if __name__ == '__main__':
    
    # Set Argument parser
    parser = argparse.ArgumentParser(description='Convert JPEG to PNG and set alpha value for white pixels.')
    parser.add_argument('--input', '-i', type=str, required=True, help='Path to the input image.')
    parser.add_argument('--config', '-c', type=str, required=True, help='Path to mmseg python config file')
    parser.add_argument('--check', '-k', type=str, required=True, help='Path to pre-trained checkpoint model')
    
    args = parser.parse_args()

    image_segmentation(args.input)