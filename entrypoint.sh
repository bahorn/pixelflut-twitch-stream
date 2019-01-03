INRES="1920x1080" # input resolution
OUTRES="1920x1080" # output resolution
FPS="15" # target FPS
GOP="30" # i-frame interval, should be double of FPS, 
GOPMIN="15" # min i-frame interval, should be equal to fps, 
THREADS="2" # max 6
CBR="1000k" # constant bitrate (should be between 1000k - 3000k)
QUALITY="ultrafast"  # one of the many FFMPEG preset
AUDIO_RATE="44100"
SERVER="live-lhr" # London


unclutter -idle 0 & \
    /pixelflut/pixelnuke/pixelnuke & \
    ffmpeg -f x11grab -video_size $INRES -i $DISPLAY -s "$INRES" -r "$FPS" -f flv -ac 2 \
    -vcodec libx264 -g $GOP -keyint_min $GOPMIN -b:v $CBR -minrate $CBR -maxrate $CBR -pix_fmt yuv420p\
    -s $OUTRES -preset $QUALITY -tune film -acodec libmp3lame -threads $THREADS -strict normal \
    -bufsize $CBR "rtmp://$SERVER.twitch.tv/app/$STREAM_KEY" & \
    python3 /bot
