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


def image_segmentation(inputImgPath): 
    device = None

    if torch.cuda.is_available():
        device = 'cuda'
    else:
        device = 'cpu'

    # EDIT NEEDED!! -> To argparse
    config_file = './configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-20k_voc12aug-512x512.py'
    checkpoint_file = './checkpoints/deeplabv3plus_r101-d8_512x512_20k_voc12aug_20200617_102345-c7ff3d56.pth'

    # build the model from a config file and a checkpoint file
    model = init_model(config_file, checkpoint_file, device=device) # cuda to cpu

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
            if pixelInfo[i][j] != 8:
                copyImgPNG[i, j, 3] = 100

    # Convert numpy into PIL Image
    imgPNGDone = Image.fromarray(copyImgPNG, 'RGBA')
    # imgPNGDone.show()

    # Save as a PNG Image file
    imgPNGDone.save("./demo/cat_demo_done.png")
    print('Image saved done!!')

    # return PNG img in PIL Image type
    return imgPNGDone


if __name__ == '__main__':
    
    # Set Argument parser
    parser = argparse.ArgumentParser(description='Convert JPEG to PNG and set alpha value for white pixels.')
    parser.add_argument('--input', '-i', type=str, required=True, help='Path to the input image.')
    
    args = parser.parse_args()

    image_segmentation(args.input)