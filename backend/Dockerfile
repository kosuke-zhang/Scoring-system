FROM python:3.7.3

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package -r requirements.txt

