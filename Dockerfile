FROM ubuntu:latest

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install build-essential libevent-dev libglew-dev libglfw3-dev

RUN apt-get -y install xvfb ffmpeg obs-studio git

# Build pixel nuke
RUN git clone https://github.com/defnull/pixelflut /pixelflut ; \
    cd /pixelflut/pixelnuke; \
    make

EXPOSE 1337

COPY ./entrypoint.sh /entrypoint.sh
CMD xvfb-run /entrypoint.sh
