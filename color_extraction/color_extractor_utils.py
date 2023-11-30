import cv2
import numpy as np

# 컬러 매칭 테이블 정의 (각 컬러와 RGB 값)
color_table = {
    'Black': (0, 0, 0),
    'White': (255, 255, 255),
    'Red': (205, 0, 0),
    'Green': (0, 153, 0),
    'Blue': (0, 102, 204),
    'Yellow': (255, 255, 0),
    'Orange': (255, 128, 0),
    'Brown': (128, 64, 0),
    'Purple': (128, 0, 128),
    'Pink': (255, 105, 180),
}

def color_extractor(segImg):
    # 이미지 크기 확인
    if segImg.shape[0] <= 500 and segImg.shape[1] <= 500:
        # 이미지 크기가 500x500 이하이면 원본 이미지 사용
        dst = segImg
    else:
        # 이미지 크기가 500x500보다 크면 리사이즈
        dst = cv2.resize(segImg, dsize=(0, 0), fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)

    # 리사이즈한 이미지의 크기에 맞는 빈 행렬 생성
    result_matrix = np.full((dst.shape[0], dst.shape[1]), 0, dtype=object)

    # dst의 이미지의 색상을 추출하여 color name을 result_matrix에 저장
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
