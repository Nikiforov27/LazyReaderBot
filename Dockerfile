FROM debian:bookworm
COPY . /bot
WORKDIR /bot
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 python3-pip python3-venv python3.11-venv python3-setuptools python3-wheel libspeechd-dev build-essential espeak-ng portaudio19-dev flac opus-tools
RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN pip3 install -r requirements.txt
CMD ["python3", "main_bot.py"]
