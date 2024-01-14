FROM python:latest AS builder
COPY . /bot
WORKDIR /bot
RUN apt update -y
RUN apt upgrade -y
RUN apt install lame tar git wget curl python3 python3-pip python3-venv python3.11-venv python3-setuptools python3-wheel libspeechd-dev build-essential espeak-ng portaudio19-dev flac opus-tools -y
RUN pip3 install -r requirements.txt
CMD ["python3", "main_bot.py"]
