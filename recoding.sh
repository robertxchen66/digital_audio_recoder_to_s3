sudo ffmpeg -f alsa -sample_rate 44100 -i hw:1,0 -t 100 -strftime 1 "/home/pi/Downloads/%Y%m%d_%H%M%S.mp3"