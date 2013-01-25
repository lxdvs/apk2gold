ARCH=`uname`
echo "$ARCH"
git submodule update --init
cd jd-cli
if [[ "$ARCH" -eq "Darwin" ]]
then
make osx
cd ..
ln -s ./osx/apktool apktool
elif [[ "$ARCH" -eq "Linux" ]]
then
make linux
ln -s ./linux/apktool apktool
fi
cd ..
pwd
