# Pixelnuke in Docker + Twitch Streaming

This uses streams the pixelnuke[1] server to twitch.

Stole the ffmpeg command from [2]. Need to adjust the setting used, etc.

## Usage

```
make
export STREAM_KEY=<YOUR_TWITCH_KEY>
make run
```

## References

```
[1] https://github.com/defnull/pixelflut
[2] https://wiki.archlinux.org/index.php/Streaming_to_twitch.tv#Ffmpeg_solutions
```
