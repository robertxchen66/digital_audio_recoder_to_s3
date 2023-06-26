#!/bin/bash

/usr/bin/s3fs audiostreamsfrommimosa -o nonempty -o passwd_file=/home/pi/passwd-s3fs /mnt/s3
/usr/bin/rsync -avz --delete /home/pi/Downloads /mnt/s3
/bin/umount /mnt/s3
