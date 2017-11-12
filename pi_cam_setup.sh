#Camera Integration With Pi:

#Image:
sudo apt-get install fswebcam
fswebcam -p YUYV -d /dev/video0 -r 640x480 $DIR/$filename

#Voice:
arecord -D sysdefault:CARD=C170 test.wav --format S16_LE --rate 44100 -c1 test.wav
