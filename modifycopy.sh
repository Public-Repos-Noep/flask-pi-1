#!/bin/sh
BASEDIR=/home/pi/mnt

#check if directory is already mounted
ISMOUNTED=$(mount |grep $BASEDIR)
if [ "ISMOUNTED" ] ; then
	echo "unmount device"
	sudo umount -l $BASEDIR
fi

#make timestamp
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
echo current time : $TIMESTAMP

PROJECTDIR='/home/pi/Projects/flask-pi-1'
PICTURE='modify.jpeg'
FILEDIR='flask-pi'

#mount android device
echo "MOUNT ANDROID DEVICE"
jmtpfs $BASEDIR

cd $BASEDIR
DIR=$(ls $BASEDIR)

echo finded directory $DIR
echo $DIR

if [ ! -d $BASEDIR/"$DIR"/$FILEDIR ] ; then
	echo "create directory"
	mkdir $BASEDIR/"$DIR"/$FILEDIR
fi

echo "FILE TRANSFER"
#copy file
echo $PROJECTDIR/$PICTURE
echo $BASEDIR/"$DIR"/$FILEDIR/$TIMESTAMP-$PICTURE
cp $PROJECTDIR/$PICTURE $BASEDIR/"$DIR"/$FILEDIR/$TIMESTAMP-$PICTURE

#unmount
echo "UNMOUNT ANDROID DEVICE"
sudo umount -l $BASEDIR


echo "FILECOPY SUCCESS"
