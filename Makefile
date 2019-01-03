XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth

build:
	docker build . -t pixelnuke:latest

run:
	docker run \
		-e STREAM_KEY=${STREAM_KEY} \
		-e BOT_USERNAME=${BOT_USERNAME} \
		-e CHANNEL_NAME=${CHANNEL_NAME} \
		-e OAUTH_TOKEN=${OAUTH_TOKEN} \
		-e PIXELFLUT_HOST=${PIXELFLUT_HOST} \
		-e PIXELFLUT_PORT=${PIXELFLUT_PORT} \
		-e IRC_HOST=${IRC_HOST} \
		-e IRC_PORT=${IRC_PORT} \
		-p 1337:1337 -it pixelnuke:latest

gui:
	# Hack taken from:
	# https://stackoverflow.com/questions/16296753/can-you-run-gui-applications-in-a-docker-container
	xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f ${XAUTH} nmerge -
	docker run -ti -v ${XSOCK}:${XSOCK} -v ${XAUTH}:${XAUTH} -e XAUTHORITY=${XAUTH} -e DISPLAY=${DISPLAY} -p 1337:1337 pixelnuke:latest /pixelflut/pixelnuke/pixelnuke
