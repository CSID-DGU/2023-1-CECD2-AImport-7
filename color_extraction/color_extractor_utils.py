import cv2
import numpy as np
import color_table

def color_extractor(segImg):

    # 이미지 크기 가져오기
    height, width, _ = segImg.shape

    # RGB에서 BGR로 변환 (이미지 분할된 원본 이미지)
    segCV = cv2.cvtColor(segImg, cv2.COLOR_RGB2BGR)

    # 그레이스케일로 변환
    gray = cv2.cvtColor(segImg, cv2.COLOR_BGR2GRAY)

    # 엣지 검출 (Canny 알고리즘 사용)
    edges = cv2.Canny(gray, threshold1=30, threshold2=100)

    # 객체 내부의 픽셀에 대한 마스크 생성
    object_mask = np.zeros_like(edges)
    object_mask[edges != 0] = 1

    # 결과 행렬 초기화
    result_matrix = np.full((height, width), None, dtype=object)

    # 객체 내부 색상 추출 및 매칭
    for y in range(height):
        for x in range(width):
            if object_mask[y, x] == 1:
                pixel = segCV[y, x]
                closest_color = min(color_table, key=lambda color: np.linalg.norm(np.array(color_table[color]) - np.array(pixel)))
                result_matrix[y, x] = closest_color
    
    # Numpy 형식의 color matrix 반환
    return result_matrix
