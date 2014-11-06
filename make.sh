#!/bin/bash
SYS=`uname`
ARCH=`uname -m`
git submodule update --init
cd jd-cli
if [[ "$SYS" = "Darwin" ]]
then
	if [[ "$ARCH" = "x86_64" ]]
	then
		make osx64
	else
		make osx32
	fi
	ln -s ./osx/apktool apktool
elif [[ "$SYS" = "Linux" ]]
then
	if [[ "$ARCH" = "x86_64" ]]
	then
		make linux64
	else
		make linux32
	fi
fi
cd ..
pwd
