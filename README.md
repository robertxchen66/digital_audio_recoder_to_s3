{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # digital_audio_recoder_to_s3\
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
  AWS account and generate S3 key and secret\
\
Put files in Downloads directory to the /home/pi/Downloads directory,\
replace the keys and secrete in the "passwd-s3fs" file,\
add two lins in the crontab-add to the buttom of the "crontab -e" and save.\
Reboot, the recording should start automatically. }