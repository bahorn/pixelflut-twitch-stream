FROM ubuntu:latest

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install build-essential libevent-dev libglew-dev libglfw3-dev

RUN apt-get -y install xvfb ffmpeg git xdotool unclutter python3 python3-pip

# Build pixel nuke
RUN git clone https://github.com/defnull/pixelflut /pixelflut ; \
    cd /pixelflut/pixelnuke; \
    sed -i -e "s/px_width = 1024/px_width = 1920/" -e "s/px_height = 1024/px_height = 1080/" -e "s/1024/1920/g" pixelnuke.c; \
    sed -i -e 's/glfwCreateWindow(800, 600, "Pixelflut", NULL, NULL);/glfwCreateWindow(1920, 1080, "Pixelflut", NULL, NULL);/' -e "s/1024/1920/g" canvas.c; \
    make

# Now add the bot into the container
COPY bot /bot
RUN cd /bot; \
    pip3 install -r requirements.txt

EXPOSE 1337
COPY ./entrypoint.sh /entrypoint.sh
CMD xvfb-run -n 99 --server-args="-screen 0 1920x1080x24" /entrypoint.sh
