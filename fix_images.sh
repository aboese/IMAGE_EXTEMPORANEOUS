#!/bin/bash
#
#  This provides basic image handling
#  Alex Booese - 2015
#
SOURCE_DIR="" # image source directory
HOME_DIR=""   # script home directory

/bin/echo Adding Tags
/usr/bin/exiftool -v "-FileModifyDate>DateTimeOriginal" $SOURCE_DIR/*
/bin/echo Removing backup imgs
/bin/rm -rf $SOURCE_DIR/*original
/bin/echo Rename files for reference
/usr/bin/rename 's/\(\)//' $SOURCE_DIR/*.jpg
/usr/bin/rename 's/camera1_id/camera_1_location/' $SOURCE_DIR/*.jpg 
/bin/echo Place files into correct date folder
/usr/bin/python3 $HOME_DIR/img_org.py $SOURCE_DIR $HOME_DIR 

