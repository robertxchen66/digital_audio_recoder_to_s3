import ffmpy3
import subprocess
import time

timestr =time.strftime("%Y%m%d_%H%M%S")
print(timestr)

ff=ffmpy3.FFmpeg(
#    inputs={'pipe:0': '-f alsa -sample_rate 44100 -i hw:1,0 -t 30'},
    inputs={'hw:1,0': '-f alsa -sample_rate 44100 -t 3590 -y'},
#    inputs={'test.avi':None},
#    outputs={'/home/pi/Downloads/' + time.strftime("%Y%m%d_%H%M%S") + '.mp3': None}
    outputs={'/home/pi/Downloads/' + time.strftime("%d_%H%M") + '.mp3': None}
)

ff.run()