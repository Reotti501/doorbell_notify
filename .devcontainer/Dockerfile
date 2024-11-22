# Python - DevContiner公式イメージ
# * GitHub | devcontainer/pyhton : https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:latest

# [オプション] 追加パッケージのインストール
#
# 使い方 :
#  * 「&& apt-get -y install --no-install-recommends <install packages>\」
#    のコメントアウトを外し、<install packages>の部分にパッケージを追加
#

WORKDIR /home/reotti/project

RUN apt-get update \
    # && export DEBIAN_FRONTEND=noninteractive \
    && apt-get upgrade -y \
    && apt-get -y install --no-install-recommends \
        libasound-dev \
        libportaudio2 \
        libportaudiocpp0 \
        portaudio19-dev \
    # && apt-get -y install --no-install-recommends <install packages> \
    && pip install --upgrade pip \
    && pip install \
        matplotlib \
        numpy \
        pandas \
        pyaudio \
        python-dotenv \
        requests \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
