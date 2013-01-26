#!/bin/bash
ARCH=`uname`
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
cd ..
ln -s ./linux/apktool apktool
fi
pwd
