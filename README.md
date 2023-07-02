
# digital_audio_recoder_to_s3
This project is to use Raspberry Pi to recorder audio and store in S3 as hourly mp3 files. \
Prerequisites:\
  Respberry Pi with WiFI\
  sound capture card or USB dungle (I am using Andrea Communications USB-SA)\
  Raspian version 5.10\
  Python 3\
  pip3\
  ffmepg\
  ffmpy3\
  alsa\
  rsync\
  s3fs\
  AWS account and generate S3 key and secret\
\
Create a s3 directory under /mnt, and make it writeable by other users.
```
sudo mkdir /mnt/s3
chmod o+w /mnt/s3
```
Put files in Downloads directory to the /home/pi/Downloads directory,\
replace the keys and secrete in the "passwd-s3fs" file,\
add two lins in the crontab-add to the buttom of the "crontab -e" and save.\
Reboot, the recording should start automatically.

https://blog.technotesdesk.com/2014/01/03/mount-s3-bucket-as-a-local-drive-and-use-rsync-to-sync-files-on-debian-7/
