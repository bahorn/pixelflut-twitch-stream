XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth

build:
	docker build . -t pixelnuke:latest

run:
	docker run -e STREAM_KEY=${STREAM_KEY} -p 1337:1337 -it pixelnuke:latest

gui:
	xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f ${XAUTH} nmerge -
	docker run -ti -v ${XSOCK}:${XSOCK} -v ${XAUTH}:${XAUTH} -e XAUTHORITY=${XAUTH} -e DISPLAY=${DISPLAY} -p 1337:1337 pixelnuke:latest /pixelflut/pixelnuke/pixelnuke
