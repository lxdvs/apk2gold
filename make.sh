#!/bin/bash
SYS=`uname`
ARCH=`uname -m`
git submodule update --init
cd jd-cmd
mvn clean package
cp jd-cli/target/jd-cli.jar .. 
cd ..
pwd
