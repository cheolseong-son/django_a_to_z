<<<<<<< HEAD
# Python 3.8 (alpine 리눅스 기반)을 base 이미지로 사용
FROM python:3.8.0-alpine

# 프로젝트의 작업 폴더를 지정
WORKDIR /usr/app

# 도커를 이용할 때는 .pyc파일을 생성하지 않도록 함
ENV PYTHONDONTWRITEBYTECODE 1

# 버퍼링 없이 즉각적으로 출력하게 만듬
ENV PYTHONUNBUFFERED 1

# requirements.txt에서 살펴본 라이브러리를 설치하기 우해 필요한 gcc, musl-dev 등을 미리 설치
RUN apk update
RUN apk add libffi-dev
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

# 현재 위치에 있는 모든 파일을 WORKDIR로 복사
COPY . /usr/app/

# requirements.txt에 나열된 라이브러리를 설치
=======
# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev #--(5.2)

COPY . /usr/src/app/
# install dependencies
>>>>>>> master
RUN pip install --upgrade pip
RUN pip install -r requirements.txt