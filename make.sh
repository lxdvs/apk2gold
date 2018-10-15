#!/bin/bash
SYS=`uname`
ARCH=`uname -m`
git submodule update --init
cd jd-cmd

which mvn > /dev/null 2>&1
[[ ! "$?" -eq 0 ]] && {

	which apt > /dev/null 2>&1
	if [[ "$?" -eq 0 ]]; then
		echo "[*] Installing maven..."
		sudo apt-get install maven
	else
		echo "[!] This script require maven installed to work"
		exit 1
	fi
}

mvn clean package
cp jd-cli/target/jd-cli.jar .. 
cd ..
pwd
