import cv2
import numpy as np

color_table = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'orange': (255, 165, 0),
    'green': (0, 128, 0),
    'blue': (0, 0, 255),
    'gray': (128, 128, 128),
    'purple': (128, 0, 128),
    'sky_blue': (0, 191, 255),
    'yellow': (255, 255, 0),
    'pink': (255, 192, 203),
    'brown': (165, 42, 42),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'olive': (128, 128, 0),
    'lime': (0, 255, 0),
    'teal': (0, 128, 128),
    'navy': (0, 0, 128),
    'silver': (192, 192, 192),
    'maroon': (128, 0, 0),
    'fuchsia': (255, 0, 255),
    'aqua': (0, 255, 255),
    # 추가 색상을 여기에 계속 추가하세요
}

def color_extractor(segImg):

    image = cv2.imread(segImg)


    #segImg의 크기를 상대크기로 줄이기
    dst = cv2.resize(image, dsize=(0,0), fx=0.05, fy=0.05,  interpolation=cv2.INTER_AREA)
    

    #resize한 이미지의 크기에 맞는 빈 행렬 생성
    result_matrix = np.full((dst.shape[0], dst.shape[1]), 0, dtype=object)

    #dst의 이미지의 색상을 추출하여 color name을 result_matrix에 저장
    for y in range(dst.shape[0]):
        for x in range(dst.shape[1]):
            pixel = dst[y, x]
            # 배경이 None일 때는 None을 그대로 저장
            if pixel is None:
                result_matrix[y, x] = None
            else:
                closest_color = min(color_table, key=lambda color: np.linalg.norm(np.array(color_table[color]) - np.array(pixel)[:3]))
                result_matrix[y, x] = closest_color

    # Numpy 형식의 color matrix 반환
    return result_matrix