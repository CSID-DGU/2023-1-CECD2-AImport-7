import cv2
import numpy as np

color_table = {
    'Black': (0, 0, 0),
    'White': (255, 255, 255),
    'Red': (205, 0, 0),
    'Bright_Red': (255, 0, 0),
    'Green': (0, 153, 0),
    'Bright_Green': (0, 255, 0),
    'Blue': (0, 102, 204),
    'Bright_Blue': (0, 204, 255),
    'Yellow': (255, 255, 0),
    'Bright_Yellow': (255, 255, 102),
    'Orange': (255, 128, 0),
    'Bright_Orange': (255, 160, 10),
    'Brown': (128, 64, 0),
    'Light_Brown': (210, 105, 30),
    'Tan': (218, 165, 32),
    'Dark_Tan': (136, 84, 24),
    'Dark_Grey': (169, 169, 169),
    'Light_Grey': (211, 211, 211),
    'Dark_Bluish_Grey': (89, 89, 89),
    'Light_Bluish_Grey': (155, 155, 155),
    'Purple': (128, 0, 128),
    'Pink': (255, 105, 180),
    'Lime': (50, 205, 50),
    'Lime_Green': (50, 205, 50),
}

def color_extractor(segImg):

    #segImg의 크기를 상대크기로 줄이기
    dst = cv2.resize(segImg, dsize=(0,0), fx=0.05, fy=0.05,  interpolation=cv2.INTER_AREA)

    #resize한 이미지의 크기에 맞는 빈 행렬 생성
    result_matrix = np.full((dst.shape[0], dst.shape[1]), 0, dtype=object)

    #dst의 이미지의 색상을 추출하여 color name을 result_matrix에 저장
    for y in range(dst.shape[0]):
        for x in range(dst.shape[1]):
            pixel = dst[y, x]
            # 배경이 None일 때는 None을 그대로 저장
            if pixel[3] == 0:
                result_matrix[y, x] = None
            else:
                closest_color = min(color_table, key=lambda color: np.linalg.norm(np.array(color_table[color]) - np.array(pixel)[:3]))
                result_matrix[y, x] = closest_color

    # Numpy 형식의 color matrix 반환
    return result_matrix