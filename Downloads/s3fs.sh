!/bin/bash

/usr/bin/s3fs yourbucket -o accessKeyId=AKIAZ5J5FVWGY323VAWU -o secretAccessKey=GsROZKQ6esTb5C0u2xgZoK7i6j/tTmWFSnbJQfSY /mnt/s3
/usr/bin/rsync -avz --delete /home/pi/Downloads/*.wav /mnt/s3
/bin/umount /mnt/s3
