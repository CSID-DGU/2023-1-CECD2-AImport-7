## ldraw-parts library를 ubuntu에서 설치하는 방법
  1. sudo apt-get update -y
  2. sudo apt-get install -y ldraw-parts

## lpub3d를 ubuntu에서 설치하는 방법(20.04 LTS 기준)
  - 자세한 정보는 https://software.opensuse.org//download.html?project=home%3Atrevorsandy&package=lpub3d
  
  1. echo 'deb http://download.opensuse.org/repositories/home:/trevorsandy/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:trevorsandy.list
  2. curl -fsSL https://download.opensuse.org/repositories/home:trevorsandy/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_trevorsandy.gpg > /dev/null
  3. sudo apt update
  4. sudo apt install lpub3d


