#!/bin/sh
DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -o /home/pi/main_software/data_acquisition/images/$DATE.jpg

echo /home/pi/main_software/data_acquisition/images/$DATE.jpg