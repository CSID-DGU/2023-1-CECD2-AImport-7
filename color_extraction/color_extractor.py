import cv2
import numpy as np

# 이미지 파일 경로
image_path = "./test.jpeg"
# 결과 행렬을 저장할 파일 경로
output_path = "final_result1.txt"

# 컬러 매칭 테이블 정의 (각 컬러와 RGB 값)
color_table = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'orange': (255, 165, 0),
    'green': (0, 128, 0),
    'blue': (0, 0, 255),
    'gray': (128, 128, 128),
    'purple': (128, 0, 128),
    'sky_blue': (0, 191, 255)
}

# 이미지를 엽니다.
image = cv2.imread(image_path)

# 이미지 크기 가져오기
height, width, _ = image.shape

# 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
            pixel = image[y, x]
            closest_color = min(color_table, key=lambda color: np.linalg.norm(np.array(color_table[color]) - np.array(pixel)))
            result_matrix[y, x] = closest_color

# 결과 행렬을 텍스트 파일로 저장
with open(output_path, 'w') as file:
    for row in result_matrix:
        file.write(' '.join(map(str, row)) + '\n')

print("Done.")
