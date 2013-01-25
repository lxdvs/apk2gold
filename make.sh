#!/bin/bash
ARCH=`uname`
echo "$ARCH"
git submodule update --init
cd jd-cli
if [[ "$ARCH" = "Darwin" ]]
then
make osx
cd ..
ln -s ./osx/apktool apktool
elif [[ "$ARCH" = "Linux" ]]
then
make linux
ln -s ./linux/apktool apktool
fi
cd ..
pwd
