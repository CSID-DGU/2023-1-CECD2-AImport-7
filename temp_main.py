'''
Initial merge: 2023.09.17 by AImport
Last merge: 2023.09.17 by AImport
'''

from segmentation import image_segmentation # ! EDIT: 폴더명 추후에 변경 필요
from color_extraction.color_extractor_utils import color_extractor # ! EDIT: 폴더명 추후에 변경 필요
import assemble.auto_gene as mangen # ! EDIT: 폴더명 추후에 변경 필요

import argparse
from PIL import Image

# Set Argument parser
parser = argparse.ArgumentParser(description='Convert JPEG to PNG and set alpha value for white pixels.')
parser.add_argument('--label', '-l', type=str, required=True, help='cartegory of the object: 1.aero, 2.bicycle, ...')
parser.add_argument('--input', '-i', type=str, required=True, help='Path to the input image.')
parser.add_argument('--config', '-c', default='./mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-20k_voc12aug-512x512.py', 
                    type=str, required=False, help='Path to mmseg python config file') # ! EDIT: Defult dir should be edited...
parser.add_argument('--check', '-k', default='./mmsegmentation/checkpoints/deeplabv3plus_r101-d8_512x512_20k_voc12aug_20200617_102345-c7ff3d56.pth', 
                    type=str, required=False, help='Path to pre-trained checkpoint model')# ! EDIT: Defult dir should be edited...
parser.add_argument('--output', '-o', type=str, required=True, help='PDF or PNG') # ! EDIT: Add 'LDraw' later!!

args = parser.parse_args()

# Get segmented image
segPNG = image_segmentation(args.input, args.config, args.check, args.label)

# ! DEBUG: Convert numpy into PIL Image 
imgPNGDone = Image.fromarray(segPNG, 'RGBA')

# ! DEBUG: Save as a PNG Image file
imgPNGDone.save("./segmented.png")
print('Image saved done!!')

# Get color matrix from the segmented image (numpy)
colorMatrix = color_extractor(segPNG)

# ! DEBUG: 결과 행렬을 저장할 파일 경로
output_path = "color_matrix.txt"

# ! DEBUG: 결과 행렬을 텍스트 파일로 저장
with open(output_path, 'w') as file:
    for row in colorMatrix:
        file.write(' '.join(map(str, row)) + '\n')

# Get complete manual as a result
# ! EDIT: 1. 절대경로명 사용 예정, 2. 저장될 LDraw 이름 -> 오늘 날짜와 생성 시간
mangen.pixelTomanual(colorMatrix, '/home/paralies/sandbox/output', '/home/paralies/sandbox/output', args.output)