#!/bin/bash
SYS=`uname`
ARCH=`uname -m`
git submodule update --init
cd jd-cli
wget https://github.com/kolipass/jd-core-java/releases/download/1.2/jd-core-java-1.2.jar
if [[ "$SYS" = "Darwin" ]]
then
	if [[ "$ARCH" = "x86_64" ]]
	then
		make osx64
	else
		make osx32
	fi
	cd ..
	ln -s ./osx/apktool apktool
elif [[ "$SYS" = "Linux" ]]
then
	if [[ "$ARCH" = "x86_64" ]]
	then
		make linux64
	else
		make linux32
	fi
	cd ..
	ln -s ./linux/apktool apktool
fi
pwd
