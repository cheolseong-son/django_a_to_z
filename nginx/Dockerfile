# 도커 제공 최신버전 사용
FROM nginx:latest

# 이 이미지 안의 default.conf에는 도커가 제공하는 Nginx의 기본 설정값이 들어 있음 rm 명령어로 제거
RUN rm /etc/nginx/conf.d/default.conf

# 대신 로컬에서 새로 만든 Nginx 설정 정보를 Nginx이미지에 복사해 넣는다.
COPY nginx.conf /etc/nginx/conf.d