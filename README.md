# 2023-1-CECD2-AImport-7

<팀원>\
2020112119 강동희\
2018112558 김철희\
2018112007 이승현

## Segmentation 사용법 (Linux 기준)
- 참고 사이트: (https://github.com/open-mmlab/mmsegmentation/blob/main/docs/en/get_started.md)
- 윈도우의 경우 0~2, 4과정의 경우 Annaconda의 conda prompt 사용을 추천드립니다.
- Mac의 경우 아직 테스트를 못했습니다. 추후에 확인해주시면 감사하겠습니다!

0. (선택사항) Ananconda 가상환경 설정 (PyTorch)
    - conda create --name openmmlab python=3.8 -y
    - conda activate openmmlab
    - CUDA ver: conda install pytorch torchvision -c pytorch
    - CPU only: conda install pytorch torchvision cpuonly -c pytorch

1. 다음 명령어를 통해 MMCV 설치
    - pip install -U openmim
    - mim install mmengine
    - mim install "mmcv>=2.0.0"

2. MMSegmentaion GitHub Repo(https://github.com/open-mmlab/mmsegmentation) 에서 git clone하여 local에 설치
    - git clone -b main https://github.com/open-mmlab/mmsegmentation.git
    - cd mmsegmentation
    - pip install -v -e .

3. Pre-trained 모델을 저장할 디렉토리 생성 및 모델 다운로드
    - mkdir ./checkpoints
    - wget https://download.openmmlab.com/mmsegmentation/v0.5/deeplabv3plus/deeplabv3plus_r101-d8_512x512_20k_voc12aug/deeplabv3plus_r101-d8_512x512_20k_voc12aug_20200617_102345-c7ff3d56.pth -P ./checkpoints
    - (윈도우의 경우) 직접 checkpoints 폴더 생성 및 위의 링크에 직접 들어가 pre-trained 모델 다운로드하여 checkpoints 폴더 안에 옮겨주세요.

4. sementaion.py 실행 (clone한 mmsegmentation 파일 안에서 실행 필요)
    - python segmentation.py -i put_your_path_to_img.jpg (segmentaition 원하는 이미지파일 경로)
  

## ldraw-parts library를 ubuntu에서 설치하는 방법
  1. sudo apt-get update -y
  2. sudo apt-get install -y ldraw-parts
  3. site : https://library.ldraw.org/updates?latest
  4. 만약 lpub3d에서 part library를 못 찾는 경우 /usr/share/ldraw로 폴더 지정
     
## lpub3d를 ubuntu에서 설치하는 방법(20.04 LTS 기준) ->  https://software.opensuse.org//download.html?project=home%3Atrevorsandy&package=lpub3d  
  1. echo 'deb http://download.opensuse.org/repositories/home:/trevorsandy/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:trevorsandy.list
  2. curl -fsSL https://download.opensuse.org/repositories/home:trevorsandy/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_trevorsandy.gpg > /dev/null
  3. sudo apt update
  4. sudo apt install lpub3d

- lpub3d -> ldraw-parts library 순으로 설치.

## Requirement.txt 관련
- 'pip freeze > requirement.txt'
