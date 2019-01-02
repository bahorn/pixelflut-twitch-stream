build:
	docker build . -t pixelnuke:latest

run:
	docker run -e STREAM_KEY=${STREAM_KEY} -p 1337:1337 -it pixelnuke:latest
